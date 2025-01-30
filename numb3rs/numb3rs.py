import re


def main():
    print()
    print(validate(input("IPv4 Address: ")))
    print()

def validate(ip):
    ipExpresion = "(^[0-9]$)|(^[1-9][0-9]$)|(^2[0-4][0-9]$)|(^25[0-5]$)|(^1[0-9][0-9]$)"

    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$", ip): #search #.#.#.# format
        numberList = ip.split(".")
        for _ in numberList:
            if re.search(ipExpresion, _) == None: #search if each number is 0-255
                return False
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
