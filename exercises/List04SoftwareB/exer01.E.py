lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2=[]
m=lista[0:16:2]+lista[0:16:3]+lista[0:16:4]
lista2.extend(m)
print("multiplos de 2, 3 e 4:",list(set(lista2)))


