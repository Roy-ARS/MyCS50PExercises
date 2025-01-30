import random

def main():

    value = get_range()
    user_guess = get_userNum(value)

    print(user_guess)

def get_range():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                rand_num = random.randint(1, level)
                return rand_num
        except ValueError:
            continue

def get_userNum(rand_num):
    while True:
        try:
            user_input = int(input("Guess: "))
            if user_input > 0:
                if user_input > rand_num:
                    print("Too large!")
                elif user_input < rand_num:
                    print("Too small!")
                else:
                    return "Just right!"
        except ValueError:
            continue








if __name__ == "__main__":
    main()