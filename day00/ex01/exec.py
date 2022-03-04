import sys

def reverse(x):
    return x[::-1]
    
print(reverse(' '.join(sys.argv[1:])).swapcase())