def main():
    # ask for greeting
    greeting = input("Greeting: ")
    print("$" + str(value(greeting)))


def value(g):
    g_low = g.lower().strip()
    if "hello" in g_low:
        return 0
    elif "h" in g_low[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()