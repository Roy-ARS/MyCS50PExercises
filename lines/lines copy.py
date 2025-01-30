import sys
import urllib.request

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            url = "https://cdn.cs50.net/python/2022/x/lectures/6/src6/"+sys.argv[1]
            try:
                file = urllib.request.urlopen(url)
                count = 0
                for line in file:
                    if line.startswith(b"#") or line.isspace():
                        pass
                    else:
                        count += 1
                print(count)
            except:
                raise
                sys.exit(f"File {url} not found")
        else:
            sys.exit("Not a python file")





if __name__ == "__main__":
    main()
