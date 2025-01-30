def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    if percentage != None:
        print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])
            percentage = (x/y)*100
            if x <= y:
                return percentage
        except (ValueError, ZeroDivisionError, IndexError):
            pass


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(round(percentage)) + "%"



if __name__ == "__main__":
    main()