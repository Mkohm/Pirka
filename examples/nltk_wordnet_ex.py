# NLTK WordNet Example
# This example shows how to determine word similarity using WordNet
# Author: Audun Liberg

# Remove comments from the lines below upon first run to install WordNet
#import nltk
#nltk.download()

from nltk.corpus import wordnet as wn

# Request input and convert into synsets
word1 = input("Word 1: ")
word2 = input("Word 2: ")

synset1 = wn.synsets(word1)[0]
synset2 = wn.synsets(word2)[0]

# Calculate score using path_similarity
score = synset1.path_similarity(synset2)
print("Calculated similarity: ", round(score, 3))
