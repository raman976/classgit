n=int(input())
k=input()
listy=list(k)
for i in k:
    listy.append(int(i))
n=int(n//11)
a=listy.count(8)
if int(a)>n:
    print(n)
if int(a)<n:
    print(a)
if a==int(n):
    print(a)