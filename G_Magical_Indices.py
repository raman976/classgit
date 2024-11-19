T=int(input())
for x in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    b=len(a)
    count=0
    t1=True
    t2=True
    for i in range(b):
        test_list1=a[a[0]:a[i]]
        test_list2=a[a[i]:]
        for j in test_list1:
            if a[i]<j:
                t1=False
                break
        for j in test_list2:
            if a[i]>j:
                t2=False
                break
        if t2==True and t1==True:
            count+=1
        else:
            count=0
        print(count)

