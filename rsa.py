p=17
q=11
n=p*q
fn=(p-1)*(q-1)
e=7
def inv(a,m):
    a=a%m
    for x in range(1,m):
        if((a*x)%m==1):
            return x
    return 1

e1=inv(e,fn)
d=e1%fn
#print(d)
pu=[e,n]
pr=[d,n]
print("n=",n)
def encrypt(m,e,n):
    c=[]
    for i in m:
        m1=ord(i)-97
        m2=(m1**e)%n
        c.append(chr(m2))
        c1=''.join(c)
    print("encrypted=",c1)
    return c
def decrypt(c,d,n):
    p=[]
    #print(c)
    for i in range(len(c)):
        c1=ord(c[i])
        c1=(c1**d)%n
        p.append(chr(c1+97))
        p1=''.join(p)
    return p1

st=input("enter plain text")
enc=encrypt(st,e,n)
dec=decrypt(enc,d,n)
#print("encrpyted=",enc)
print("decrypted=",dec)
