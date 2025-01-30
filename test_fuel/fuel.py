def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])
            f = x/y
            if f <= 1:
                return round(f*100)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            #fraction = input("Fraction: ")
            raise



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"



if __name__ == "__main__":
    main()
