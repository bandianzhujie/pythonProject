from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import string
import re


def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    #print(input)
    input = input.split(' ')
    #output = []
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
        #range(len(input) - n + 1):
        #output.append(input[i:i+n])
    return cleanInput
def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", 'have', "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                   "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
                   "by", "she", "or", "as", "what", "go", "their", "can", "who", "get",
                   "if","would","her","all","my","make","about","know","will",
                   "as","up","one","time","has","been","there","year","so",
                   "think","when","which","them","some","me","people","take",
                   "out","into","just","see","him","your","come","could","now",
                   "than","like","other","how","then","its","our","two","more",
                   "these","want","way","look","first","also","new","because",
                   "day","more","use","no","man","find","here","thing","give",
                   "many","well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False


def ngrams(input, n):
    input = cleanInput(input)
    #output = []
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n]).encode('utf-8')
        if isCommon(ngramTemp.split()[0]) or isCommon(ngramTemp.split()[1]):
            pass
        else:
            if ngramTemp not in output:
                output[ngramTemp] = 0
            output[ngramTemp] += 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
print("2-grams count is : " + str(len(ngrams)))