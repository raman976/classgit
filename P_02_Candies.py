n=input()
listy=list(map(int,input().split()))
a,b=map(int,input().split())

sum=0
for i in listy[a:b+1]:
    sum+=i
print(sum)