def swap_case(s):
    newstring = ''
    for i in s:
        if i.isupper()==True:
            newstring+=i.lower()
        elif i.islower()==True:
            newstring+=i.upper()
        else:
            newstring+=i
    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)