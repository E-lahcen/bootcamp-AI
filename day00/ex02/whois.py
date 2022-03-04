import sys

num = ''.join(sys.argv[-1:2])
if num.isdigit() and (len(sys.argv) == 2):
    if (int(num) == 0):
        print("I am zero")
    elif (not(int(num) % 2)):
        print("I am Even")
    elif (int(num) % 2):
        print("I am Odd")
elif len(sys.argv) == 1:
    sys.exit()
assert len(sys.argv) == 2, "More than one argument is provided."

assert num.isdigit(), "argument is not integer."
