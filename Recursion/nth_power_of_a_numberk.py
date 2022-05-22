#Practice - https://bit.ly/3FPCfV3
def pow(x,n):
    if(n==0):
        return 1
    else:
        mul=x*pow(x,n-1)
        return mul
t=int(input())
while t>0:
    x,n=map(int,input().split())
    ans=pow(x,n)
    print(ans)
    t-=1