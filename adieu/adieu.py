import inflect
p = inflect.engine()

def main():
#prompt user for names
    names = []
    try:
        while True:
            name = input("Name :")
            names.append(name)
    except EOFError:
    #call function to print the results
        print()
        print(adieu(names))

#iterate through the list of names separating them with a comma, then add 'and' before the last one
def adieu(names_list):
    final_sent = "Adieu, adieu, to "
    list_len = len(names_list)
    joined_list = p.join(names_list)
    return final_sent + joined_list
    '''
    if list_len == 1:
        return final_sent+names_list[0]

    else:
        for name in names_list[:-1]:
            if list_len == 2:
                final_sent = final_sent+name+" "

            else:
                final_sent = final_sent+name+", "

        final_sent = final_sent+"and "+names_list[-1]
        return final_sent
'''

if __name__ == "__main__":
    main()


