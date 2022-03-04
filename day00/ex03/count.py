import sys
import string

def text_analyzer(*text):
    """Counts the number of upper, lower, punctuation and space characters."""
    uper = 0
    lower = 0
    ponc = 0
    space = 0
    if len(text) == 0:
        print("What is the text to analyse?")
        print(">> ", end='')
        sys.stdout.flush()
        inp = sys.stdin.readline()
    elif len(text) > 1:
        print("Error", len(sys.argv))
        exit()
    if len(text) == 1:
        inp = text[0]
    for i in range(len(inp)):
        if inp[i].islower():
            lower += 1
        elif inp[i].isupper():
            uper += 1
        elif inp[i] in string.punctuation:
            ponc += 1
        elif inp[i] == ' ':
            space += 1

    print("The text contains",len(inp),"charachters.")
    print("- {} upper letters".format(uper))
    print("- {} lower letters".format(lower))
    print("- {} punctuation marks".format(ponc))
    print("- {} spaces".format(space))