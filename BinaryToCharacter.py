# Name:   Cayden Lombard
# Date:    September 30, 2020
# Purpose: Translate binary to text messages

def main():
    # Get the binary to decode
    my_file = open("code.txt")
    my_string = my_file.read()

    # Print the length of the binary
    print(len(my_string))


    def findcode(code):
        if code == "0000":
            my_char = " "
        elif code == "0001":
            my_char = "a"
        elif code == "0010":
            my_char = "e"
        elif code == "0011":
            my_char = "n"
        elif code == "0100":
            my_char = "o"
        elif code == "0101":
            my_char = "r"
        elif code == "0110":
            my_char = "s"
        elif code == "0111":
            my_char = "t"
        elif code == "1000000":
            my_char = "b"
        elif code == "1000001":
            my_char = "c"
        elif code == "1000010":
            my_char = "d"
        elif code == "1000011":
            my_char = "f"
        elif code == "1000100":
            my_char = "g"
        elif code == "1000101":
            my_char = "h"
        elif code == "1000110":
            my_char = "i"
        elif code == "1000111":
            my_char = "j"
        elif code == "1001000":
            my_char = "k"
        elif code == "1001001":
            my_char = "l"
        elif code == "1001010":
            my_char = "m"
        elif code == "1001011":
            my_char = "p"
        elif code == "1001100":
            my_char = "q"
        elif code == "1001101":
            my_char = "u"
        elif code == "1001110":
            my_char = "v"
        elif code == "1001111":
            my_char = "w"
        elif code == "1010000":
            my_char = "x"
        elif code == "1010001":
            my_char = "y"
        elif code == "1010010":
            my_char = "z"
        elif code == "1010011":
            my_char = "A"
        elif code == "1010100":
            my_char = "B"
        elif code == "1010101":
            my_char = "C"
        elif code == "1010110":
            my_char = "D"
        elif code == "1010111":
            my_char = "E"
        elif code == "1011000":
            my_char = "F"
        elif code == "1011001":
            my_char = "G"
        elif code == "1011010":
            my_char = "H"
        elif code == "1011011":
            my_char = "I"
        elif code == "1011100":
            my_char = "J"
        elif code == "1011101":
            my_char = "K"
        elif code == "1011110":
            my_char = "L"
        elif code == "1011111":
            my_char = "M"
        elif code == "1100000":
            my_char = "N"
        elif code == "1100001":
            my_char = "O"
        elif code == "1100010":
            my_char = "P"
        elif code == "1100011":
            my_char = "Q"
        elif code == "1100100":
            my_char = "R"
        elif code == "1100101":
            my_char = "S"
        elif code == "1100110":
            my_char = "T"
        elif code == "1100111":
            my_char = "U"
        elif code == "1101000":
            my_char = "V"
        elif code == "1101001":
            my_char = "W"
        elif code == "1101010":
            my_char = "X"
        elif code == "1101011":
            my_char = "Y"
        elif code == "1101100":
            my_char = "Z"
        elif code == "1101101":
            my_char = "."
        elif code == "1101110":
            my_char = ","
        elif code == "1101111":
            my_char = '"'
        elif code == "1110000":
            my_char = "\n"
        elif code == "1110001":
            my_char = "-"
        elif code == "1110010":
            my_char = "!"
        elif code == "1110011":
            my_char = "'"
        elif code == "1110100":
            my_char = "sh"
        elif code == "1110101":
            my_char = "th"
        elif code == "1110110":
            my_char = "oo"
        elif code == "1110111":
            my_char = "the"
        elif code == "1111000":
            my_char = "it"
        elif code == "1111001":
            my_char = "ing"
        return my_char;



    # Loop through the binary and print out the text
    my_ans = "";
    i = 0
    while i<len(my_string):
        if my_string[i] == "0":
            val = findcode(my_string[i:i+4])
            my_ans= my_ans+val
            print(i, " ", my_string[i:i+4], " ", val)
            i += 4
        else:
            val = findcode(my_string[i:i + 7])
            my_ans = my_ans + val
            print(i, " ", my_string[i:i + 7], " ", val)
            i += 7

    # Print the string of text
    print(my_ans)
main()
###########################################################################