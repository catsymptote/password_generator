'''Relevant link:
https://github.com/taikuukaits/SimpleWordlists'''


import json
import os
import sys
import urllib3


def make_txt(words, url):
    if url.endswith('.txt'):
        words = words[2:-1].replace('\\n', '\n')
    elif url.endswith('.json'):
        removes = ['\t', '"', ',', '  ']
        for character in removes:
            words = words.replace(character, '')

        words = words[3:-4].replace('\\n', '\n')
    else:
        return words

    # Remove trailing empty lines
    words = words.strip()
    return words


# Parse arguments
URL_LIST = 'short'
if len(sys.argv) > 1:
    URL_LIST = sys.argv[1]


# Load settings
with open('settings.json') as f:
    file_contents = f.read()
    settings = json.loads(file_contents)


# Find links
adjectives_link = settings['URLs'][URL_LIST]['adjectives']
nouns_link = settings['URLs'][URL_LIST]['nouns']


# Set up downloader
http = urllib3.PoolManager()


# Download adjectives and nouns
adj_response = http.request("GET", adjectives_link)
adj_status = adj_response.status
adjectives = str(adj_response.data)

# Download nouns
noun_response = http.request("GET", nouns_link)
noun_status = noun_response.status
nouns = str(noun_response.data)


# Convert to JSON if necessary
adjectives = make_txt(adjectives, adjectives_link)
nouns = make_txt(nouns, nouns_link)


# Write text files
if not os.path.exists('assets'):
    os.mkdir('assets')
with open(settings['adjectives'], 'w', encoding='utf-8') as f:
    f.write(adjectives)
with open(settings['nouns'], 'w', encoding='utf-8') as f:
    f.write(nouns)


# Print results
adj_len = adjectives.count('\n')
noun_len = nouns.count('\n')

print(f'Word list \tStatus \tAmount')
print(f'Adjective\t{adj_status} \t{adj_len}')
print(f'Noun\t\t{noun_status} \t{noun_len}')
