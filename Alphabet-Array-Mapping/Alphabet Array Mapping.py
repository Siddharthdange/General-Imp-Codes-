def My_Mapping():
    input1 = input(' ')
    input1 = input1.lower()
    output = []
    for character in input1:
        number = ord(character) - 96
        output.append(number)
    print(output)


My_Mapping()