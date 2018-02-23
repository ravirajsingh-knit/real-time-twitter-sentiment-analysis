#noise removal
import re
def _remove_regx(input_text,regx_pattern):
	pointers=re.finditer(regx_pattern,input_text)
	for x in pointers:
		input_text=re.sub(x.group().strip(),'',input_text)
	print(input_text)	

#_remove_regx("this is #lifeofpie wonderfullllllll","#[/w]*")

#lemmatization and stemming
def _lemmatization():
	from nltk.stem.wordnet import WordNetLemmatizer
	lem=WordNetLemmatizer()
	from nltk.stem.porter import PorterStemmer
	stem=PorterStemmer()
	word="multiplying"
	print(lem.lemmatize(word,"v"))
	print(stem.stem(word))

def _lookup_words(input_text):
	lookup_dict={'rw':'Retweet','msg':'message','fb':'facebook','luv':'love'}
	words=input_text.split()
	new_word=""
	for word in words:
		if word in lookup_dict.keys():
			new_word=new_word+" "+lookup_dict[word]
		else:
			new_word=new_word+" "+word
	print(new_word)
_lookup_words("rw and fb are most luv social media")
		
