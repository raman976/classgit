t=int(input())
for i in range(t):
    k=int(input())
    a=list(map(int,input().split()))
    required=len(a)-2
    factors=[]
    for p in range(1,int(required**0.5)+1):
        if required%p==0:
            factors.append(p)
        for j in factors:
            if j in a:
                first=j
                b=required//j
                if b in a:
                    second=b
                    break
    print(first,second)
