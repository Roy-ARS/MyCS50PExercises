import sys
from tabulate import tabulate

def main():
    menu = get_menu()
    split_menu = separate_csv(menu)
    menu.close()
    print(tabulate(split_menu, headers="firstrow", tablefmt="grid"))




def get_menu():
    arguments_count = len(sys.argv)
    if arguments_count < 2:
        sys.exit("Too few command-line arguments")
    elif arguments_count > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            try:
                file = open(sys.argv[1])
                return file
            except:
                sys.exit("File not found")
        else:
            sys.exit("Not a CSV file")


def separate_csv(menu):
    list = []
    try:
        for line in menu:
            name, small, large = line.rstrip().split(",")
            dict = {"name": name, "small": small, "large": large}
            list.append(dict)
    except ValueError:
        sys.exit("Not the right file")

    return list



if __name__ == "__main__":
    main()