import math
t=int(input())
while(t>0):
    n=int(input())
    if((n<=4)):
        print(n)
    else:
        div=math.ceil((n*4)/5)
        print(div)
    t-=1