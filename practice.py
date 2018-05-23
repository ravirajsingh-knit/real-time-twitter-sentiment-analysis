#import nltk
#from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.stem import PorterStemmer
#from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer
#sentence="Few idiots says:'My life' I reply:'than fuck your ass' "
#print(word_tokenize(sentence))
#from nltk.corpus import stopwords
#stop_words=set(stopwords.words("english"))
#sen="I will solve some of your problem but you have to pay for it. the payment must be done before performing all checkup."
#words=word_tokenize(sen)
#csen=[word for word in words if not word in stop_words]
#ps=PorterStemmer()
#for w in csen:
#    print(ps.stem(w))
#print(csen)




#train_text=state_union.raw("2006-GWBush.txt")
#sample_text=state_union.raw("2006-GWBush.txt")
#custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
#tokenized=custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for x in tokenized:
            #print(x)
            word=word_tokenize(x)
            #print(word)
            tagged=nltk.pos_tag(word)
            #chunkGram=r"""Chunk: {<.*>+}           }<VB.?|IN|DT|TO>+{"""
            #chunkParser=nltk.RegexpParser(chunkGram)
            #chunked=chunkParser.parse(tagged)
            #print(chunked)
            #chunked.draw()
            #print(tagged)
            nameEnt=nltk.ne_chunk(tagged,binary=True)
            nameEnt.draw()
            
            

    except Exception as e:
         print(str(e))
         print("Some error occ.")
#process_content()




#from nltk.stem import WordNetLemmatizer
#lemmatizer=WordNetLemmatizer()
#print(lemmatizer.lemmatize("cats"))
#print(lemmatizer.lemmatize("cati"))

#imp
#print(lemmatizer.lemmatize("better",pos="a"))
# default parameter pos="n";
#import nltk
#print(nltk.__file__)


from nltk.corpus  import wordnet
syns=wordnet.synsets("program")
print(syns[0].lemmas()[0].name())
print(syns[0].definition())

