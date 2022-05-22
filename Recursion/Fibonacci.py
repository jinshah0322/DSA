#Problem link:- https://bit.ly/3NkbBWJ
def fibo(n):
    if(n==1 or n==2):
        return 1
    else:
        p1=fibo(n-1)
        p2=fibo(n-2)
        return p1+p2
n=int(input())
print(fibo(n)) 