#Testing Testing
from difflib import get_close_matches

def closeMatches(patterns, word):
    if get_close_matches(word, patterns):
        print('1')
    else:
        print('0')

def main():
    word = 'AT & T'
    patterns = ['AT&T', 'Pepsi']
    closeMatches(patterns, word)

main()