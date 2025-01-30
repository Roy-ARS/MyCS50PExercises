import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("not enough arguments")
    else:
        try:
            n_bitcoins = float(sys.argv[1])
        except:
            sys.exit("Argument is not a number")



    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()

    json_object = response.json()
    price = json_object["bpi"]["USD"]["rate_float"]

    print(f"${price*n_bitcoins:,.4f}")
    print("${:,.4f}".format(price*n_bitcoins))


if __name__ == "__main__":
    main()
