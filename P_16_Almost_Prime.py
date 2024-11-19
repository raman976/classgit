def check_prime(k):
    if k==1:
        return False
    elif k==2:
        return True
    elif k%2==0:
        return False
    for i in range(3,int((k)**0.5)+1):
        if k%i==0:
            return False
    return True
def count_prime(B):
    count=0
    for i in range(1,B+1):
        if check_prime(i)==True:
            count+=1
    if count==2:
        return True
    else:
        return False
n=int(input())
final=0
for i in range(1,n+1):
    if count_prime(i)==True:
        final+=1
print(final)
