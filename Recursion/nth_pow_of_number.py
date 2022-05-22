#Practice - https://bit.ly/3FPCfV3
def pow(x,n):
    if(n==0):
        return 1
    temp=pow(x,n//2)
    if(n%2==1):
        return temp*temp*x
    return temp*temp
t=int(input())
while t>0:
    x,n=map(int,input().split())
    ans=pow(x,n)
    print(ans)
    t-=1