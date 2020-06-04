import time as t
z=t.time()
a=1
b=2
c=3
s=2
while c<=4000000:
    a=b
    b=c
    c=a+b
    if(c%2==0):
        s=s+c
print(s)
y=t.time()
print('le temps execution est :',y-z)