string=input().strip()
if string!="":
    new=string.lower()
    listy=list(new)
    while "a" in listy:
        listy.remove("a")
    while "e" in listy:
        listy.remove("e")
    while "i" in listy:
        listy.remove("i")
    while "o" in listy:
        listy.remove("o")
    while "u" in listy:
        listy.remove("u")
    while "y" in listy:
        listy.remove("y")
    result=".".join(listy)
    print(".",result,sep="")
else:
    print("")
