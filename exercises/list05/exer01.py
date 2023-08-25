lista=[]
for n in range(0,5):
    val1=float(input("Insira um valor:"))
    val2=float(input("Insira outro valor:"))
    lista=val1,val2
    if val1==val2:
        print("Ambos são mesmos valores.")
    elif val1>val2:
        print("Maior valor:{}, Menor elemento:{}.".format(val1,val2))
    else:
        print("Maior valor:{}, Menor elemento:{}.".format(val2,val1))
    print("\n")


