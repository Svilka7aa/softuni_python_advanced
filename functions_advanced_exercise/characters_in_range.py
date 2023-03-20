def char(char1, char2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=" ")


ch1 = input()
ch2 = input()
char(ch1, ch2)
