def main():

    amount_due = 50

    while amount_due > 0:
        print("Amount Due: " + str(amount_due))

        user_coin = int(input("Insert Coin: "))

        if user_coin == 25 or user_coin == 10 or user_coin == 5: #machine only accepts these coins
            amount_due = amount_due - user_coin

    print("Change Owed: " + str(abs(amount_due)))

if __name__ == "__main__":
    main()