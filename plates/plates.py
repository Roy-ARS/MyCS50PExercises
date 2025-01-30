def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 2 <= len(s) <= 6 and s.isalnum(): #first check if lenght is right size and if it has no special chars

        if s[0:2].isalpha():  #check if starts with 2 letters
            if len(s) > 2:
                for c in s:
                    if c.isdecimal():
                        if int(c) != 0:       # check if first number found is zero
                            break
                        else:
                            return False

                count = 0
                for i in s:
                    if i.isdecimal():  #counting total numbers in plate
                        count += 1

                j = 1
                while j <= count:
                    if s[-j].isalpha(): #verify if all numbers found are at the end
                        return False
                    j += 1
        else:
            return False

    else:
        return False

    return True #if everything tested true


main()
