#find sum of n natural numbers
def sum(n):
    if(n==1):
        return 1
    else:
        partialsum=sum(n-1)
        return n+partialsum
n=int(input())
if(n<0):
    print("Enter valid number")
else:
    x=sum(n)
    print(x)