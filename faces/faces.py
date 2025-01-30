def main():
    myStr = convert(input("Type something: "))
    print(myStr)

#converts emoticon into emoji
def convert(changeThis):
    changeThis = changeThis.replace(":)", "🙂")
    changeThis = changeThis.replace(":(" , "🙁")
    return changeThis

main()
