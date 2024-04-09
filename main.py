'''
Assignment: Python Project
Onlinegdb Name: Tam T
Due: 04/17/2024
Name: Tam Truong
ID: 1002067897
'''

import re

def clean_text(text):
    cleaned_text = re.sub(r'\s+|[,.]', '', text)
    return cleaned_text

with open('script.txt', 'r', encoding="utf-8") as file:
    text = file.read()

cleaned_text = clean_text(text)
text_array = cleaned_text.split()


with open('output.txt', 'w', encoding="utf-8") as file:
    for word in text_array:
        file.write(word + '\n')  