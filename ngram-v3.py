# ##### ngram.py #######
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
#   Description: Analyze given texts, and generate all contained ngrams. 
#       Frequency statistics for each ngram are used to generate new 
#       sentences. 
# ######################

import re
import sys
from collections import Counter

# Helper function to apply (n-1) start tags and end tags to corpus string
def start_end_tagger(corpus, n):
    n_start_tags = ""
    for _ in range(n-1):
        n_start_tags = n_start_tags + " <start> "

    ngram_tags = " <end> " + n_start_tags
    tagged_corpus = re.sub(r'!\.\?', ngram_tags, corpus)

    # Remove start tags left at end
    
    return tagged_corpus
    

# Helper function to count ngrams, returning a 
# dict of {ngram: count}
# IN: corpus - input string of sentences
# OUT: ngram_counts - {ngram : count}
def count_ngrams(corpus_list):
    pass
# Helper function for calculating frequency of each ngram

# Helper function for counting unique isntances of each word
def count_words(corpus_list):
    word_counts = Counter(corpus_list)
    return word_counts


# Function to generate counts of history ((n-1)-gram)
# IN: list of words in corpus
# OUT: relative frequency table 
def train_model(corpus_list):
    unigram_counts = count_words(corpus_list)
    ngram_model = count_ngrams(corpus_list)
# Function for generating sentences using trained model

#

if __name__ == "__main__":

    # Empty buffer for input file
    corpus_string = ""
    tagged_corpus = ""
    # Input command line arguments
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    with open(sys.argv[3]) as f:
        corpus_string = f.read()
    f.close()
    tagged_corpus = start_end_tagger(corpus_string, n)
    
    print(tagged_corpus)
