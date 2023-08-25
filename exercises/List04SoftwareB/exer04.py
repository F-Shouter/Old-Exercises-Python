lista=[]
for n in range(0,20):
    num=int(input("Insira um número inteiro:"))
    lista.append(num)
x=max(lista)
y=min(lista)
print("\n")
print("Maior elemento:{}, Menor elemento:{}".format(x,y))