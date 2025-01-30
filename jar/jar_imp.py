from jar import Jar

def main():
    jar = Jar()

    while True:
        opcion = input("1. deposit  2. withdraw  3. check")

        match opcion:
            case "1":
                try:
                    jar.deposit(int(input("Deposit cookies: ")))
                except ValueError as exc:
                    print(str(exc))
                print(jar)

            case "2":
                try:
                    jar.withdraw(int(input("Take cookies: ")))
                except ValueError as exc:
                    print(str(exc))
                print(jar)

            case "3":
                print(f"Capacity: {jar.capacity}, Size: {jar.size}")
                print(jar)
                break



if __name__ == "__main__":
    main()

