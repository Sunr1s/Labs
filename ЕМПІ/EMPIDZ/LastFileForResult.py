import pymorphy2
import string
import pandas as pd
import simplemma
from simplemma import text_lemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize

morph = pymorphy2.MorphAnalyzer(lang='uk')
# Ваш текст
text = "Наразі, технологія блокчейну зазнала серьойзну проблему з розмім и вагою, не кожен користувач наважеться завантажуватим програму, з настільки великою вагою. Тому наш проект з розвиненую інфраструктурою обміну , додаток для переказів «вільних» коштів. НА відміну від звчиних фіатних тарнзакцій , ніяка структура чи компанія не вплине на неї (відміна , блокування). Ми даруємо вам зручний інструмент , що дозволяє створювати перекази 24/7 , без вихідних."
string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# пунктуацию будем удалять в цикле
for p in string.punctuation:
    if p in text:
        # банальная замена символа в строке
        text = text.replace(p, '')

word_tokens = word_tokenize(text)
# токенезация предложений
print(sent_tokenize(text))
# токенезация слов
print(word_tokens)


#--- Stop Words ---
# импортируем файл со стоп словами, каждое стоп слово должно начинатся с новой строки и находится в  папке etc под програмой
stopwords_ua = pd.read_csv("etc/stopwords_ua.txt", header=None, names=['stopwords'])
stop_words = list(stopwords_ua.stopwords)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
 
filtered_sentence = []
# в цикле удаляем совпадения
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(filtered_sentence)


#--- Stemming ---
# каждое слово проверяем в цикле , используем библиотечную функцию
for ele in filtered_sentence:
    p = morph.parse(ele)[0]
    print(p.normal_form, end=' ')


#--- Optional Lemming ---
langdata = simplemma.load_data('uk')
# Python program to convert a list to string
print()
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ' '+ele  
    
    # return string  
    return str1 

print(text_lemmatizer(listToString(filtered_sentence), langdata))
