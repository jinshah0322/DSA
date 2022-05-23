#Practice - https://bit.ly/39UrBjK
def palindrome(s,start,end):
    if(s[start]!=s[end]):
        return 0
    else:
        if(start==end or start>end):
            return 1
        palindrome(s,start+1,end-1)
        return 1
t=int(input())
while(t>0):
    s=input()
    print(palindrome(s,0,len(s)-1))
    t-=1