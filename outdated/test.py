months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


old_month = input("Month: ").title()

if old_month in months:
    month = months.index(old_month) + 1
    print(f"{old_month} is the {month}th month of the year")

else:
    print("CABALLOOOO")


