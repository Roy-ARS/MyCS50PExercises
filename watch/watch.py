import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"^<iframe.+src=\"(?:https?://)?(?:www.)?youtube.com/embed/([0-9a-zA-Z]+).+</iframe>", s):
        return "https://youtu.be/" + url.group(1)
    else:
        return None

...


if __name__ == "__main__":
    main()
