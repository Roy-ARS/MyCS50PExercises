def main():

    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    final_word = ""
    for c in word:
        if c not in vowels:
            final_word = final_word+c
    return final_word

if __name__ == "__main__":
    main()