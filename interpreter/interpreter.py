def main():
    x, y, z = input("Expression: ").split()

    print(math(x, y, z))


def math(x, y, z):
    if y == "/":
        result = int(x)/int(z)
    elif y == "*":
        result = int(x)*int(z)
    elif y == "+":
        result = int(x)+int(z)
    else:
        result = int(x)-int(z)
    return "{0:.1f}".format(result)







main()