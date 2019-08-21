#!/usr/bin/env python3
#shebang to locate the envyroment
import sys
from urllib.request import urlopen

def get_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = get_words(url)
    print_items(words)

# we can execute the function as script
# the module i been executed
if __name__ == '__main__':
    # main(sys.argv[1])
    main('http://sixty-north.com/c/t.txt')