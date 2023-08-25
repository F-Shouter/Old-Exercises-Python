listaA=[]
listaB=[]
x=int(input("valor x:"))
listaA.append(x)
for n in range(0,5):
    num=int(input("elemento:"))
    listaA.append(num)
    if num>=x:
        listaB.append(num)
print("lista a:", listaA)
print("lista b", listaB)
