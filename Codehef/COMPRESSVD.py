# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(0,len(l)-1):
        if(l[i]==l[i+1]):
            l[i]=-1
    print(len(l)-l.count(-1))
    t-=1