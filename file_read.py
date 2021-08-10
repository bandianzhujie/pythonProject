from urllib.request import urlopen

textpage = urlopen(
    "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt"
)

print(str(textpage.read(), 'utf-8'))