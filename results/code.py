txtdata = open("1.txt", "r")
# print(txtdata)
for line in txtdata:
    splitarray=line.split("]")
    print(splitarray)
    break
    
