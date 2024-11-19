n=int(input())
if (n)**0.5==int(n/(n)**0.5):
    print(int(4*(n)**0.5))
else:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    a=count//2-1
    b=count//2
    print(2*(d[a]+d[b]))
