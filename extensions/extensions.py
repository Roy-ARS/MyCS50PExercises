def main():
    userFile = input("File name: ").strip().lower().rsplit(".", 1)
    extensions = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

    #print(userFile)
    #print(userFile[-1])

    if userFile[-1] in extensions:
        for _ in extensions:
            if _ == userFile[-1]:
                print(compare(userFile[-1]))
                break
    else:
        print("application/octet-stream")

def compare(ext):
    if ext == "jpg" or ext == "jpeg":
        type = "image/jpeg"
    elif ext == "gif" or ext == "png":
        type = "image/" + ext
    elif ext == "pdf" or ext == "zip":
        type = "application/" + ext
    elif ext == "txt":
        type = "text/plain"

    return type


main()


