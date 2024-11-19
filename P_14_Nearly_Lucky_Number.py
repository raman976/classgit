n=input()
lis=[int(i) for i in n]
count=0
if n=="7" or n=="4":
    print("NO")
else:
    for i in lis:
        if i==4 or i==7:
            count+=1
    if count==7 or count==4:
        print("YES")
    else:
        print("NO")