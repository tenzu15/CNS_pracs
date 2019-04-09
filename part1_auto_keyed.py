

st="hello"
k=12
lst=[]
for i in range(0,len(st)):
	ch=ord(st[i])
	if (i == 0):
		ch=((ch+ k-97)%26)+97
	else:
		ch=((ch+ ord(st[i-1])-194)%26)+97
	lst.append(ch)
#print(lst)
st1="";
for i in range(len(n)):
	st1=st1+chr(lst[i])
print(st1)


#st1="enemyattackstonight"
key =[3,1,4,5,2]
n= len(st1)% len(key)
for i in range(len(key)-n) :
	st1=st1+"z"
n1=len(key)
st2=list(st1)
st3=[]

for i in range(0,len(st2),5):
	#print(i)
	st2[i],st2[i+1],st2[i+2],st2[i+3],st2[i+4]=st2[i+2],st2[i],st2[i+3],st2[i+4],st2[i+1]
print(st2)

for i in range(len(key)):
	for j in range(len(st2)):
		if (j%n1==i):
			st3.append(st2[j])
	#st3=''.join(st2)
print(st3)




