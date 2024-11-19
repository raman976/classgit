n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    k=a*60+b
    print(24*60-k)