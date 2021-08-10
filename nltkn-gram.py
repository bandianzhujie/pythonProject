from nltk.book import *
from nltk import ngrams
fourgrams = ngrams(text6, 4)
print(">>>>>>>>>>>>>>>>>")

for fourgram in fourgrams:
    if fourgram[0] == 'father':
        print(fourgram)
    #else:
     #   print(fourgram)