#import nltk
#from  nltk import*

#nltk.download()  #download texts
from nltk.book import *#text1, sents, sent1

#a= text1

#print( sents())
print( sent1) # ['Call', 'me', 'Ishmael', '.']
print("_____________________________________________")
print( sent7) # ['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
print("\n")

dist =FreqDist(text7)
print(dist)#<FreqDist with 12408 samples and 100676 outcomes>

print("\n")
vocab1 = dist.keys()
print(vocab1[:5])#[u'Mortimer', u'foul', u'Heights', u'four', u'spiders']
