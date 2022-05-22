#Problem link:- https://bit.ly/3NkbBWJ
def fibo(n):
    if(n==1 or n==2):
        return 1
    else:
        partialnminus1=fibo(n-1)
        partialnminus2=fibo(n-2)
        return partialnminus1+partialnminus2
n=int(input())
print(fibo(n)) 