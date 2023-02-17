import argparse
import os
import pyperclip
from random import SystemRandom

from word_loader import WordLoader


class PasswordGenerator:
    def __init__(self):
        # Read files
        file_path = os.path.realpath(__file__)
        self.wl = WordLoader() 

        self.symbols = '.,;:!?@#$%^&*()_+=-[]{}|;'
        self.numbers = '0123456789'

        self.rand = SystemRandom()

    def get_random_index(self, iterable):
        random_number = self.rand.random()
        section_size = 1 / len(iterable)
        random_index = int(random_number // section_size)
        return random_index

    def get_random(self, words) -> str:
        random_index = self.get_random_index(words)
        return words[random_index]

    def get_random_pair(self):
        adjective = self.get_random(self.wl.adjectives)
        noun = self.get_random(self.wl.nouns)
        return (adjective, noun)

    def insert_random(self, pw: str, instertion_iterable) -> str:
        value = self.get_random(instertion_iterable)
        index = self.get_random_index(instertion_iterable)
        return pw[:index] + value + pw[index:]

    def generate_words(self, pairs: int) -> str:
        password = ''
        for _ in range(pairs):
            adjective, noun = self.get_random_pair()
            password += f'{adjective.title()} {noun.title()} '
        return password[:-1]

    def generate(self, options):
        pw = self.generate_words(options['pairs'])
        for _ in range(options['symbols']):
            pw = self.insert_random(pw, self.symbols)
        for _ in range(options['numbers']):
            pw = self.insert_random(pw, self.numbers)
        for _ in range(options['symnum']):
            pw = self.insert_random(pw, self.symbols + self.numbers)
        return pw


def parse_args():
    arg_desc = '''\
        Let's load an image from the command line!
        --------------------------------
            This program loads an image
            with OpenCV and Python argparse!
        '''
    parser = argparse.ArgumentParser()  # formatter_class =
                                     #argparse.RawDescriptionHelpFormatter,
                                     #description= arg_desc)

    parser.add_argument('-e', '--echo', metavar='ECHO',
                        help='Echo the password')
    parser.add_argument('-p', '--pairs', metavar='PAIRS',
                        help='Print the password')
    parser.add_argument('-c', '--copy', metavar='COPY',
                        help='Copy the password to clipboard')
    parser.add_argument('-s', '--symbols', metavar='SYMBOLS',
                        help='Number of symbols in the password')
    parser.add_argument('-n', '--numbers', metavar='NUMBERS',
                        help='Number of numbers in the password')
    parser.add_argument('-sn', '--symnum', metavar='SYMNUM',
                        help='Number of symbols and numbers in the password')

    args = vars(parser.parse_args())
    return args


def is_yes(answer):
    yes_answers = ['y', 'yes', 'yeah', 'yup', 'yep', 'True', 'true', 't', '1']
    return answer in yes_answers


def construct_options(args):
    # Default values
    options = {
        'echo': True,
        'copy': True,
        'pairs': 3,
        'symbols': 0,
        'numbers': 0,
        'symnum': 0
    }

    # Set options from args
    if args['echo']:
        options['echo'] = is_yes(args['echo'])
    if args['copy']:
        options['copy'] = is_yes(args['copy'])

    if args['echo']:
        options['pairs'] = int(args['echo'])
    if args['symbols']:
        options['symbols'] = int(args['symbols'])
    if args['numbers']:
        options['numbers'] = int(args['numbers'])
    if args['symnum']:
        options['symnum'] = int(args['symnum'])

    return options


def main():
    # Parse arguments and set options
    args = parse_args()
    options = construct_options(args)

    # Generate password
    generator = PasswordGenerator()
    password = generator.generate(options)

    # Return password
    if options['echo']:
        print(password)
    if options['copy']:
        pyperclip.copy(password)


if __name__ == '__main__':
    main()
