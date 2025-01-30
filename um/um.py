import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    total = 0
    words = re.findall(r"[a-zA-Z]+", s.lower())
    for word in words:
        if word == "um":
            total += 1
    return int(total)

if __name__ == "__main__":
    main()
