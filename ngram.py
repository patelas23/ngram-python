###### ngram.py ######
# A python script to parse supplied text, to build 
#   an n-gram model for sentence generation. 
# 
# Author: Ankur Patel
# 
# Algorithm:
#   IN: n - number of words in n-gram sequence
#       m - number of sentences to generate
#       filename(s)
#   OUT: Sentences generated using n-gram model
#   Description: 
# 

# ##################
current_corpus = ['I', 'am', 'here']
# ##################


# Generic imports
from json.tool import main
import re
from sys import argv
from random import random
from collections import deque
from unicodedata import name


# Regex to detect end of sentences
punctuator = re.compile(r"!\.\?")
despacer = re.compile(r"\S")
start_tagger = re.compile(r"<start>")
end_tagger = re.compile(r"<end>")

# Insert spaces between stored words
space_joiner = ' '.join

# input corpus as a single, long string
current_corpus = ''
# array of words parsed from above string
corpus_arr = []
# contains all parsed ngrams
ngram_dict = dict()
# contains (n-1)grams and their frequencies 
history_dict = dict()

# minimum of one start tag
ngram_start_tags = ""

n = argv[0]

# N-size window
ngram_deq = deque()

# Create n-1 start tags
for _ in range(n-1):
    ngram_start_tags = ngram_start_tags + "<start>"


m = argv[1]
num_files = argv.__len__
# # Iterate through each available filename
# for arg in range(argv.__len__ - 2):
#     current_file = argv[arg + 2]

# # ### Testing with a single filename
# current_file = open(argv[2], 'r')
# # Read file as a single, all lowercase string
# TODO: parse string as usual for starts of sentences
with open(argv[2]) as f:
    current_corpus = f.read()

# Delimit file by punctuation
punctuation_match = punctuator.search(current_corpus)

# Add <start> and <end> tags
current_corpus = ngram_start_tags + current_corpus
current_corpus = punctuator.sub(ngram_start_tags + "<end>", current_corpus)

# Split corpus along whitespace -> array of words
corpus_arr = current_corpus.split()

# Create dictionary of all uniquely identified words

# Create scrolling n-sequence window
# For each word in current corpus
for word in corpus_arr:
    ngram_deq.append(word)
    if(ngram_deq.__len__ == n):
        previous_word = ngram_deq.pop()
        if previous_word == "<end>":
            # store current ngram, then clear it
            pass
    if word in ngram_dict:
        ngram_dict[word] += 1
    else:
        ngram_dict[word] = 1

    
# Create dictionary for n-sequence history

# Create n-gram dictionary using history and current word

# Generate n-gram sentences from <start> to <end>



# if name == '__main__':
    # import sys
    # n = int(sys.argv[0])