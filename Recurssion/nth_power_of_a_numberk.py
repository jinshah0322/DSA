#Practice - https://bit.ly/3FPCfV3
def pow(x,n):
    if(x!=0 and n==0):
        return 1
    if(x==0 and n==0):
        return 1
    if(n==1):
        return x
    else:
        mul=x*pow(x,n-1)
        return mul
t=int(input())
while t>0:
    x,n=map(int,input().split())
    ans=pow(x,n)
    print(ans)
    t-=1