#!/usr/bin/python
import argparse
from random import choice
from os.path import isfile

parser = argparse.ArgumentParser()
parser.add_argument("-n", metavar="number", help="Number of passphrases to generate", type=int, default=1)
parser.add_argument("-l", metavar="number", help="Number of words in each passphrase", type=int, default=4)
parser.add_argument("-s", metavar='"separator"', help="Separator used between each word", default=" ")
parser.add_argument("-d", metavar="path", help="The path to a custom dictionary", default="dictionaries/google-10000-english-usa-no-swears-medium.txt")
parser.add_argument("--script", help="Output only the generated passphrase(s), useful for scripting", action="store_true")
args = parser.parse_args()

if not isfile(args.d):
    print("Dictionary file not found")
    quit()

if args.n < 1:
    print("Cannot generate less than one passphrase")
    quit()

if args.l < 1:
    print("Cannot generate a passphrase with less than 1 word")
    quit()

with open(args.d, "r") as file:
    words = file.readlines()

    #remove newlines and whitespace from end of lines
    for i, x in enumerate(words):
        words[i] = x.rstrip()

    #generate and print passphrases
    for i in range(args.n):
        phraseList = []
        for i in range(args.l):
            phraseList.append(choice(words))
        phrase = args.s.join(phraseList)
        print(phrase)

    if not args.script:
        print(f"Words in dictionary: {len(words)}")