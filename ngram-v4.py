# #### ngram.py ####
# python script which randomly generates sentences
# using phrases from given input texts. Sentences are
# generated using an n-gram model
#
# Author: Ankur Patel
#
# Course:
# Instructor: 
#
# Algorithm:
# 	IN:
#   	training_corpus: text file
#   	n - length of ngram sequence to parse and generate
#   	m - number of sentences to generate
# 	OUT: m sentences generated using n-gram model
# ##################


import sys


def main():
    corpus_string = ""

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    # input arbitrary number of files
    num_files = len(sys.argv) - 2
    file_index = 3
    file_list = []
    
    for i in range(num_files):
        current_file = sys.argv[file_index]
        with open(current_file) as f:
            corpus_string = f.read()
        file_index += 1

    # welcome message
    print("Welcome to ngram.py\n")
    print("This script was written by Ankur Patel\n")

    print("User-selected options: \n")
    print("n - " + n)


def process_text():
    pass

def train_model():
    pass


def count_ngrams():
    pass


if __name__ == "__main__":
    main()