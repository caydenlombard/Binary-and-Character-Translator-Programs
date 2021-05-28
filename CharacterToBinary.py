# Name:   Cayden Lombard
# Date:    September 27, 2020
# Purpose: Translate text messages to binary

def main():
    # Get the message to encode
    my_file = open("text.txt")
    my_string = my_file.read()

    # Print the length of the message
    print(len(my_string))


    def findcode(my_char):
        if my_char == " ":
            code = "0000"
        elif my_char == "a":
            code = "0001"
        elif my_char == "e":
            code = "0010"
        elif my_char == "n":
            code = "0011"
        elif my_char == "o":
            code = "0100"
        elif my_char == "r":
            code = "0101"
        elif my_char == "s":
            code = "0110"
        elif my_char == "t":
            code = "0111"
        elif my_char == "b":
            code = "1000000"
        elif my_char == "c":
            code = "1000001"
        elif my_char == "d":
            code = "1000010"
        elif my_char == "f":
            code = "1000011"
        elif my_char == "g":
            code = "1000100"
        elif my_char == "h":
            code = "1000101"
        elif my_char == "i":
            code = "1000110"
        elif my_char == "j":
            code = "1000111"
        elif my_char == "k":
            code = "1001000"
        elif my_char == "l":
            code = "1001001"
        elif my_char == "m":
            code = "1001010"
        elif my_char == "p":
            code = "1001011"
        elif my_char == "q":
            code = "1001100"
        elif my_char == "u":
            code = "1001101"
        elif my_char == "v":
            code = "1001110"
        elif my_char == "w":
            code = "1001111"
        elif my_char == "x":
            code = "1010000"
        elif my_char == "y":
            code = "1010001"
        elif my_char == "z":
            code = "1010010"
        elif my_char == "A":
            code = "1010011"
        elif my_char == "B":
            code = "1010100"
        elif my_char == "C":
            code = "1010101"
        elif my_char == "D":
            code = "1010110"
        elif my_char == "E":
            code = "1010111"
        elif my_char == "F":
            code = "1011000"
        elif my_char == "G":
            code = "1011001"
        elif my_char == "H":
            code = "1011010"
        elif my_char == "I":
            code = "1011011"
        elif my_char == "J":
            code = "1011100"
        elif my_char == "K":
            code = "1011101"
        elif my_char == "L":
            code = "1011110"
        elif my_char == "M":
            code = "1011111"
        elif my_char == "N":
            code = "1100000"
        elif my_char == "O":
            code = "1100001"
        elif my_char == "P":
            code = "1100010"
        elif my_char == "Q":
            code = "1100011"
        elif my_char == "R":
            code = "1100100"
        elif my_char == "S":
            code = "1100101"
        elif my_char == "T":
            code = "1100110"
        elif my_char == "U":
            code = "1100111"
        elif my_char == "V":
            code = "1101000"
        elif my_char == "W":
            code = "1101001"
        elif my_char == "X":
            code = "1101010"
        elif my_char == "Y":
            code = "1101011"
        elif my_char == "Z":
            code = "1101100"
        elif my_char == ".":
            code = "1101101"
        elif my_char == ",":
            code = "1101110"
        elif my_char == '"':
            code = "1101111"
        elif my_char == "\n":
            code = "1110000"
        elif my_char == "-":
            code = "1110001"
        elif my_char == "!":
            code = "1110010"
        elif my_char == "'":
            code = "1110011"
        elif my_char == "sh":
            code = "1110100"
        elif my_char == "th":
            code = "1110101"
        elif my_char == "oo":
            code = "1110110"
        elif my_char == "the":
            code = "1110111"
        elif my_char == "it":
            code = "1111000"
        elif my_char == "ing":
            code = "1111001"
        return code;

    # Loop through the message and print out the binary values
    for i in range(len(my_string)):
        val = findcode(my_string[i])
        print(i, " ", my_string[i], " ", val)

    # Get the Binary to be one long string
    my_ans = "";
    for i in range(len(my_string)):
        val = findcode(my_string[i])
        my_ans= my_ans+val

    # Print the long string of binary
    print()
    print(my_ans)
main()
###########################################################################