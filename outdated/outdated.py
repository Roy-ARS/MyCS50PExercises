def main():

    #MM/DD/YYYY || month D, YYYY  to YYYY/MM/DD

    print(get_ISO_date())



def get_ISO_date():
    months = {
    "January" : "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }

    while True:
        user_date = input("Date: ").strip()

        try:
            for c in user_date:
                if not c.isalnum():
                    user_date_list = user_date.title().split(c) #catch user date and split it
                                                                #by month, day, year into a list
                    if user_date_list[0].isalpha():
                        if "," in user_date_list[1]:                #if letters, convert to month number
                            month = int(months[user_date_list[0]])  #and check for comma format
                        else:
                            break
                    else:
                        month = int(user_date_list[0])
                    day   = int(user_date_list[1].replace(",", "")) #independent int var for each item
                    year  = int(user_date_list[2])
                    break

            if 1 <= day <= 31 and 1 <= month <= 12:  #return only if meets all conditions
                return "{2}-{0}-{1}".format( f"{month:02}",
                                            f"{day:02}",
                                            f"{year:04}")
            else:
                pass

        except:
            pass






if __name__ == "__main__":
    main()
