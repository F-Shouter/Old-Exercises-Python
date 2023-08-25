num=int(input("numero:"))
while num>0:
    if (num//2>1) or (num//3>1):
        print("não primo")
    elif (num/num==1) and (num/1==num):  
        print("primo")
    num=int(input("numero:"))
print("invalido")