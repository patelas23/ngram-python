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
from collections import deque
from random import random
from sys import argv
import re
current_corpus = ['I', 'am', 'here']
# ##################

# Insert spaces between stored words
space_joiner = ' '.join

# input corpus as a single, long string
current_corpus = ''
# array of words parsed from above string
corpus_arr = []
# contains all parsed ngrams
token_dict = dict()
# contains (n-1)grams and their frequencies
history_dict = dict()
# Contains frequency of ngrams
ngram_dict = dict()

# minimum of one start tag
ngram_start_tags = ""

n = argv[0]

# N-size window
ngram_deq = deque()


num_files = argv.__len__ - 2

# # Iterate through each available filename
# for arg in range(argv.__len__ - 2):
#     current_file = argv[arg + 2]

# # ### Testing with a single filename
# current_file = open(argv[2], 'r')
# # Read file as a single, all lowercase string
# TODO: parse string as usual for starts of sentences



# Create dictionary for n-sequence history

# Create n-gram dictionary using history and current word

# Generate n-gram sentences from <start> to <end>

# Function to generate ngram model in the form of a 
#   nested dictionary. 
# 
# IN: n - number of words in ngram sequence
#     corpus_arr - list of words 
# OUT: nested dictionary containing [ngrams][next_word: count]
def ngram_analyzer(n, corpus_arr):
    # window for current ngram
    ngram_list = deque()
    # dictionary mapping history: {[list of words]: count}
    ngram_dict = dict()
    # Dictionary counting raw frequency of each word
    token_dict = dict()
    for word in corpus_arr:
        ngram_list.append(word)
        if(ngram_list.__len__ == n):
            next_word = ngram_list.pop()
            history = tuple(ngram_list)
            if history in ngram_dict:
                if next_word in ngram_dict[history]:
                    ngram_dict[history][next_word] += 1
                else:
                    ngram_dict[history] = {next_word, 1}
            else:
                ngram_dict[history] = {}

    return ngram_dict

def sentence_generator():
    pass

if __name__ == '__main__':

    import sys

    ### Regular expressions
    # Remove punctuation and spaces
    punctuator = re.compile(r"!\.\?")
    despacer = re.compile(r"\S")
    # Search for start and end tags
    start_tagger = re.compile(r"<start>")
    end_tagger = re.compile(r"<end>")

    # Create n-1 start tags
    for _ in range(n-1):
        ngram_start_tags = ngram_start_tags + "<start>"

    # input corpus variables
    current_corpus = ''

    # Command line arguments
    n = int(sys.argv[0])
    m = int(argv[1])


    with open(argv[2]) as f:
        current_corpus = f.read()

    # Delimit file by punctuation
    punctuation_match = punctuator.search(current_corpus)

    # Add <start> and <end> tags
    current_corpus = ngram_start_tags + current_corpus
    current_corpus = punctuator.sub(ngram_start_tags + "<end>", current_corpus)

    # Split corpus along whitespace -> array of words
    corpus_arr = current_corpus.split()
    print("Hello! welcome to my ngram script.")
    print(
        "Enter n: number of words in sequence \n m: number of sentences to be generated \n [files] names of files to input")
