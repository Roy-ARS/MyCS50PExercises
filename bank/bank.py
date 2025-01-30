def main():
    # ask for greeting
    greeting = input("Greeting: ").lower().strip()
    print(giveMoneyFor(greeting))


def giveMoneyFor(g):
    if "hello" in g:
        return "$0"
    elif "h" in g[0]:
        return "$20"
    else:
        return "$100"

main()