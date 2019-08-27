#You are given a string s and width w. 
#Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    splittedstring = [string[i:i+max_width] for i in range(0,len(string),max_width)]
    returnstring = ""
    for st in splittedstring:
        returnstring += st
        returnstring += '\n' 
    return returnstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)