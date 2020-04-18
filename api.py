from flask import Flask
from flask_restful import Resource, Api
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


app = Flask(__name__)
api = Api(app)

def removeNumber(text):
	result = re.sub(r'\d+', '', text)
	return result

def toLower(text):
	return text.lower()

def removeCharacter(text):
	print("por implementar por {}".format("Mike"))

class partSpeech(Resource):
	def get(self, name):
		text1 = """He determined 5 to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had indeed the vaguest idea where the wood and river in question were."""
		nuevotexto=removeNumber(text1)
		result = TextBlob(toLower(nuevotexto))
		return {"Hello": result.tags}

class Lemma(Resource):
	def get(self, name):
		text1 = """He determined to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had indeed the vaguest idea where the wood and river in question were."""
		result = TextBlob(text1)
		return {"Hello": result.tags}

class Shallow(Resource):
	def get(self, name):
		text1 = """He determined to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had indeed the vaguest idea where the wood and river in question were."""
		result = TextBlob(text1)
		reg_exp = "NP: {<DT>?<JJ>*<NN>}"
		rp = nltk.RegexpParser(reg_exp)
		result = rp.parse(result.tags)
		return {"Hello": result}

class Normalization(Resource):
	def get(self, name):
		text1 = """He determined to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had indeed the vaguest idea where the wood and river in question were."""
		result = TextBlob(text1)
		return {"Hello": result.tags}

class Entity(Resource):
	def get(self, name):
		text1 = """He determined to There are several types of stemming algorithms. 5 drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had indeed the vaguest idea where the wood and river in question were."""
		result = TextBlob(text1)
		return {"Hello": result.tags}

api.add_resource(partSpeech, '/speech/<name>')
api.add_resource(Lemma, '/lemma/<name>')
api.add_resource(Normalization, '/normalization/<name>')
api.add_resource(Shallow, '/shallow/<name>')
api.add_resource(Entity, '/entity/<name>')

if __name__ == '__main__':
 app.run(debug=True)