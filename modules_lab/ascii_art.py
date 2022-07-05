from pyfiglet import figlet_format


def print_art(msg):
    ascii_art = figlet_format(msg,  font="isometric1")
    print(ascii_art)


print_art(input("Enter your text: \n"))
