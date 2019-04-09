from math import *
key=[['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','T','P']]
plaintext="HELLO I AM SHREEYAA"
plain=[]
encr=""
plaintext=plaintext.replace(" ","")
if len(plaintext) % 2== 1:
	plaintext=plaintext+"X"
plain=plaintext.split()
last=plain[0]
for i in range(1,len(plain)):
	if plain[i]==last:
		plain[i]="X"
	last=plain[i]
for i in range(0,len(plain),2):
	a=plain[i]
	b=plain[i+1]
	ak=[]
	bk=[]
	for j in range(5):
		for k in range(5):
			if a==key[j][k]:
				ak=[j,k]
			if b==key[j][k]:
				bk=[j,k]
		if len(ak)>0 and len(bk)>0:
			break
	if ak[0]==bk[0]:
		encr+=key[ak[0]][ak[1]+1]
		encr+=key[bk[0]][bk[1]+1]
	elif ak[1]==bk[1]:
		encr+=key[ak[0]+1][ak[1]]
		encr+=key[bk[0]+1][bk[1]]
	else:
		encr+=key[ak[0]][bk[1]]
		encr+=key[bk[0]][ak[1]]
keyed=[3,1,4,5,2]
m=4 #rows
e=[]
b=len(encr)%m
b=m-b
for i in range(b):
	encr+="X"
cols=len(encr)/m
for i in range(0,cols):
	k=[]
	for i in range(i,len(encr),cols):
		k.append()
	l.append(k)
for i in keyed:
	e.append(l[i])
for i in e:
	for j in e:
		encr+=j
print(encr)





