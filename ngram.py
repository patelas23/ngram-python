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


# Generic imports
import re
from sys import argv
from random import random



# Regex to detect end of sentences
punctuator = re.compile(r"!\.\?")
despacer = re.compiler(r"\S")
start_tagger = re.compile(r"<start>")
end_tagger = re.compile(r"<end>")

# Insert spaces between stored words
space_joiner = ' '.join

current_corpus = ''
corpus_arr = []
history_dict = dict

# minimum of one start tag
ngram_start_tags = ""

n = argv[0]

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
    current_corpus = f.read().lower()

# Delimit file by punctuation
punctuation_match = punctuator.search(current_corpus)

# Add <start> and <end> tags
current_corpus = ngram_start_tags + current_corpus
current_corpus = punctuator.sub(ngram_start_tags + "<end>", current_corpus)

# Split corpus along whitespace -> array of words

# Create dictionary of all uniquely identified words

# Create scrolling n-sequence window

# Create dictionary for n-sequence history

# Create n-gram dictionary using history and current word

# Generate n-gram sentences from <start> to <end>

