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

import sys

# Helper function to apply (n-1) start tags and end tags to corpus string
def start_end_tagger(corpus, n):
    n_start_tags = ""
    for _ in range(n-1):
        n_start_tags = n_start_tags + " <start> "

    ngram_tags = " <end> " + n_start_tags



if __name__ == "__main__":
    print("Welcome to ngram.py!")

    # Empty buffer for input file
    corpus_string = ""
    
    # Input command line arguments
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    with open(sys.argv[3]) as f:
        corpus_string = f.read()
    f.close()
