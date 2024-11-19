t=int(input())
for i in range(t):
    final=0
    n=int(input())
    a=list(map(int,input().split()))
    se=set(a)
    count=0
    for i in se:
        p=a.count(i)
        if p>=2:
            d=p//2
            count+=d
    print(count)