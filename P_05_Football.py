num=input()
lis=list(num)
if len(lis)<7:
    print("NO")
else:
    for i in range(len(lis)):
        while len(lis)-i>=7:
            count=0
            if lis[i]==lis[i+1]==lis[i+2]==lis[i+3]==lis[i+4]==lis[i+5]==lis[i+6]:
                count+=1
if count>=1:
    print("YES")
else:
    print("NO")
                               
             
