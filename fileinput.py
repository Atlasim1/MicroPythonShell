print("File Input / Receive Program")
filename = input("File Name >")

file = open(filename, "a")
while True:
    contents = input("CONTENTS (\"***!!!EXITTYPE!!!***\" To exit)> ")
    if contents == "***!!!EXITTYPE!!!***":
        file.close()
        break
    else:
        file.write(f"{contents}\n")

