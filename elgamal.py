'''q,al,xa=19,10,5
ya=(al**xa)%q
k=6
K=(ya**k)%q
msg="hello"
x=0
l=[[x for i in range(2)]for j in range(len(msg))]
#print(l)
c=0
for m in msg:
    ce=0
    m=ord(m)-97
    c1=(al**k)%q
    c2=(K*m)%q
    l[c][ce]=c1
    l[c][ce+1]=c2
    c=c+1
cd=0
print(l)


def inv(K,q):
    K=K%q
    for i in range(1,q):
        if((K*i)%m==1):
            return i
pt=[]
for i in range(len(l)):
    ce=0
    ele=l[cd][ce]
    ele1=l[cd][ce+1]
    print(ele,ele1)
    K=(ele**xa)%q
    print(K)
    K1=inv(q,K)
    #print("K-1=",K1)
    M=(ele1*K1)%q
    M=chr(M+97)
    pt.append(M)
    cd=cd+1
print(pt)
'''

def prim_root(val):
    totient=tot(val)
    roots=[]
    exp=len(totient)
    for x in totient:
        y=1
        while pow(x,y,val)!=1:
            y+=1
        if y==exp:
            roots+=[x]
    return roots
prim_root(7)
