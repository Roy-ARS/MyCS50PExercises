#CONVERTS GIVEN NUMBER INTO BINARY
def main():
    #ask user for the number
    num = int(input("Number: "))
    count = 0
    binary_num = []
    final_binary = toBinary(num, count, binary_num)
    i = 1
    while i <= len(final_binary):
        print(final_binary[-i], end="")

        i += 1
    print()




def toBinary(num, count, list):
    #take number and divide without residual
    result = num // 2
    r = num % 2
    list.append(r)
    #save residual into a variable
    print(f"{num} / {2} = {result}  r = {r}")
    count += 1
    if num != 0:
        return toBinary(result, count, list)
    #return the concatenated residuals
    else:
        return list


if __name__ == "__main__":
    main()
