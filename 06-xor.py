string = "label"
number = 13

def string_to_ascii(string):
    chars = ''
    for a in string:
        # print(a)
        chars += str(ord(a))
    return chars

## ---> string to unicode (ascii)
a = string_to_ascii(string)
# print(a)

## ---> decimal number to binary
b = bin(number)
# print(b)

## ---> xor each character with b
msg = ''
for a in string:
    ch = ord(a)
    # print(a, " => ", ch, sep='')

    ## in this case, we are xoring 13 and numbers between 90
    ## and 110; since 13 is relatively little, it automatically
    ## adds zeros to the left to match the size
    print(number, " ^ ", ch, sep='')
    xored = ch ^ 13
    print("\t", xored)
    msg += chr(xored)

print(msg)
