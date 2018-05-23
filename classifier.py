import nltk
import random
from nltk.corpus import movie_reviews

documents=[(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)
            ]
#print(documents)
random.shuffle(documents)
#print(documents[0])
all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())
all_words=nltk.FreqDist(all_words)
#print(all_words.most_common(15))
#print(all_words["stupid"])
#print(all_words.keys())



word_features=list(all_words.keys())[:3000]


def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features
#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
featuresets=[(find_features(rev),category) for  rev, category in documents]
training_set=featuresets[:1900]
testing_set=featuresets[1900:]

classifier=nltk.NaiveBayesClassifier.train(training_set)
#print(nltk.classify.accuracy(classifier,testing_set)*100)
#classifier.show_most_informative_features(15)


import pickle

save_classifier=open("naivebayes.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()



classifier_f=open("naivebayes.pickle","rb")
classifier=pickle.load(classifier_f)
classifier_f.close()

#print(nltk.classify.accuracy(classifier,testing_set)*100)



from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB 
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
MNB_classifier=SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print(nltk.classify.accuracy(MNB_classifier,testing_set)*100)
#GNB_classifier=SklearnClassifier(GaussianNB())
#GNB_classifier.train(training_set)
#print(nltk.classify.accuracy(GNB_classifier,testing_set)*100)
BNB_classifier=SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print(nltk.classify.accuracy(BNB_classifier,testing_set)*100)
LR_classifier=SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)
print(nltk.classify.accuracy(LR_classifier,testing_set)*100)
SGD_classifier=SklearnClassifier(SGDClassifier())
SGD_classifier.train(training_set)
print(nltk.classify.accuracy(SGD_classifier,testing_set)*100)
LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print(nltk.classify.accuracy(LinearSVC_classifier,testing_set)*100)
NuSVC_classifier=SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print(nltk.classify.accuracy(NuSVC_classifier,testing_set)*100)

#voting of classification
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers

    def classify(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        choice_votes=votes.count(mode(votes))
        conf= choice_votes/len(votes)
        return conf

voted_classifier=VoteClassifier(classifier,MNB_classifier,LR_classifier) 
print(nltk.classify.accuracy(voted_classifier,testing_set)*100)
print(voted_classifier.classify(testing_set[0][0]))
print(voted_classifier.confidence(testing_set[0][0]))

