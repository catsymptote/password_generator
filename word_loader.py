import json


class WordLoader:
    def __init__(self) -> None:
        self.settings = self.load_settings()
        self.adjectives, self.nouns = self.load_assets()

    def load_settings(self) -> dict:
        with open('settings.json', 'r') as f:
            file_contents = f.read()
            settings = json.loads(file_contents)
        return settings
    
    def load_assets(self):
        with open(self.settings["adjectives"], 'r') as f:
            file_contents = f.read()
            adjectives = file_contents.split('\n')

        with open(self.settings["nouns"], 'r') as f:
            file_contents = f.read()
            nouns = file_contents.split('\n')

        return adjectives, nouns


if __name__ == '__main__':
    wl = WordLoader()
    print(f'Adjectives:\t{len(wl.adjectives)}')
    print(f'Nouns:\t\t{len(wl.nouns)}')
