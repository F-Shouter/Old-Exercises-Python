x=0
lista1=[]
lista2=[]
num=int(input("numero:"))
if num>=80:
   lista1.append(num)
if num<=10:
    lista2.append(num)
while num!=100:
    if num>=80:
        lista1.append(num)
    if num<=10:
         lista2.append(num)
    x=x+1
    num=int(input("numero:"))

print("acima de 80:",lista1)
print("abaixo de 10:",lista2)
print("x:",x)