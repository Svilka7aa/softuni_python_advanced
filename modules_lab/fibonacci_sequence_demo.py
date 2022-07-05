import sys
from io import StringIO

from read_until import read_until_command
from fibonacci_sequence import create_sequence, locate


def parse_command(command):
    parts = command.split(" ")
    if parts[0] == "Create":
        return ("Create", int(parts[2]))
    else:
        return ("Locate", int(parts[1]))


# test_input = """Create Sequence 10
# Locate 13
# Create Sequence 3
# Locate 10
# Stop
# """
#
#
# sys.stdin = StringIO(test_input)

commands = read_until_command("Stop", map_func=parse_command)

for (command, value) in commands:
    result = None
    if command == "Create":
        result = ' '.join([str(x) for x in create_sequence(value)])

    elif command == "Locate":
        number, index = locate(value)

        if index is None:
            print(f"The number {number} is not in the sequence")
            continue
        else:
            print(f"The number - {number} is at index {index}")
            continue
    print(result)
