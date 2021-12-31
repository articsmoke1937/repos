temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 + 32
        return f

with open("tempfile.txt", "w") as tempfile:
    for t in temperatures:
        f = (c_to_f(t))
        tempfile.write(str(f) + "\n")
