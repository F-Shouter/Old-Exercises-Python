lista=[]
for n in range(0,4):
    nota=float(input("Insira a nota:"))
    lista.append(nota)
print("Notas",lista)
print("Media das notas:",sum(lista)/4)
