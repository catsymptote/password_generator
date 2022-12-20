import os
import pyperclip
from random import SystemRandom
import sys


class PasswordGenerator:
    def __init__(self):
        # Read files
        file_path = os.path.realpath(__file__)
        with open(os.path.join(os.path.dirname(file_path), 'assets', 'adjectives.txt')) as f:
            adjective_text = f.read()

        with open(os.path.join(os.path.dirname(file_path), 'assets', 'nouns.txt')) as f:
            noun_text = f.read()

        # Make lists
        self.adjectives = list(set([adjective for adjective in adjective_text.split('\n')]))
        self.nouns = list(set([noun for noun in noun_text.split('\n')]))

        self.rand = SystemRandom()

    def get_random(self, words: list) -> str:
        random_number = self.rand.random()
        section_size = 1 / len(words)
        random_int = int(random_number // section_size)
        return words[random_int]

    def get_random_pair(self):
        adjective = self.get_random(self.adjectives)
        noun = self.get_random(self.nouns)
        return (adjective, noun)

    def generate(self, pairs=3):
        password = ''
        for i in range(pairs):
            adjective, noun = self.get_random_pair()
            password += f'{adjective.title()} {noun.title()} '
        return password[:-1]


def main():
    help_message = '''Run the script with an integer (number of word pairs) and option arguments.
The following option arguments are accepted:
    -h : Print help message
    -p : Disables printing
    -c : Disables copying to clipboard'''

    PRINT_ACTIVE = True
    COPY_ACTIVE = True

    arguments = []
    for argument in sys.argv[1:]:
        arguments += argument.split()

    pairs = 1
    if len(arguments) == 0:
        pairs = 1
    else:
        for argument in arguments:
            argument = argument.lower()
            if argument.startswith('-'):
                if argument == '-h':
                    print(help_message)
                    exit()
                elif argument == '-p':
                    PRINT_ACTIVE = False
                elif argument == '-c':
                    COPY_ACTIVE = False
            else:
                pairs = int(argument)

    # Generate password
    generator = PasswordGenerator()
    password = generator.generate(pairs)

    # Return password
    if PRINT_ACTIVE:
        print(password)
    if COPY_ACTIVE:
        pyperclip.copy(password)


if __name__ == '__main__':
    main()
