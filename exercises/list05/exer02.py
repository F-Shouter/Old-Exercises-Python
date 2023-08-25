lista=[]
for n in range(0,20):
    A=float(input("Insira o valor de A:"))
    B=float(input("Insira o valor de B:"))
    C=float(input("Insira o valor de C:"))
    if (A>B) and (A>C):
        print("A é o maior elemento, sendo:",A)
    elif (A==B) and (A>C):
        print("A")
    elif (B>A) and (B>C):
        print("B é o maior elemento, sendo:",B)
    elif (C>A) and (C>B):
        print("C é o maior elemento, sendo:",C)
    elif (A==B):
        print("B")
    print("\n")
   