def main():
    mass = formulaEinstein(int(input("m: ")))
    print("E: " + str(mass))


def formulaEinstein(m):
    e = m*pow(300000000, 2)
    return e

main()