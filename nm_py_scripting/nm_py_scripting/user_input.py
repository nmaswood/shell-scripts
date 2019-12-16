import sys

YES = {'yes', 'y', 'true'}


def is_yes(message):
    should_delete = input(message).lower()
    return should_delete in YES


def read_std_in_as_stripped_lines():
    return [line.strip() for line in sys.stdin.readlines()]
