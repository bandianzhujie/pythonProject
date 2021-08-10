from nltk import word_tokenize
from nltk import Text
from nltk.book import *
from nltk import FreqDist
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams


#tokens = word_tokenize("Here is some very interesting text")
#text = Text(tokens)
print("-----------------------------")
print("the text length is  %d" %len(text6))
print("-------------------------")
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[("Sir", "Robin")])
print("------------------------------")
fdist = FreqDist(text6)
print(fdist.most_common(10))
print("----------------------")
print(fdist["Grail"])

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
fourgram = ngrams(text6, 4)
fourgramDist = FreqDist(fourgram)
print(fourgramDist[("father", "smelt", "of", "elderberries")])