import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'отримати аналіз програмний застосунок конкурент створивши таблиця порівняти плюс мінус визначити необхідний функіональний вимога вимога конфеденційність безпека визначити можливий проблема вразливість ринок вирішення привести нововедення ринок it послуга також отпримати список вимога розробка можливо уникнити допрацювання пз виконавши повня тз одразу '
documentB = 'наразі технологія блокчейний зазнати серьойзний проблема розмім вага користувач наважутися завантажуватий програма настільки великий вага том проект розвиненувати інфраструктура обмін додаток переказ « вільний » кошт на відміна звчин фіатний тарнзакція структура компанія вплинути відміна блокування ми дарувати зручний інструмент дозволяти створювати переказ 247 вихідний '
documentC = 'у лабораторний робот ознайомитися процес встановлення призначення система провести аналіз предметний галуза визначити функція система зробити інтерво ’ actors система – користувач сервіс директор ceo фінансист власник сформулювати функціональний вимога випливати проведений інтерво ’ виконати робот визначення функціональний вимога власний проект провести декомпозиція вимога графічно представити допомога відповідний діаграма визначити системний вимога'
documentD = 'тема гра доганлка кіт рухатися меньший швидкостью миша задача миша навздоганяти їжа гра закінчуватися кіт догнати миша програутися звук програш якщо миша успішно тікати програтися звук успіх миша наздогнати їжа програутися звук харчуваннятакож провести моделювання допомога мова моделювання bpmn вигляд діаграма'
documentE = 'у лабораторний робот здобути навичка створення специфікація функціональний вимога програмний забезпечення основа шаблон software requirements specification стандарт ieee 830 методологія розробка rup відповідний формат представлення специфікація вимога дослідити процес створення документ опис первин вимога програмний забезпечення набути практичний навичати виділення документування вимога виділенно функціональний нефункціональний вимога програмний забезпечення'
documentF = 'у лабораторний робот здобути навичка постановка завдання створення документ « ескізний проект » містить111 вибір метода рішення мова програмування112 специфікація процесів113 весь отриманий діаграми114 словник термінівнавчитися надати визначення аналіз пояснити призначення метода засіб аналіз особливість застосування метод аналіз існуючий метода збора виявлення вимогпризначення діаграма прецедент'
documentG = 'у лабораторний робот вивчити особливість застосування технологія idef0 idef3 обрати варіант використання система аналізуватися провести аналіз бізнеспроцес використовуючи технологія idef0 побудувати контекстний діаграма дочірній діаграма 1го рівня нотація idef0 здійснити текстовий опис обрати функціональний блок діаграма idef0 побудувати діаграма декомпозиція блок нотація idef3тий навести текстовий опис'
documentH = 'тестування вимога дозволяти зменшити кількість допрацювання зміна перед початок тестування вимога необхідний наступний умова вимога проаналізований задокументований працювати аналітик роль самостійно проводити певний оцінка перевірка вимога під тестування вимога відбуватися наступний процес зацікавлений особа підтверджувати вимога коректний зрозумілий достатній розпочинати робот а користувач підтверджувати вимога відображати потреба робот основний критерій готовність вимога містити вимога достатньо інформація розпочинати розробка і важливо відзначити замовник користувач проектний команда плануватися робот проект — брати участь тестування вимога враховувати різний пов ’ язаня тестування вимога аспектиий лабораторний здобутий навичка перевірка документація створений лабораторний робот 14 допомога checklist здійснити аналіз поведінка система допомога достатній покриття система тесткейс юзкейс позитивний негативний сценарій'
documentI = 'тестовий звітність метрика тестування головний qaкий інструмент підвищення візібіліт перти грамотний підхід робот тестувальник знати допомагати qa впливати процес цілий завдання набір метрика оцінити наскільки якісно тестувальник виконувати завдання визначити рівень компетенція зрілість команда qa володіючи набір показник порівнювати команда різний момент зовнішній група тестуванняметрика цикл розробка програмний забезпечення проте аналізувати аспект ефективність застосування метрика точка зір етап розробка проект отриманий інформація отримати максимальний результатотже лабораторний робот здобути навичка дослідження особливість підрахунок значення метрика орієнтований вимога визначеня значення метрика орієнтований вимога наведений формула побудова матриця відповідність функціональний вимога програмний продукт підготований тестовий сценарій'
documentJ = 'у лабораторний робот створити новий проект програмний засіб керування відстеження вимога створити новий тип вимога функціональний нефункціональний визначити атрибут створити новий документ додати функціональний нефункціональний вимога створити перегляд вимога здійснити додавання новий редагування видалення існуючий вимога налаштування атрибут провести фільтрація вимога пріоритет підрахувати кількість вимога проект мати високий середній пріоритет'

bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
bagOfWordsC = documentC.split(' ')
bagOfWordsD = documentD.split(' ')
bagOfWordsE = documentE.split(' ')
bagOfWordsF = documentF.split(' ')
bagOfWordsG = documentG.split(' ')
bagOfWordsH = documentH.split(' ')
bagOfWordsI = documentI.split(' ')
bagOfWordsJ = documentJ.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB)).union(set(bagOfWordsC)).union(set(bagOfWordsD)).union(set(bagOfWordsE)).union(set(bagOfWordsF)).union(set(bagOfWordsG)).union(set(bagOfWordsH)).union(set(bagOfWordsI)).union(set(bagOfWordsJ))

numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsC:
    numOfWordsC[word] += 1
numOfWordsD = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsD:
    numOfWordsD[word] += 1
numOfWordsE = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsE:
    numOfWordsE[word] += 1
numOfWordsF = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsF:
    numOfWordsF[word] += 1
numOfWordsG = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsG:
    numOfWordsG[word] += 1
numOfWordsH = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsH:
    numOfWordsH[word] += 1
numOfWordsI = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsI:
    numOfWordsI[word] += 1
numOfWordsJ = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsJ:
    numOfWordsJ[word] += 1



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
        if(float(val) ==0):
            idfDict[word] = 0
        else:
         idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)
tfC = computeTF(numOfWordsC, bagOfWordsC)
tfD = computeTF(numOfWordsD, bagOfWordsD)
tfE = computeTF(numOfWordsE, bagOfWordsE)
tfF = computeTF(numOfWordsF, bagOfWordsF)
tfG = computeTF(numOfWordsG, bagOfWordsG)
tfH = computeTF(numOfWordsH, bagOfWordsH)
tfI = computeTF(numOfWordsI, bagOfWordsI)
tfJ = computeTF(numOfWordsJ, bagOfWordsJ)

idfs = computeIDF([numOfWordsA, numOfWordsB, numOfWordsC, numOfWordsD, numOfWordsE, numOfWordsF, numOfWordsF, numOfWordsG, numOfWordsI, numOfWordsJ])


tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
tfidfC = computeTFIDF(tfC, idfs)
tfidfD = computeTFIDF(tfD, idfs)
tfidfE = computeTFIDF(tfE, idfs)
tfidfF = computeTFIDF(tfF, idfs)
tfidfG = computeTFIDF(tfG, idfs)
tfidfH = computeTFIDF(tfH, idfs)
tfidfI = computeTFIDF(tfI, idfs)
tfidfJ = computeTFIDF(tfJ, idfs)

df = pd.DataFrame([tfidfA, tfidfB, tfidfC, tfidfD, tfidfE, tfidfF, tfidfG, tfidfH, tfidfI, tfidfJ])

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
df.to_excel("output.xlsx",engine='xlsxwriter')
# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform([documentA, documentB])
# feature_names = vectorizer.get_feature_names()
# dense = vectors.todense()
# denselist = dense.tolist()
# df = pd.DataFrame(denselist, columns=feature_names)
# print()
# print(df)

