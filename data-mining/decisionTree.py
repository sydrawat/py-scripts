import csv,math,copy
class  decisionTree():
    def __init__(self,data,parent):
        self.value=data
        self.child=[]
        self.parent=parent
    def addChild(self,data):
        self.child.append(decisionTree(data,self.value))
    def __str__(self, level=0):
        tree = "\t"*level+self.value+"\n"
        for children in self.child:
            tree += children.__str__(level+1)
        return tree

def getInfo(database):
    d={}
    count=0
    for i in database:
        d[i]=d.get(i,0)+1
        count+=1
    sum=0
    for i in d:
        p=d[i]/count
        sum-=(p*math.log2(p))
    return sum

def getInfoGain(database,label,info):
    d={}
    count=0
    for i in database:
        d[i]=d.get(i,0)+1
        count+=1
    sum=0
    for i in d:
        if d[i]==0:
            continue
        l=[]
        p=d[i]/count
        for j in range(len(database)):
            if database[j]==i:
                l.append(label[j])
        sum+=p*getInfo(l)
    return info-sum,d    

def updateDB(trans_db,attr_name,attribute_list):
    index=attribute_list.index(done[-1])
    temp_trans_db=[]
    for i in trans_db:
        if i[index]==attr_name:
            temp_trans_db.append(i)
    temp_trans={}
    for i in attribute_list:
        temp_trans[i]=[]
    for i in range(0,len(temp_trans_db)):
        for j in range(len(temp_trans_db[i])):
            temp_trans[attribute_list[j]].append(temp_trans_db[i][j])
    for i in done:
        if i in temp_trans:
            del(temp_trans[i])
    return temp_trans,temp_trans_db

trans={};label=None;info={};d={};dt=None;node_databases={}
training=input("Enter the filename where the training data is stored : ").strip()
with open(training) as transactions:
    trans_db=list(csv.reader(transactions,delimiter=','))
for i in trans_db[0]:
    trans[i]=[]
for i in range(1,len(trans_db)):
    for j in range(len(trans_db[i])):
        trans[trans_db[0][j]].append(trans_db[i][j])
i=1
for attribute in trans_db[0]:
    print(i,". ",attribute)
    i+=1
n=int(input("Choose the attribute to be used as the label : "))
label=trans_db[0][n-1]
temp_trans=copy.copy(trans)
temp_trans_db=copy.copy(trans_db)
attribute_list=copy.copy(trans_db[0])
root="";parent_root=None;nodes=[];done=[]
while True:
    infoGain=0
    if len(set(temp_trans[label]))==1:
        dt.addChild(temp_trans[label][0])
    else:
        info=getInfo(temp_trans[label])
        for attribute in attribute_list:
            d_temp={}
            if attribute==label or attribute in done:
                continue
            temp,d_temp=getInfoGain(temp_trans[attribute],temp_trans[label],info)
            if temp>infoGain:
                infoGain=temp
                root=attribute
                d=d_temp
        if not dt:
            dt=decisionTree(root,[])
            nodes.append(dt)
            parent_root=dt
        elif root in attribute_list:
            dt.addChild(root)
            dt=dt.child[0]
            nodes.append(dt)
        if not dt.value in node_databases.keys():
            node_databases[dt.value]=temp_trans_db
        for i in d:
            dt.addChild(i)
        for i in dt.child:
            nodes.append(i)
    if nodes[0].value in attribute_list:
        done.append(nodes[0].value)
    del(nodes[0])
    if not nodes:
        break
    if nodes[0].value in attribute_list:
        done.append(nodes[0].value)
        if not nodes[0].value in node_databases.keys():
            node_databases[nodes[0].value]=temp_trans_db
        del(nodes[0])
    dt=nodes[0]
    temp_trans,temp_trans_db=updateDB(node_databases[dt.parent],dt.value,attribute_list)
    if not dt.value in node_databases.keys():
        node_databases[dt.value]=temp_trans_db
    if not nodes:
        break
print(parent_root)
while True:
    details={}
    print('Enter values for the following attributes \n')
    for i in attribute_list:
        if i!=label:
            details[i]=input(i+' : ')
    root=parent_root
    while root.child:
        if root.value in attribute_list:
            value=details[root.value]
            for i in root.child:
                if i.value==value:
                    root=i
        else:
            root=root.child[0]
    print('Predicted value for',label,'is',root)
    ans=input('Predict more details? (y/n) ')
    if ans=='n':
        break