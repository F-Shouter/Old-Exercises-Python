lista=[]
for n in range(0,6):
    num=int(input("numero:"))
    lista.append(num)
    
for x in lista:
    print("posição:",lista.index(x))
    print("numero:",x)
    print("\n")
