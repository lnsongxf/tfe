from tika import parser
import os, sys
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
import nltk

pos_to_wornet_dict = {

    'JJ': wn.ADJ,
    'JJR': wn.ADJ,
    'JJS': wn.ADJ,
    'RB': 'a',
    'RBR': 'a',
    'RBS': 'a',
    'NN': 'n',
    'NNP': 'n',
    'NNS': 'n',
    'NNPS': 'n',
    'VB': 'v',
    'VBG': 'v',
    'VBD': 'v',
    'VBN': 'v',
    'VBP': 'v',
    'VBZ': 'v',
    'DT' : 'n',
    'IN' : 'n',
    'PRP$' : 'n',
    'MD' : 'n',
    'TO' : 'n',
    'CC' : 'n',
    'PRP' : 'n'

}


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

files = os.listdir(os.getcwd())
for x in range (0, len(files)):
	if os.path.isfile(files[x]):
		raw = parser.from_file(files[x])
		#print(raw['content'])
		f = open("extract\\"+files[x]+".txt", "wb")
		f.write(raw['content'].encode('utf-8'))
		f.close()
		text = ""
		textLem = ""
		
		with open("extract\\"+files[x]+".txt",encoding="utf8") as f:
			for line in f:
				for word in line.split():				
					a = nltk.pos_tag(nltk.word_tokenize(word))[0][1]
					tag = 'n'
					if a in pos_to_wornet_dict:
						tag = pos_to_wornet_dict[a]
					newWord = lemmatizer.lemmatize(word, tag)

					textLem = textLem + newWord
					textLem = textLem + " "
					
				textLem = textLem + "\n"
					
		file = open("extractLEM\\"+files[x]+"_LEM.txt", "wb")
		file.write(textLem.encode('utf-8'))
		file.close()
		print(files[x]+"LEM DONE")
					
		with open("extractLEM\\"+files[x]+"_LEM.txt",encoding="utf8") as f:
			for line in f:
				for word in line.split():
					#print(word)
					newWord = stemmer.stem(word)

					text = text + newWord
					text = text + " "
					
				text = text + "\n"
				
			file = open("extractSTEM\\"+files[x]+"_STEM.txt", "wb")
			file.write(text.encode('utf-8'))
			file.close()
			
			print(files[x]+"STEM DONE")

					
		print(files[x]+" DONE")
				
				




	#			a = nltk.pos_tag(nltk.word_tokenize(word))[0][1]
	#			tag = 'n'
	#			if a in pos_to_wornet_dict:
	#				tag = pos_to_wornet_dict[a]
	#			newWord = lemmatizer.lemmatize(word, tag)
	#			print(lemmatizer.lemmatize(word, tag))				
				
				
				
				