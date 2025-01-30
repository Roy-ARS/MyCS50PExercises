def main():
    userTime = float("{0:.2f}".format(convert(input("What time is it? "))))
    #print(userTime)

    if 7.00 <= userTime <= 8.00:
        print("breakfast time")
    elif 12.00 <= userTime <= 13.00:
        print("lunch time")
    elif 18.00 <= userTime <= 19.00:
        print("dinner time")


def convert(time):
    moment = ""
    if " " in time:
        time, moment = time.split(" ")

    hours, minutes = time.split(":")

    if moment == "p.m.":
        hours = int(hours)+12
    #print(hours, minutes)
    minutesDecimal = "{0:.0f}".format(int(minutes)*100/60)

    if len(minutesDecimal) == 1:
        minutesDecimal = "0" + minutesDecimal

    floatTime = str(hours) + "." + minutesDecimal
    #print(minutesDecimal)
    return float(floatTime)


if __name__ == "__main__":
    main()