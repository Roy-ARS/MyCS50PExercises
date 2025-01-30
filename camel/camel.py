def main():
    user_input = snakecasing(input("camelCase: "))

    print("snake_case: " + user_input)


def snakecasing(camel):
    for c in camel:
        if c.isupper():
            camel = camel.replace(c, "_" + c.lower())

    return camel




if __name__ == "__main__":
    main()