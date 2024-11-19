t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    k=a*60+b
    print(24*60-k)
