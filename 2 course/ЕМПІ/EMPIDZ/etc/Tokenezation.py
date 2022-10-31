import string
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
  
text = "Отримано аналіз програмних застосунків конкурентів. Створивши таблицю порівняли їх плюси та мінуси , визначили необхідні функіональні вимоги. Вимоги до конфеденційності та безпеки. Визначили можливі проблеми та вразливості ринку для вирішення та привести нововедення у ринок IT послуг. Також отпримаємо деякий список вимог до розробки , та можливо уникнимо допрацювання ПЗ, виконавши повне ТЗ одразу."
string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# пунктуацию будем удалять в цикле
for p in string.punctuation:
    if p in text:
        # банальная замена символа в строке
        text = text.replace(p, '')
print(sent_tokenize(text))
print(word_tokenize(text))
print(wordpunct_tokenize(text))
