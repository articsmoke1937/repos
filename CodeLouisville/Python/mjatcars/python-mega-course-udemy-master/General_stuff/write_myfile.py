numbers = [1, 2, 3]
myfile = open("numfile.txt","w")
for i in numbers:
    myfile.write("\n"+str(i))
myfile.close()
