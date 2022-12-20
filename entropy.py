# Settings
HASHES_PER_SECOND = 10_000_000_000
MAX_PAIR_LENGTH = 10
DIVIDER_HEIGHT = 5  # You want MAX_PAIR_LENGTH to be divisible by DIVIDER_HEIGHT


# Read files
with open('assets/adjectives.txt') as f:
    adjective_text = f.read()

with open('assets/nouns.txt') as f:
    noun_text = f.read()


# Find the number of words
length_adjectives = adjective_text.count('\n') + 1
length_nouns = noun_text.count('\n') + 1



export = f'''# Regarding password generator entropy


## Number of words per word class

+------------+-------+
| Word class | Words |
+------------+-------+
|    Noun    | {length_nouns:^5} |
| Adjective  | {length_adjectives:^5} |
+------------+-------+

'''


bar = '+-------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+'
export += f'''
## Combinations and estimated brute force time

{bar}
| Pairs | Combinations |   Seconds    |   Minutes    |    Hours     |     Days     |    Months    |    Years     |
{bar}
'''


def set_size(number, size=12):
    if number >= 10**(size + 1) or number <= 1/(10**(size + 1)) or True:
        return f'{number:.0e}'
    return f'{number}'


for i in range(1, MAX_PAIR_LENGTH + 1):
    combinations = (length_adjectives * length_nouns)**i
    seconds = combinations / HASHES_PER_SECOND
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30
    years = days / 365.24
    export += f'| {i:^5} | {set_size(combinations):^12} | {set_size(seconds):^12} | {set_size(minutes):^12} | {set_size(hours):^12} | {set_size(days):^12} | {set_size(months):^12} | {set_size(years):^12} |\n'

    if (i) % DIVIDER_HEIGHT == 0:
        export += f'{bar}\n'

if not export.endswith(f'{bar}\n'):
    export += f'{bar}\n'

# Export string
with open('report/entropy.txt', 'w') as f:
    f.write(export)
