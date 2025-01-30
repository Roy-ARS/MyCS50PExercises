import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #inputs 9:00 AM to 5:00 PM      9 AM to 5 PM    9:00 AM to 5 PM    9 AM to 5:00 PM
    #output 09:00 to 17:00
    hour24List = []
    try:
        hour1, hour2 = s.split(" to ") #split the two times
        hourList = [hour1, hour2]
        i = 0
        for h in hourList:
            match = re.search(r"((?:^[0-9])|(?:^0[0-9])|(?:1[0-2])):?([0-5][0-9])? (A|P){1}M{1}$", h) #search correct format and group info
            hour = int(match.group(1))
            if (match.group(3) == "P"):
                hour += 12
            if match.group(1) == "12": #12 PM must be 12, and 12 AM must be 00
                hour -= 12
            if match.group(2):
                minutes = match.group(2)
            else:
                minutes = "00"
            hour24List.append(str(f"{hour:02d}") + ":" + minutes)
            i += 1
    except:
        raise ValueError

    return hour24List[0] + " to " + hour24List[1]


if __name__ == "__main__":
    main()
