n,L,a=map(int,input().split())
for i in range(n):
    t,l=map(int,input().split())
    sum=t+l
    L=L-sum
print(L//a)