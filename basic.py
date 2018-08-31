a = 'I am harkishen singh and i m very studious working hard.I study in cet bhubaneswar which is a college.\
harkishen is naughty boy'
afterShifts = [
    'bad','good','worst','best','great'
]
from data_knowledge.prepositions import preposition_array
from data_knowledge.adjectives import adjectives
import csv
file = open('verbs.csv','r')
f = csv.reader(file)
verbs_available = []
for i in f:
    for j in range(len(i)):

        if i[j] !='' :
            # print(i[j])
            verbs_available.append(i[j])
file2 = open('verbs2.csv','r')
f2=csv.reader(file2)
for i in f2:
    for j in i :
        verbs_available.append(j)

print('verbs array below')
print(verbs_available)
print('size : '+ str(len(verbs_available)))
print('prepositions below')
print(preposition_array)
print('size : '+str(len(preposition_array)))
print('adjectives below')
print(adjectives)
print('size : '+str(len(preposition_array)))
genWords = preposition_array

def analysier(sets) :
    sentences = []
    b = sets.split('.')
    words = []
    for i in range(len(b)) :
        print('counter')
        words = b[i].split(' ')
        sentences.append(words)
    print(sentences)
    for i in range(len(sentences)):
        sen = sentences[i]
        for j in range(len(sen)):
            word = sen[j]
            if word in verbs_available :
                print('plain availability word : '+word)
            if word in verbs_available and j<(len(sen)-1) and j>0 and  not (word in genWords) :
                print('Specific word : '+word)
                for k in range(j+1, len(sen)) : # afterworth scanning
                    wordAft = sen[k]
                    if not (wordAft in genWords) :
                        print('after word : ' + wordAft)
                        break
                for k in range(0, j) :
                    wordBef = sen[k]
                    if not (wordBef in genWords) :
                        print('before word : ' + wordBef)
                        break
                print('finals ..\n\n')
                print(wordBef + ' '+word+' '+wordAft+'\n')
    # for i in range(len(b)) :
    #     for x in range(words[i]) :
    #         w = words[x]
analysier(a)