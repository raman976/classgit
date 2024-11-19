t=int(input())
for i in range(t):
    n=int(input())
    if n==1 or n==2 or n==3 or n==4:
        print(-1)
    else:
        even=[]
        odd=[]
        for i in range(1,n+1):
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        ind=(len(odd)-1)//2
        popped=odd.pop()
        odd.insert(ind,popped)
        list3=even+odd
        for i in list3:
            print(i,end=" ")





