temperatures = [10, -20, -289, 100]
def c_to_f(c):
    f = c* 9/5 + 32
    return str(f)

with open("tempfile.txt","w") as temp:
    for t in temperatures:
        if t >= -273.15:
            print(c_to_f(t))
            temp.write(str(c_to_f(t)) + "\n")
