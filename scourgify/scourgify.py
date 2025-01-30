import sys
import csv

def main():
#check if there are 2 extra argv, input file exists and is CSV
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    name_house_list = split_dict(file)
            except:
                sys.exit("File not found")
        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("Provide exactly 2 CSV file names in command-line arguments")
#-----------------------------------------------------


    write_csv(name_house_list)

#read the file and store the dictionary splitting names, last names and houses
def split_dict(f):
    name_house_list = []
    reader = csv.DictReader(f) #reader creates list of lists, Dict reader creates list of dicts
    for row in reader:
        last_name, first_name = row["name"].split(",")
        name_house_list.append({"first_name": first_name.strip(),
                                "last_name": last_name.strip(),
                                "house": row["house"]})

    return name_house_list

#------------------------------------


#write the new file given in argv with the new data order
def write_csv(dict):
    with open(sys.argv[2], 'w') as output:
        writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for entry in dict:
            writer.writerow({'first': entry["first_name"],
                             'last': entry["last_name"],
                             'house': entry["house"]})



if __name__ == "__main__":
    main()