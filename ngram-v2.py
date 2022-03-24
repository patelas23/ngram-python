# ngram.py
# 
# Author: Ankur Patel
# 
# Course: CMSC-416-001-SP2022
# Instructor: Dr. Bridgette Mckinnes
# 
# Usage: ngram.py n m input-file/s
# 
# Description:
#    A python script which learns an n-gram language model
#    from the supplied body of text using a Markov-chain algorithm. 
#   The model can be used to generate the user's desired 
#    number of sentences
#   
#   IN:
#   OUT:
# 
# Algorithm:
#  1. Build dictionary keys of each unique word,
#   a. Maintain count of each word as dictionary value
#  2. 
from collections import Counter
import re
import sys

from parso import parse

# Dictionary containing ngrams and their counts as key-value pairs
# Structure: {ngram(list): count}
ngram_model = dict()


# Return either a dictionary or a dataframe object 
def parse_corpus(n: int, corpus:str):
    # Insert n-1 start tags at beginning of corpus
    n_start_tags = ""
    for _ in range(n-1):
        n_start_tags = n_start_tags + " <start> "
    corpus = n_start_tags + corpus
    # Insert tags between each sentence
    conjoined_tag = " <end> " + n_start_tags
    corpus = re.sub(r'[?.!]', conjoined_tag, corpus)
    
    # Separate corpus into list along whitespace
    corpus_arr = corpus.split()
    
    # Remove start tag(s) from end of corpus
    for _ in range(n-1):
        corpus_arr.pop()
        
    return corpus_arr
    

# Helper function which takes a list of strings 
#  and returns all contained sequential n-grams
def find_ngrams(corpus_arr, n):
    ngram_list = []
    # For each index in the corpus until last ngram
    for i in range(len(corpus_arr) - n):
        # append current ngram to list
        ngram_list.append(tuple(corpus_arr[i:i+n]))
    return ngram_list

# Create a dictionary containing tuples of ngrams as keys: paired with 
#   their frequency counts. 
#  NEED: frequency of history, frequency of co-currence with history
# Algorithm:
#   1. 
#   2. 
#   3. 
#   4. 
def get_ngram_freq(ngram_list, n):
    # ngram_frequency = freq(ngram)/freq((n-1)-gram)
    # Count frequency of each ngram
    history_list = []
    # Count of every nth word
    for i in range(len(ngram_list)):
        history_list.append((ngram_list[i][n-1]))
    history_counts = Counter(history_list)
    ngram_counts = Counter(ngram_list)

    # print(history_counts)
    

# Generates ngram model from corpus
# 
# Algorithm: 
#   1. Create n-size widow of words 
#   2. Store each ngram in a dictionary 
#   3. Record count of each ngram
def train_model(corpus_arr: list, n):
    # Current n-length window
    ngram = tuple()
    current_ngram = list()
    # raw count of all words
    word_count = 0
    
    # extract frequency of each ngram
    get_ngram_freq(find_ngrams(corpus_arr, n), n)
    # ngram_counts = Counter(find_ngrams(corpus_arr, n))
    
    # extract frequencies of (n-1)-grams
    
    # For each word in the corpus
    for word in corpus_arr:
        word_count += 1
        current_ngram.append(word)
        
        if(len(current_ngram) == n):
            # Separate history from current word
            next_word = current_ngram.pop()
            history = tuple(current_ngram)    
            
def generate_sentences():
    pass

if __name__ == "__main__":
    # Number of words parsed at once
    n = int(sys.argv[1])
    # Number of sentences to generate
    m = int(sys.argv[2])
    # Number of input files
    num_files = len(sys.argv)
    
    corpus_string = ""
    
    # Generate model using all input files
    for i in range(3, num_files):
        with open(str(sys.argv[i])) as file:
            corpus_string = file.read()
            train_model(parse_corpus(n, corpus_string), n)
            
    # print(find_ngrams(parse_corpus(n, corpus_string), n))
    # Generate specified number of sentences using model