import emoji

def main():
    text = input("Input: ").lower()
    print("Output: ", emoji.emojize(text, language="alias"))





if __name__ == "__main__":
    main()
