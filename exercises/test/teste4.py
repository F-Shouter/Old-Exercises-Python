lista=[]
i=0
while(i<15):
    x=int(input("Digite um número:"))
    if x not in lista:
        lista.append(x)
        i=i+1
print(lista)


