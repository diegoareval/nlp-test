import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords
from textblob import Word
import re
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from nltk import word_tokenize, pos_tag, ne_chunk


word_to_find = "find"
english = 'english'
spanish = 'spanish'
text1 = """He determined to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and 
    fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had 
    indeed the vaguest idea where the wood and river in question were."""

paragraph="a about about \n after all \n also keep always am an and any are at be been being but by came can cant come could did didn't do does doesn't doing don't else for from get give goes going had happen has have having how i if ill i'm in into is isn't it its i've just keep let like made make many may me mean more most much no not now of only or our really say see some something take tell than that the their them then they thing this to try up us use used uses very want was way we what when where which who why will with without wont you your youre"

def printInfo(freq):
	for key,val in freq.items():
		print(str(key) + ':' + str(val))
	#freq.plot(20, cumulative=False)

def lemmatization(text):
    input_str="Muchos de los recursos de este portal han sido publicados en la revista ELE Punto y Coma."
    lem = []
    for i in input_str.split():
        word1 = Word(i).lemmatize("n")
        word2 = Word(word1).lemmatize("v")
        word3 = Word(word2).lemmatize("a")
        lem.append(Word(word3).lemmatize())
    print(lem)

def toLower(text):
	print(text.lower())

def removeNumber(text):
	result = re.sub(r'\d+', '', text)
	print(result)

def entityRecognition():
    input_str = "Bill works for Apple so he went to Boston for a conference."
    print(ne_chunk(pos_tag(word_tokenize(input_str))))



def lemma1():
    lemmatizer=WordNetLemmatizer()
    input_str="been had done languages cities mice"
    input_str=word_tokenize(input_str)
    for word in input_str:
        print(lemmatizer.lemmatize(word))

def partSpeech():
    input_str="Muchos de los recursos de este portal han sido publicados en la revista ELE Punto y Coma."
    result = TextBlob(input_str)
    print(result.tags)

def shallowParsing():
    input_str="A black television and a white stove were bought for the new apartment of John."
    result = TextBlob(input_str)
    #print(result.tags)
    #chunking
    reg_exp = "NP: {<DT>?<JJ>*<NN>}"
    rp = nltk.RegexpParser(reg_exp)
    result = rp.parse(result.tags)
    print(result)
    result.draw()

def normalization(text):
    set(stopwords.words('english'))


    stop_words = set(stopwords.words('english')) 
  
    word_tokens = word_tokenize(text) 
    
    filtered_sentence = [] 
  
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 

    Stem_words = []
    ps =PorterStemmer()
    for w in filtered_sentence:
        rootWord=ps.stem(w)
        Stem_words.append(rootWord)
    print(filtered_sentence)
    #print("stem: {}".format(Stem_words))




response =  urllib.request.urlopen("https://en.wikipedia.org/wiki/{}".format(word_to_find))
html = response.read()
#print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
#print(text)
tokens = [t for t in text.split()]
#print(tokens)

sr= stopwords.words(english)
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words(english):        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
#printInfo(freq)
#lemmatization(text)
#normalization(text1)
#toLower(text1)
#removeNumber(text1)
#lemma1()
#partSpeech()
#shallowParsing()
#entityRecognition()

    



