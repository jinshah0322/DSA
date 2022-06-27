# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    s=input()
    string=""
    dna=[s[i:i+2] for i in range(0,len(s),2)]
    for i in dna:
        if(i=='00'):
            string+='A'
        elif(i=='01'):
            string+='T'
        elif(i=='10'):
            string+='C'
        elif(i=='11'):
            string+='G'
    print(string)
    t-=1