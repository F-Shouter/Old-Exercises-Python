x=0
lista1=[1,98,30,5,4,2563256,3,0,1542,2]
for n in lista1:
    print("numero:",n)
    print("posição:",lista1.index(n))
    print("acrescimo:",n+1 )
    print("\n")
    x=x+1
soma=sum(lista1)
print("soma de todos os elementos:",soma)
elem=len(lista1)
print("número de elementos:",elem)
media=soma/x 
print("média:",media)
print("x:",x)


    