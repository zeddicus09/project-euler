import time as t
z=t.time()
s=0
for i in range(0,1000):
    if i%3==0 or i%5==0:
        s=s+i
print(s)
y=t.time()
print('le temps d\'execution est :',y-z)

