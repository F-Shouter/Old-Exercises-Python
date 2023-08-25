for n in range(0,10):
    num=int(input("Insira um número inteiro:"))
    if (num%3==0) and (num!=0):
        print("o número inserido é múltiplo de 3")
    if (num>=0):
        print("positivo")
    else:
        print("negativo")
    print("\n")