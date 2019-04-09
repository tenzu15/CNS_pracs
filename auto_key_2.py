
key=[2,5,4,1,3]
st1="ettheakimaotycnzntsg"
mod=int(len(st1)/len(key))
print(mod)
st2=[]
st3=[]
st=""
for i in range(len(key)):
	st2=[]
	for j in range(len(st1)):
		if (j%mod==i):
			st2.append(st1[j])
	#st2[0],st2[1],st2[2],st2[3],st2[4]=st2[1],st2[4],st2[0],st2[2],st2[3]
	st3.append(st2)
#print(st3)
for i in range(mod):
	st3[i][0],st3[i][1],st3[i][2],st3[i][3],st3[i][4]=st3[i][1],st3[i][4],st3[i][0],st3[i][2],st3[i][3]
#print(st3)

for i in range(mod):
	st=st+st3[i][0]+st3[i][1]+st3[i][2]+st3[i][3]+st3[i][4]
#print(st)

#st="mtmtcmktwdwj"
k=12
a=0
st4=""
b=0
for i in range(len(st)):
	if i==0:
		a=ord(st[0])-k-97
		st4=st4+ chr(b+97)
               
	if not i==0:
		c=ord(st[i])
		b=(c-ord(st4[i-1]))%26
		#print(b," ",c)
		d=chr(b+97)
	
		st4=st4+d
print(st4)


