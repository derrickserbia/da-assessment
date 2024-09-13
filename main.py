import requests
from bs4 import BeautifulSoup

class CharacterCoordinates:
    def __init__(self, x:int, character, y: int):
        self.x = x
        self.character = character
        self.y = y
    
    def __str__(self) -> str:
        return f"x={self.x}, character={self.character}, y={self.y}"

def get_table_rows_from_url(url):
    r = requests.get(url)
    html_text = r.text

    soup = BeautifulSoup(html_text, 'html.parser')
    return soup('tr')

def convert_tr_to_character_coordinate(tr):
    tds = tr('td')
    x = int(tds[0].p.span.string)
    c = tds[1].p.span.string
    y = int(tds[2].p.span.string)
    return CharacterCoordinates(x, c, y)

def print_characters(characters):
    sorted_characters = sorted(characters, key=lambda c: (-c.y, c.x))
    
    max_y = sorted_characters[0].y
    x = 0
    for c in sorted_characters:
        if c.y == max_y and c.x == x:
            print(c.character, end='')
            x += 1
        elif c.y == max_y and c.x != x:
            print(' ' * (c.x - x) + c.character, end='')
            x = c.x + 1
        elif c.y < max_y:
            print()
            print(c.character, end='')
            max_y = c.y
            x = 1
            
    
def print_secret(url):

    table_rows = get_table_rows_from_url(url)

    characters = []
    for tr in table_rows[1:]:
        character = convert_tr_to_character_coordinate(tr)
        characters.append(character)

    print_characters(characters)

def main():
    print_secret("https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub")


if __name__ =="__main__":
    main()