import itertools
num = str(input("enter a number: "))
c=[]
for digit in num:
    c.append(int(digit))

print "permutations are:"
list1= list(itertools.permutations(c,len(num)))

for tup in list1:
    str1=''.join(str(i) for i in tup)
    print str1


