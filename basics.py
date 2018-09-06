from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.classify import NaiveBayesClassifier
from nltk.probability import FreqDist
import csv

f = open('trolls.csv', 'r')
file = csv.reader(f)
sentences=[]
remarks=[]
psObject = PorterStemmer()

illegal_chars = [
    '.',',','@',"'",'+','-','*',
]
paragraph=''

for kk in file :
    paragraph+=kk[0]
f.close()
f = open('trolls.csv', 'r')
file = csv.reader(f)
all_words = word_tokenize(paragraph)
# print(all_words)
all2 = FreqDist(all_words)
most_common_words = list(all2.most_common(100))
print('most commons below...')
print(most_common_words)
most_cm_1=[]
for i,j in most_common_words:
    most_cm_1.append(i)
# print(most_cm_1)
stopWords = stopwords.words('english')
all_words = []
for i in file :
    filtered=''
    filtered_from_stopWords=''
    counter = 0
    for j in range(len(illegal_chars)) :
        if counter == 0:
            counter+=1
            filtered = i[0].replace(illegal_chars[j], '')
        else :
            filtered=filtered.replace(illegal_chars[j],'')
    counter=0
    filteredArr = filtered.split(' ')
    for x in filteredArr :
        if x not in stopWords :
            filtered_from_stopWords+=x+' '
    bb=[]
    filtered_from_stopWords_ARRAY=filtered_from_stopWords.split(' ')
    features = {w.lower(): (w  in most_cm_1) for w in filtered_from_stopWords_ARRAY}
    bb.append(features)
    bb.append(i[1])
    sentences.append(bb)
    remarks.append(i[1])

count =0
print(remarks)
print(sentences)
classifier = NaiveBayesClassifier.train(sentences)
inputs = input('Enter a comment ')
words_entered=inputs.split(' ')
entry = {w: ( True) for w in words_entered}

print(classifier.classify(entry))
