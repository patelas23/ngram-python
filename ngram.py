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
# ##################

# Insert spaces between stored words
space_joiner = ' '.join

# input corpus as a single, long string
current_corpus = ''
# array of words parsed from above string
corpus_arr = []

# minimum of one start tag
ngram_start_tags = ""

# Function to generate ngram model in the form of a 
#   nested dictionary. 
# 
# IN: n - number of words in ngram sequence
#     corpus_arr - list of words 
# OUT: nested dictionary containing [ngrams][next_word: count]
def ngram_analyzer(n, corpus_arr):
    # window for current ngram
    ngram_list = list()
    # dictionary mapping history: {[list of words]: count}
    ngram_dict = {}
    
    # Dictionary counting raw frequency of each word
    token_dict = dict()

    for word in corpus_arr:
        ngram_list.append(word)
        if(len(ngram_list) == n):
            next_word = ngram_list.pop()
            history = tuple(ngram_list)
            if history in ngram_dict:
                if next_word in ngram_dict[history]:
                    pass
                    # ngram_dict[history][next_word] += 1
                else:
                    pass
                    # ngram_dict[history] = {next_word, 1}
            else:
                ngram_dict[history] = {}
                print(ngram_dict.keys())
    return ngram_dict

# 
def sentence_generator(m, ngram_model):
    # Produce m sentences
    for _ in range(m):
        # Generate a random float (0-1)
        rand = random()
        count = 0
        # For ngram in history
        # ## For word in ngram
        # #### Generate frequencies
    # Probability(first_word) = freq(ngram)/freq(first_word)
    count = 0
    # if count > probability
    # ## print word
    # else
    # ## 
    pass


if __name__ == '__main__':

    import sys

    # Variable (n-1) start tags
    ngram_start_tags = ""

    ### Regular expressions
    # Remove punctuation and spaces
    punctuator = re.compile(r"!\.\?")
    despacer = re.compile(r"\S")
    # Search for start and end tags
    start_tagger = re.compile(r"<start>")
    end_tagger = re.compile(r"<end>")

    # input corpus variables
    current_corpus = ''

    # Command line arguments
    n = int(sys.argv[1])
    m = int(argv[2])

    with open(argv[3]) as f:
        current_corpus = f.read()

    # while num_files > 0:
    #     pass

    # Create n-1 start tags
    for _ in range(n-1):
        ngram_start_tags = ngram_start_tags + "<start>"

    # Delimit file by punctuation
    punctuation_match = punctuator.search(current_corpus)

    # Add n*<start> tags to beginning of corpus
    current_corpus = ngram_start_tags + current_corpus
    # Add <end> n*<start> tags at the end of each sentence.
    current_corpus = punctuator.sub(ngram_start_tags + "<end>", current_corpus)

    # Split corpus along whitespace -> array of words
    corpus_arr = current_corpus.split()

    # Build ngram model
    ngram_model = ngram_analyzer(n, corpus_arr)

    print(ngram_model.keys())

    print("Hello! welcome to my ngram script.")
    print(
        "Enter n: number of words in sequence \n m: number of sentences to be generated \n [files] names of files to input")
    print("")
