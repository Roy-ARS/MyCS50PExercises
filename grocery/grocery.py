def main():
    grocery_list = {}

    try:
        while True:
            item = input()
            if item in grocery_list:      #if exists, count one more
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1    # add it if does not exist

    except EOFError:
        for item in sorted(grocery_list):
            print(grocery_list[item], item.upper())



if __name__ == "__main__":
    main()