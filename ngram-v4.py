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


from collections import Counter
from collections import defaultdict
import sys
import re
import random

def main():
    ngram_model = {}
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
        train_model(n, corpus_string, ngram_model)
        file_index += 1

    # welcome message
    print("Welcome to ngram.py\n")
    print("This script was written by Ankur Patel\n")
    print("User-selected options: \n")
    print("n - " + n + "\n")
    print("number of sentences to generate: " + m + "\n")

    generate_sentences(n, m, ngram_model)


def clean_text():
    pass



def create_start_tags(n):
    tags = ""
    for i in range(n-1):
        tags = tags + " <start> "
    return tags
# Function which inputs corpus as a raw string,
# applies start and end tags to it, and returns
# the result as a list of words
def apply_tags(n, corpus):
    start_tags = create_start_tags(n)
    end_tag = " <end> "

    started_corpus = create_start_tags(n) + corpus

    combined_tags = end_tag + start_tags

    return re.sub(r'[!.?]', combined_tags, started_corpus)


# Function which updates the current ngram model
# with information from the supplied word list
def train_model(n, corpus, model):
    slide_window = list()
    # Clean up text

    # Apply start and end tags
    tagged_corpus = apply_tags(n, corpus)
    # Generate list of words from corpus
    word_list = tagged_corpus.split(' ')
    # Key model through history (n-1 gram)
    # Add list of possible next words to each history
    for word in word_list:
        slide_window.append(word)
        if len(slide_window) == n:
            next_word = slide_window.pop()
            history = slide_window
            if history in model:
                if next_word in model[history]:
                    model[history][next_word] += 1
                else:
                    model[history][next_word] = 1
            else:
                model[history] = {}
                model[history][next_word] += 1
            # Restart current ngram when end tag is reached
            if next_word == "<end>":
                slide_window.clear()


# Use trained ngram model to generate the specified number of
# sentences.
# Algorithm:
def generate_sentences(n, m, trained_model):
    current_history = list(create_start_tags(n))

    current_word = ""
    current_sentence = ""

    i = 0

    while current_word != "<end>":
        current_choice = ""

        possible_word_counts = trained_model[current_history]
        seen = 0

        history = trained_model[current_history]
        total_history_occurence = sum(history.values())

        choice = random.randint(1, total_history_occurence)

        choice_list = list(possible_word_counts.keys())

        while seen < choice:
            current_choice = choice_list[i]
            seen += possible_word_counts[current_choice]

        if current_choice != "<end>":
            current_sentence += " "
            current_sentence += current_choice

            current_history.pop(0)
            current_history.append(current_choice)

    print(current_sentence)



if __name__ == "__main__":
    main()
