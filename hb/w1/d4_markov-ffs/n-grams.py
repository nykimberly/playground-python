"""
Further Study
Do any of the following:

Replace our dummy file with your own. Pass in this file from the command line, using sys.argv.

The longer the sequence of words to the left of the arrow, the closer it becomes to the original text, as well as valid English, because there are fewer and fewer random successors. Here, we use n_grams (word pairs) and a successor, but we could use trigrams or n-grams (sequences of n words). The longer the n-gram, the closer you get to the source text.

Modify the program to allow any number of words to use as keys so you can easily choose the size of your n-gram used in your chain rather than always using bi-grams.

Begin on a capital letter and end only at an instance of sentence punctuation.

See what happens when you mix two different authors together as a single source. This often works best when they have somewhat similar writing styles; trying to combine Dr. Seuss and the Bible probably wouldn’t work as well as combining two Jane Austen books.

i.e. 
>> python3 n-grams.py pe.txt sorority-speech.txt kant.txt
"""

import sys
import random
import markov_helpers as mh

def make_chains(text_string, n):
    
    chains = {}
    words = text_string.split()
    current_index = 0
    remaining_index = len(words)-1

    while current_index < len(words)-(n+1):

        n_gram = tuple(words[current_index:current_index+n])
        current_index += 1
        remaining_index -= 1
        subsequent_word = words[current_index+n]
        if n_gram in chains:
            chains[n_gram].append(subsequent_word)
        else:
            chains[n_gram] = [subsequent_word]
        
    return chains


n_gram = 3

input_text = ""
for i in range(len(sys.argv[1:])):
    print(sys.argv[i+1])
    input_text += mh.open_and_read_file(sys.argv[i+1])

print(input_text)
chains = make_chains(input_text, n_gram)

for chain in chains:
    print(chain,":",chains[chain])

random_text = mh.make_text(chains, n_gram)
print(random_text)
