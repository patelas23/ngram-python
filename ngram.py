###### ngram.py ######
# A python script to parse supplied text, to build 
#   an n-gram model for sentence generation. 
# 
# Author: Ankur Patel
# 
# Algorithm:
#   IN: 
#   OUT:
#   Description:
# 


# Generic imports
import re
from sys import argv
from random import random

# Insert spaces between stored words
space_joiner = ' '.join

# Regex to detect end of sentences
punctuator = re.compile(r"!\.\?")

current_corpus = ''

# number of words in n-gram sequences
n = argv[0]
# number of sentences to be generated
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

# Add <start> and <end> tags

