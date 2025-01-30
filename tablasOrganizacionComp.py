def main ():

    while True:
        variables = "ABCD"
        expresionFinal = ""
        negaciones = []
        num = input("numero binario: ")
        if "0" not in num and "1" not in num:
            break

        for c in num:
            if c == "0":
                negaciones.append("N")
            else:
                negaciones.append("S")
        i = 0
        while i < len(negaciones):
            if negaciones[i] == 'N':
                expresionFinal = expresionFinal + variables[i].join({"", "'"})
            else:
                expresionFinal = expresionFinal + "".join(variables[i])
            i += 1
        print("\n",negaciones)
        print("Numero: " + num)
        print("Variables: " + expresionFinal,"\n")







if __name__ == "__main__":
    main()
