def encode(txt_file):
    with open(txt_file, 'r') as f:
        text = f.read()

    converted = ""
    for ch in text:
        if ch == '.':
            converted += '0'
        elif ch == '-':
            converted += '1'
        elif ch == '/':
            converted += '/'
        else:
            converted += ch

    with open('encoded.txt', 'w') as f:
        f.write(converted)


def decode(txt_file):
    with open(txt_file, 'r') as f:
        text = f.read()

    converted = ""
    for ch in text:
        if ch == '0':
            converted += '.'
        elif ch == '1':
            converted += '-'
        elif ch == '/':
            converted += '/'
        else:
            converted += ch

    with open('decoded.txt', 'w') as f:
        f.write(converted)


while (1):
    f = int(input("encode(0)/decode(1):\n"))
    if f == 0:
        name = input("Input your txt filename(Must be putted into the same directory with the codefile,the filename "
                     "include the filename suffix):\n")
        encode(name)
    elif f == 1:
        name = input("Input your txt file name(Must be putted into the same directory with the codefile,the filename "
                     "include the filename suffix):\n")
        decode(name)
    else:
        print("Your input is not allowed,please try again")
