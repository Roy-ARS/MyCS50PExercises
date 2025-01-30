from datetime import date
import re
import sys
import operator


def main():
    try:
        year, month, day = validateDateFormat(input("What is your date of birth? YYYY-MM-DD \n"))
        userDate = date(int(year), int(month), int(day))
    except ValueError:
        print("Invalid date")

    print(type(userDate))
    differenceMinutes = calculateDeltaMinutes(date.today(), userDate)

    print(differenceMinutes)



def validateDateFormat(inputDate): #validates that date is in YYYY-MM-DD format, returns date split in tupple
    if reG := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", inputDate):
        return reG.groups()
    else:
        sys.exit("Wrong date format")


def calculateDeltaMinutes(date1, date2):
    validateDateFormat(str(date1))
    validateDateFormat(str(date2))
    difference = operator.__sub__(date1, date2)
    return int(difference.days)*24*60
...


if __name__ == "__main__":
    main()
