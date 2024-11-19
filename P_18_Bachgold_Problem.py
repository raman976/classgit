def prime_checker(k):
    if k<=1:
        return False
    elif k==2:
        return True
    elif k%2==0:
        return False
    for i in range(3,int(k**0.5)+1):
        if k%i==0:
            return False
    return True
n=int(input())
d=[]
for i in range(1,n+1):
    if prime_checker(i)==True:
        d.append(i)
sum=0
for i in d:
    if sum==n:
        break
    else:
        print(i,end=" ")
        sum+=i