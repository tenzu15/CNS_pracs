import socket
s=socket.socket()
port=12345
s.bind(('',port))
s.listen(5)
while True:
    c,addr=s.accept()
    n=7
    g=31
    x=5
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def primroot(modulo):
        
    a=(g**x)%n
    a=str(a)
    c.send(a.encode())
    b=(c.recv(1024)).decode()
    b=int(b)
    #print("b=",b)
    k1=(b**x)%n
    print("k1=",k1)
