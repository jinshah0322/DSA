#question link:https://bit.ly/39ID71t

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    pass
n=int(input())
if n>=0:
    x=factorial(n)
    print (x)
else:
    print("Error")