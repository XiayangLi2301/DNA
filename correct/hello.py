import random
def random_int(length,a,b):
    list = []
    count = 0
    while(count<length):
        number = random.randint(a,b)
        list.append(number)
        count = count + 1
    return list
a=[]
c=[]

for i in range(100):
    b=random_int(10,0,1)
    a.append(b)
i = 0
while i < 100:
    b=random_int(2,1,10)
    if b[0]!=b[1]:
        c.append(b)
        i=i+1
print(c)