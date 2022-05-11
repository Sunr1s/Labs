import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'отримати аналіз програмний застосунок конкурент створивши таблиця порівняти плюс мінус визначити необхідний функіональний вимога вимога конфеденційність безпека визначити можливий проблема вразливість ринок вирішення привести нововедення ринок it послуга також отпримати список вимога розробка можливо уникнити допрацювання пз виконавши повня тз одразу '
documentB = 'наразі технологія блокчейний зазнати серьойзний проблема розмім вага користувач наважутися завантажуватий програма настільки великий вага том проект розвиненувати інфраструктура обмін додаток переказ « вільний » кошт на відміна звчин фіатний тарнзакція структура компанія вплинути відміна блокування ми дарувати зручний інструмент дозволяти створювати переказ 247 вихідний '

bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

idfs = computeIDF([numOfWordsA, numOfWordsB])

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)

df = pd.DataFrame([tfidfA, tfidfB])

print(tfA)
print()
print(tfB)
print()
print(idfs)
print()
print(tfidfA)
print()
print(tfidfB)
print()
print(df)

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
print()
print(df)
