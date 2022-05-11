import pandas as pd
from nltk.tokenize import word_tokenize
 
example_sent = """Отримано аналіз програмних застосунків конкурентів. Створивши таблицю порівняли їх плюси та мінуси , визначили необхідні функіональні вимоги. Вимоги до конфеденційності та безпеки. Визначили можливі проблеми та вразливості ринку для вирішення та привести нововедення у ринок IT послуг. Також отпримаємо деякий список вимог до розробки , та можливо уникнимо допрацювання ПЗ, виконавши повне ТЗ одразу."""
 
stopwords_ua = pd.read_csv("stopwords_ua.txt", header=None, names=['stopwords'])
stop_words = list(stopwords_ua.stopwords)
word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)