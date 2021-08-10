from nltk.book import *
from nltk import word_tokenize, sent_tokenize, pos_tag

sentences = sent_tokenize("Google is none of the best companies in the word. I constantly google myself to see what I'm up to ")
nouns = ["NN", "NNS", "NNP", "NNPS"]
#text = word_tokenize("I got the idea for this word of the day from reading"
#                     " more about the Oxford English Corpus, that dictionary "
 #                    "maker’s tool said to have a billion words in its database.")
#from nltk import pos_tag
#print(pos_tag(text))

for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == "google" and word[1] in nouns:
                print(sentence)

