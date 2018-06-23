import math,csv
def distance (p1,p2):
	return Math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def getClusters(points,centroid):
	clusters={}
	for(p in points):
		d_old=-1
		for(c in centroid):
			d_new=distance(p,centroid[c])
			if(d_new<d_old or d_old==-1):
				clusters[p]=c
			d_old=d_new
	return clusters

points=[];clusters={};centroid={};result={}
with open("database.csv") as dataset:
	trans=list(csv.reader(dataset,delimiter=","))
for i in trans:
	p_temp=[]
	for j in i:
		p_temp.append(float(j))
	points.append(p_temp)
points=[tuple(i) for i in points]
#print the points

n_c=len(points)+1
while(n_c>len(points)):
	n_c=int(input("enter no of clusters:"))
	if(n_c>len(points)):
		#print sorry cannot make these many clusters

for i in range(0,n_c):
	centroid[i]=points[i]
getClusters(points,clusters)

c_old={}
while(c_old!=clusters):
	c_old=clusters
	for(i in range(0,n_c)):
		x=0;y=0;count=0
		for p in points:
			if clusters[p]==i:
				x+=p[0];y+=p[1];count+=1
			x/=count;y/=count
		centroid[i]=(x,y)
	clusters=getClusters(points,clusters)

for key,values in sorted(clusters.items()):
	result.setdefault(value,[]).append(key)
for i in result:
	print("CLuster",i+1,"->",result[i],"with Centroid =",centroid[i])