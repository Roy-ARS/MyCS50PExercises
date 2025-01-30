def main ():
    #ask the question
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    for c in [" ", "-"]:
        answer = answer.replace(c, "")
        
    print(getResponse(answer))

def getResponse(a):
    if a in ["42", "fortytwo"]:
        return "Yes"
    else:
        return "No"

main()