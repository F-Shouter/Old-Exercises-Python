num=int(input("numero:"))
while num>=1 and num<=7:
    if num==1:
        print("domingo")
    elif num==2:
        print("segunda")
    elif num==3:
        print("terca")
    elif num==4:
        print("quarta")
    elif num==5:
        print("quinta")
    elif num==6:
        print("sexta")
    else:
        print("sabado")
    print("\n")
    num=int(input("numero:"))
print("numero invalido")
