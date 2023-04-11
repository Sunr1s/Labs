# -*- coding: utf-8 -*-

import os
import re
import locale
import pandas as pd
import openpyxl

locale.setlocale(locale.LC_ALL, "Ukrainian")

# Create a folder for the files
if not os.path.exists("text_files"):
    os.mkdir("text_files")

# Here, you will add the content of your 5 text files.
file_names = [f"text_files/file_{i}.txt" for i in range(1, 6)]

file_contents = []
for file_name in file_names:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)

# Create the text files and save the content
for i, content in enumerate(file_contents):
    with open(f"text_files/file_{i + 1}.txt", "w", encoding="utf-8") as file:
        file.write(content)

# Read the files and create a dictionary of unique words
word_set = set()
for i in range(1, 6):
    with open(f"text_files/file_{i}.txt", "r", encoding="utf-8") as file:
        content = file.read().lower()
        content = re.sub(r"[^\w\s]", "", content)
        words = content.split()
        word_set.update(words)

sorted_word_list = sorted(list(word_set), key=locale.strxfrm)

# Save the dictionary to a text file
with open("dictionary.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(sorted_word_list))

# Create a DataFrame to store word occurrences
df = pd.DataFrame(columns=["file"] + sorted_word_list)
df["file"] = [f"file_{i}" for i in range(1, 6)]

# Count word occurrences and fill the DataFrame
for i, row in df.iterrows():
    with open(f"text_files/{row['file']}.txt", "r", encoding="utf-8") as file:
        content = file.read().lower()
        content = re.sub(r"[^\w\s]", "", content)
        words = content.split()
        for word in sorted_word_list:
            df.loc[i, word] = words.count(word)

df["Σ"] = df.iloc[:, 1:].sum(axis=1)

# Save the DataFrame to an Excel file
output_file = "word_occurrences.xlsx"
writer = pd.ExcelWriter(output_file, engine='openpyxl')
df.to_excel(writer, index=False, encoding="utf-8", sheet_name="Sheet1")
writer.save()

# Find words that occur only in one of the files
occurrences = df.iloc[:, 1:-1].astype(int).sum(axis=0)
unique_words = [word for word, count in occurrences.items() if count == 1]

print("Words that occur only in one of the files:")
for i, word in enumerate(unique_words, start=1):
    print(f"{i}. {word}")
