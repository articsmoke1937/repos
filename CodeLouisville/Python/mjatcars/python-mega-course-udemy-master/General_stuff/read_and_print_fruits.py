
fruitfile = open("fruits.txt")
fruits = fruitfile.read()
print(fruits)
fruitlist = fruits.splitlines()
print(fruitlist)
for i in fruitlist:
	print(len(i))
