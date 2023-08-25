lista=[]
for n in range(0,6):
    num=int(input("Insira um número inteiro:"))
    lista.append(num)
for x in lista:
    print("elemento:",x)
    print("posição:",lista.index(x))
    print("\n")