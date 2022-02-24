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
from collections import Counter
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

    # Count of all words for statistical analysis
    word_count = 0

    for word in corpus_arr:
        ngram_list.append(word)
        word_count += 1
        if(len(ngram_list) == n):
            next_word = ngram_list.pop()
            history = tuple(ngram_list)
            if history in ngram_dict:
                if next_word in ngram_dict[history]:
                    ngram_dict[history][next_word] += 1
                else:
                    ngram_dict[history] = {next_word: 1}
                if next_word == "<end>":
                    ngram_list = list() # Clear list at end of sentence
            else:
                ngram_dict[history] = {}
            # Shift window over by one word
            ngram_list.pop(0)
            ngram_list.append(next_word)

    return ngram_dict

# Helper function for determining total probability of next word occuring
def probability_sum(value_dict:dict, key:tuple):
    sum = 0
    for i in value_dict[key].values():
        sum += i
    return sum
    

# 
def sentence_generator(n:int, m:int, ngram_model:dict ):
    sentence_begun = False
    # Start tag tuple
    start_tags = []
    for _ in range(n-1):
        start_tags.append("<start>")
    # Produce m sentences
    for _ in range(m):
        # Generate a random float (0-1)
        rand = random()
        count = 0
        current_history = start_tags
        current_sentence = ""
        current_word = ""
        sentence_ended = False

        while(sentence_ended == False):
            prob_count = probability_sum(ngram_model, current_history)

            for next_word in ngram_model[current_history]:
                word_prob = ngram_model[current_history][next_word]/prob_count

                count += word_prob

                if(rand >= count):
                    print(next_word)

                if(next_word == "<end>"):
                    sentence_ended = True
            # Scroll history by one
            current_history.pop(0)

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

    print("Hello! welcome to my ngram script.")

    # Generate m random sentences based on model
    sentence_generator(n, m, ngram_model)
