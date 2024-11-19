a,b,x,y=map(int,input().split())
count=0
for i in range(1,a+1):
    for j in range(1,b+1):
        if i/j==x/y:
            count+=1
print(count)
