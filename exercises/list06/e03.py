
lista=[]
num=int(input("numero:"))
lista.append(num)
while num!=0:
   num=int(input("numero:")) 
   lista.append(num)
lista.remove(0)
print(lista)
soma=sum(lista)
print("soma dos num:",soma)
media=soma/ (len(lista))
print("media",media) 