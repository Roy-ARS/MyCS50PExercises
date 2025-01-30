def main():
    a = int(input("Define a: "))
    b = int(input("Define b: "))
    mcd, interactions = divide_euc(a, b, -1)
    print("MCD = " + str(mcd))
    desenredados = []
    ecus = []

    if input("quiere desenredar el algoritmo? y/n ") == "y":

        desenredados = desenredar(a, b, mcd, interactions, ecus)
        #print(desenredados)

    else:
        pass


def divide_euc(a, b, inter):
    q = a // b
    r = a % b
    print(f"{a}/{b} = {q}   r = {r}     {a} = {q}({b}) + {r}")
    if r == 0:
        if b == 1:
            print("Los números son coprimos.")
        return b, inter
    else:
        inter += 1
        return divide_euc(b, r, inter)

############ Desenredando el algoritmo de euclides
def desenredar(a, b, mcd, interactions, ecus):
    q = a // b
    r = a % b
    ecuaciones = ecus
    if r != 0:
        ecuaciones = ecuaciones.append(str(r) + " = " + str(a) + " - " + str(q) + " (" + str(b) + ")")
        print(str(r) + " = " + str(a) + " - " + str(q) + "(" + str(b) + ")")
        return desenredar(b, r, mcd, interactions, ecus)
    else:
        valores = ecuaciones[interactions].split()
        valores[5] = valores[5].replace("(", "").replace(")", "")
        print(f"{valores}")
        for i in range(0, interactions):
            valores[5] = ecuaciones[interactions-1]
            i += 1
        print(f"{valores}")
        #print(valores)
        pass#print(desenredar(b, r, mcd))
    #primera = str(r) + " = " + str(a) + " - " + str(q) + " (" + str(b) + ")"
    #segunda = str(b % r) + " = " + str(b) + " - " + str(b // r) + " (" + str(r) + ")"
    #print(primera)
    #print(segunda)




if __name__ == "__main__":
    main()