n,k=map(int,input().split())
d=list(map(int,input().split()))
n=[]
for i in d:
    n.append(i+k)
count=0
for i in n:
    if i<=5:
        count+=1
print(count//3)

