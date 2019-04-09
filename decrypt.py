keyed=[3,1,4,5,2]
rev=[0,0,0,0,0]
for i in range(len(keyed)):
	rev[keyed[i]]=i+1
m=4 #rows
e=[]
l=[]
cols=len(encr)/m
for i in range(0,len(encr),m):
	k=[]
	for i in range(i,i+m):
		k.append()
	l.append(k)
for i in keyed:
	e.append(l[i])
for i in e:
	for j in e:
		encr+=j
print(encr)
