def disarium(num):
    numb = str(num)
    length = len(numb)
    result = rem = 0
    while num>0:
        rem  = num % 10
        result = result + (rem ** length)
        length = length -1 
        num = num // 10
    return result


def ceaser_cipher(pltxt, shftkey):
    for i in pltxt:
        if i.isupper():
            n = (ord(i) + shftkey) % 91
            if n < 65:
                n = n + 65
            print(chr(n), end="")
        else:
            n = (ord(i) + shftkey) % 123
            if n < 97:
                n = n + 97
            print(chr(n), end="")

c = int(input("Enter choice"))
if c == 1:
    x = int(input("Enter the limit"))
    for i in range(1,x):
        if i == disarium(i):
            print(i)
else:
    plaintext = input("Enter plaintext")
    shift = int(input("Enter the shift key"))
    ceaser_cipher(plaintext, shift)