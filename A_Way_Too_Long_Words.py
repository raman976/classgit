n=int(input())
for i in range(n):
    a=input()
    b=list(a)
    if len(b)>10:
        print(b[0],len(b)-2,b[-1],sep="")
    else:
        print(a)