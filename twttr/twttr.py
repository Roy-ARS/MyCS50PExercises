def main():
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    user_input = input("Input: ")
    for c in user_input:
        if c not in vowels:
            print(c, end="")
    print()

if __name__ == "__main__":
    main()