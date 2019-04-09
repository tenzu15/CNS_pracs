import socket
s=socket.socket()
port=12345
s.connect(('localhost',port))
a=(s.recv(1024)).decode()
a=int(a)
#print("a=",a)
n=7
g=31
y=29
b=(g**y)%n
b=str(b)
s.send(b.encode())
k2=(a**y)%n
print("k2=",k2)
