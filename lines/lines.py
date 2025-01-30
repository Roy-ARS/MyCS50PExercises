import sys

def main():
    arguments_count = len(sys.argv)
    if arguments_count < 2:
        sys.exit("Too few command-line arguments")
    elif arguments_count > 2:
        sys.exit("Too many command-line arguments")
    else:

        if sys.argv[1].endswith(".py"):
            try:
                file = open(sys.argv[1])
                count = 0
                for line in file:
                    if line.lstrip().startswith("#") or line.isspace():
                        pass
                    else:
                        count += 1
                print(count)
                file.close()
            except:
                sys.exit("File not found")
        else:
            sys.exit("Not a python file")





if __name__ == "__main__":
    main()
