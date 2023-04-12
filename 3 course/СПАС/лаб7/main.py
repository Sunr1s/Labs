import os
import string
import codecs
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

nltk.download('punkt')

folder_path = 'texts'
text_files = os.listdir(folder_path)
text_data = []

for file in text_files:
    with codecs.open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
        text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation + '«»“”‘’–—' + string.digits))
        tokens = word_tokenize(text)
        text_data.extend(tokens)

fdist = FreqDist(text_data)
sorted_fdist = dict(sorted(fdist.items(), key=lambda item: item[1], reverse=True))

with codecs.open('word_frequency.txt', 'w', encoding='utf-8') as f:
    for word, freq in sorted_fdist.items():
        f.write(f'{word}: {freq}\n')

with codecs.open('stopwords_ua.txt', 'r', encoding='utf-8') as f:
    ukr_stopwords = set(word.strip() for word in f.readlines())

custom_stopwords = {word for word in ukr_stopwords if word in text_data}
fdist_stopwords = FreqDist({word: sorted_fdist[word] for word in custom_stopwords})

with codecs.open('stopwords_frequency.txt', 'w', encoding='utf-8') as f:
    for word, freq in fdist_stopwords.items():
        f.write(f'{word}: {freq}\n')

filtered_text = [word for word in text_data if word not in custom_stopwords]
fdist_filtered = FreqDist(filtered_text)
sorted_fdist_filtered = dict(sorted(fdist_filtered.items(), key=lambda item: item[1], reverse=True))

with codecs.open('filtered_word_frequency.txt', 'w', encoding='utf-8') as f:
    for word, freq in sorted_fdist_filtered.items():
        f.write(f'{word}: {freq}\n')

plt.figure(figsize=(15, 5))
fdist_filtered.plot(30, cumulative=False)
plt.show()

from sklearn.feature_extraction.text import TfidfVectorizer

def read_and_preprocess(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation + '«»“”‘’–—' + string.digits))
        tokens = word_tokenize(text)
        filtered_tokens = [word for word in tokens if word not in custom_stopwords]
        return ' '.join(filtered_tokens)

documents = [read_and_preprocess(os.path.join(folder_path, file)) for file in text_files]

vectorizer = TfidfVectorizer(use_idf=True)
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names()

tfidf_dict_list = []
for i, doc in enumerate(text_files):
    tfidf_dict = {}
    for j, feature in enumerate(feature_names):
        tfidf = tfidf_matrix[i, j]
        if tfidf > 0:
            tfidf_dict[feature] = tfidf
    sorted_tfidf_dict = dict(sorted(tfidf_dict.items(), key=lambda item: item[1], reverse=True))
    tfidf_dict_list.append(sorted_tfidf_dict)

for i, tfidf_dict in enumerate(tfidf_dict_list):
    with codecs.open(f'tfidf_{text_files[i]}.txt', 'w', encoding='utf-8') as f:
        for word, tfidf in tfidf_dict.items():
            f.write(f'{word}: {tfidf:.6f}\n')

