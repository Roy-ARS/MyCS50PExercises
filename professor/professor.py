import random


def main():


    points = 0                #initialize points var
    lvl = get_level()         # get level from user range 1 2 3

    for i in range(10):      #generate 10 additions to be asked
        x = generate_integer(lvl)     #get x and y to be added
        y = generate_integer(lvl)
        correct_answ = x+y

        tries = 0
        while tries < 3:

            try:
                user_answ = int(input(f"{x} + {y} = "))    #ask addition
                if user_answ != correct_answ:
                    print("EEE")
                    tries += 1
                    continue
                else:
                    points += 1  #add points if answer is correct
                    tries = 4    # to not ask again
            except ValueError:
                print("EEE")
                tries += 1
                continue
        if tries == 3:                   #let user try answer 3 times, if wrong, show correct and ask next
            print(x, "+", y , "=", correct_answ)


    print("Score: ", points)  #when 10 additions were prompted, show final score


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:        #ask for a level, in digits for numbers
                return level
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()