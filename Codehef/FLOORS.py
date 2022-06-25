# cook your dish here
import math
t=int(input())
while(t>0):
    x,y=map(int,input().split())
    # minimum=min(x,y)
    # maximum=max(x,y)
    # for i in range(0,10):
    #     if(minimum%10!=0):
    #         mod=(int(minimum/10)*10)
    #         if((minimum>mod and minimum<=(mod+10)) and (maximum>mod and maximum<=(mod+10))):
    #             print(i)
    #             break
    #         else:
    #             minimum+=10
    #     else:
    #         mod=(int(minimum/10)*10)
    #         if((minimum+1>mod and minimum+1<=(mod+10)) and (maximum>mod and maximum<=(mod+10))):
    #             print(i+1)
    #             break
    #         else:
    #             minimum+=10
    x=((x/10))
    y=((y/10))
    x=math.ceil(x)
    y=math.ceil(y)
    print(abs(x-y))
    t-=1