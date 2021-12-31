with open("file1.txt") as file1:
    contents1=file1.read()

with open("file2.txt","a+") as file2:
    file2.write(contents1)
    file2.seek(0)
    contents2=file2.read()
print(contents2)



'''
newd={"a":1,"b":2,"c":3}

a_dictionary = {"a": 1, "b": 2}
for k, v in a_dictionary.items():
    print(k,v)

a_list=[1,2,3,4]
for a in a_list:
    print(a)

a_tuple=[1,2,3,4]
for a in a_tuple:
    print(a)

print(a_tuple[1])
print(isinstance(('s',[1,2,3]),tuple))

print("hey {} why don't you call {}?".format("Maurice","Larry"))
'''

'''
keys_list = list(a_dictionary)
print(keys_list)
print(type(keys_list
))
a_key = keys_list[0]

print(a_key)
'''
'''
with open("data.txt", "a+") as file:
    #file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
'''

'''
with open("bear.txt","a+") as file_object:
    file_object.seek(0)
    line = file_object.read()
    file_object.seek(0)
    file_object.write("\n" + line)
    file_object.write("\n" + line)
'''
'''
def foo(v_char,filename):
    with open(filename) as file_object:
        line = file_object.read()
    return line.count(v_char)

print(foo("m","fruits.txt"))
'''
'''
filename = 'fruits.txt'
with open(filename) as file_object:
    line = file_object.read() # returns list of 'value\n'
print(line[:6])

filename = 'first.txt'
with open(filename,"a") as file_object:
    file_object.write( "\n" + line[:6])
'''
'''
filename = 'siddhartha.txt'
fruits=["apples","oranges","pears"]
with open(filename,"a") as file_object:
    for fruit in fruits:
        file_object.write( "\n" + fruit)
'''

'''
filename = 'fruits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() # returns list of 'value\n'
    #lines = file_object.read() # returns one long string with embedded '\n' between values
for line in lines:
 print(line)
'''
'''
def foo(*arg):
    a = [i.upper() for i in arg ]
    return sorted(a)
print(foo("z","a","k","A"))
'''
'''
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
'''
'''
def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(a=1,b=2))
'''
'''
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
'''
'''
def foo(*args):
    return args

print(type(foo(1,2,3,4)))    
'''
'''
def foo(listin):
    return [i if not isinstance(i,str) else 0 for i in listin ]

print (foo([-1,1,2,'g',0,-11111]))
'''
'''
def foo(listin):
    return [i for i in listin if i>0]

print (foo([-1,1,2,3,0,-11111]))
'''
'''
def foo(mixed_list):
    num_list = [num for num in mixed_list if not isinstance(num,str)]
    return num_list

print(foo(["sfsd",1,"wrwer",2]))
'''
'''
def sentence_maker(phrase):
    interrogatives = ('Who','What','Where','Why','When','How','Are')
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:    
        return '{}.'.format(capitalized)

sentence_in = []
while True:
    phrase_in = input("Say something: ")
    if phrase_in == "\end":
        break
    else:
        sentence_in.append(sentence_maker(phrase_in))        

print(" ".join(sentence_in))
'''
'''
def get_text():
    while True:
        msg = input("Say something: ")
        if msg == "\end":
            break
        else:
            full_msg.append(msg)
            print(full_msg)
full_msg = []

    for i in full_msg:
        print(i.capitalize(), end='')
        if i.startswith(("who","what","where","why","how","when")):
            print("? ", end='')
        else:
            print(". ", end='')

get_text()
'''
'''
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.value():
    print(key, value)
'''
'''
while True:
    text = input("Type anything!!! ")
    if text == "stop":
        break
'''
'''
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(key + ": " + value)
'''
'''
# Store people's favorite languages.
fav_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
# Show each person's favorite language.
for name, language in fav_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
'''
'''
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
'''   
'''
def foo4(name):
    capname = name.title()
    print(f"Hi {capname}")

foo4("maurice johnson")
'''
'''
def foo():
    name = input("What is your name? ")
    message = f"Hi {name}"
    print(message)

foo()
'''
'''
def foo(temp):
    if temp > 25:
        return "Hot"
    elif temp >= 15 and temp <= 25:
        return "Warm"
    else:
        return "Cold"

print(foo(1))       
print(foo(15))       
print(foo(22))       
print(foo(111))       
'''
'''
def foo(string):
    if len(string) > 7:
        return True
    else:
        return False

print(foo("afsfd"))       
print(foo('ewrwerwjelwjrwerwel')) 
'''

'''
def oz2ml(oz):
    return oz * 29.57353

print(oz2ml(10))   
'''
'''
def foo(l):
    a = l*l
    return a
print(foo(12)) 
'''   
'''
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1,2,3,4,5,6,7,8,9,10]))
'''
'''
mymax = max(student_grades.values())
print("Higrest_Grade: ",mymax)
mysum = sum(student_grades.values())
length = len(student_grades.values())
mean = mysum / length
print(mean)
'''

'''
student_grades = [9.1,7.4,8.5]
student_grades.reverse()
print(student_grades)
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)
'''

"""import datetime
mynow = datetime.datetime.now()
print(mynow)"""