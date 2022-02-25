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

    start_tags = []
    for _ in range(n):
        start_tags.append("<start>")
    start_tags = tuple(start_tags)
    
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
            else:
                ngram_dict[history] = {}
            if(next_word == "<end>"):
                ngram_list = list()
                continue
            # Shift window over by one word
            ngram_list.append(next_word)
            ngram_list.pop(0)
        else:
            continue
    return ngram_dict

# Helper function for determining total probability of next word occuring
def probability_sum(value_list:list):
    sum = 0
    # dict_counts = tuple(value_dict[key].values())
    for i in range(len(value_list)):
        sum += value_list[i]

    return sum

def generate_sentences(n:int, m:int, ngram_model):
    
    start_tag_tuple = []
    sentence_list = []
    # Stores working sub-dictionary
    current_dict = dict()
    # Create n-1 start tags
    # TODO: simplify
    for _ in range(n-1):
        start_tag_tuple.append("<start>")
    start_tag_tuple = tuple(start_tag_tuple)
    # Create m sentences
    for _ in range(m):
        history_list = list()
        # Flag for end of sentence
        sentence_ended = False
        # Store list of words for each sentence
        current_sentence = list()
        current_word = ""
        history_tuple = start_tag_tuple
        history_list = list(history_tuple)
        # Scroll history until end of sentence
        while(sentence_ended == False):
            ngram_list = list()
            current_word = ""
            current_dict = ngram_model[history_tuple]
            current_prediction_list = list(current_dict.keys())
            probability_list = list(current_dict.values())
            total_probability = probability_sum(probability_list)
            count = 0.0
            rand = random()
            word_index = 0

            # In-class algorithm for weighted selection from list
            # Modified to iterate over each key:value pair, associating the probability 
            #   during exeuction.
            for word in current_prediction_list:
                count += probability_list[word_index]/total_probability
                print(count)
                if(count >= rand):
                    # TODO: fold up
                    current_word = current_prediction_list[word_index]
                    current_sentence.append(current_word)
                    history_list.pop(0)
                    history_list.append(current_word)
                    history_tuple = tuple(history_list)
                    print(history_tuple)
                    break
                else:
                    word_index += 1
                    print(word_index)
            # If the end of the sentence is reached, begin next sentence
            if(current_word == "<end>"):                
                sentence_list.append(current_sentence)
                current_sentence = ""
                sentence_ended = True
    
    
def sentence_generator(n:int, m:int, ngram_model:dict ):
    # Start tag tuple
    start_tags = []
    sentence_list = []
    for _ in range(n-1):
        start_tags.append("<start>")
    # Produce m sentences
    for _ in range(m):
        # Generate a random float (0-1)
        count = 0
        current_history = start_tags
        current_sentence = []
        spacer = " "
        current_word = ""
        sentence_ended = False

        while(sentence_ended == False):
            # Perform weighted selection of next word, given hsitory
            history_tuple = tuple(current_history)
            # Total probability of this history
            prob_count = probability_sum(ngram_model[history_tuple])
            # Gather list of possible next words
            current_list = list(ngram_model[history_tuple].keys())

            rand = random()

            for next_word in current_list:
            # for _ in range(prob_count):
                word_prob = ngram_model[history_tuple][next_word]/prob_count
                count += word_prob
                if(count >= rand):
                    # Add current word to sentence, clear variables
                    current_sentence.append(next_word)
                    count = 0
                    rand = random()
                    current_history.pop(0)
                    current_history.append(next_word)
                    print(current_history)
                    if(next_word == "<end>"):
                        sentence_list.append(spacer.join(current_sentence))
                        current_sentence = ""
                        current_history = start_tags
                        sentence_ended = True
                        print("End it!")
                    break
                else:
                    continue
    return sentence_list


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

    current_corpus = ""

    # Command line arguments
    n = int(sys.argv[1])
    m = int(argv[2])

    with open(argv[3]) as f:
        current_corpus = f.read()
    f.close()

    # while num_files > 0:
    #     pass

    # Create n-1 start tags
    for _ in range(n-1):
        ngram_start_tags = ngram_start_tags + " <start> "

    # Delimit file by punctuation
    # punctuation_match = punctuator.search(current_corpus)

    # Add n*<start> tags to beginning of corpus
    current_corpus = ngram_start_tags + current_corpus
    # Add <end> n*<start> tags at the end of each sentence.
    ngram_start_tags = " <end> " + ngram_start_tags 
    current_corpus = re.sub(r"[!.?]", ngram_start_tags, current_corpus)    
    # Split corpus along whitespace -> array of words
    corpus_arr = current_corpus.split()
    # Add <end> tag to end of corpus
    corpus_arr.append("<end>")
    
    # Remove start tags from end of corpus
    for _ in range(n-1):
        corpus_arr.pop()

    # Build ngram model
    ngram_model = ngram_analyzer(n, corpus_arr)

    print("Hello! welcome to my ngram script.")

    # Generate m random sentences based on model
    # print(sentence_generator(n, m, ngram_model))
    # sentence_generator(n, m, ngram_model)
    generate_sentences(n, m, ngram_model)

    
