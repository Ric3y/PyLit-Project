'''
Assignment: Python Project
Onlinegdb Name: Tam T
Due: 04/17/2024
Name: Tam Truong
ID: 1002067897

Movie name: Deadpool
Source: https://www.scriptslug.com/script/deadpool-2016
'''

import string

# Function to clean words
# Note: string.punctuation is a list of sets of all punctutations: 
# !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 
def clean_word(word):
    word = word.lower().strip(string.punctuation)
    return word

# Read script from input file and get total lines
with open("myMarvelScript.txt", 'r', encoding='utf-8') as file:
    script_lines = file.readlines()
    total_lines = len(script_lines)

words = []
counts = []

# Count words
total_words = 0
for line in script_lines:
    words_in_line = line.split()
    total_words += len(words_in_line)
    for word in words_in_line:
        cleaned_word = clean_word(word)
        if cleaned_word:
            if cleaned_word not in words:
                words.append(cleaned_word)
                counts.append(1)
            else:
                index = words.index(cleaned_word)
                counts[index] += 1

unique_words_count = len(words)

# Output to file
with open("output.txt", 'w', encoding='utf-8') as output_file:
    output_file.write(f"Movie Script: Deadpool\n")
    output_file.write(f"Source: https://www.scriptslug.com/script/deadpool-2016\n\n")
    
    output_file.write(f"Total number of lines in the script: {total_lines}\n\n")
    
    output_file.write(f"Total number of words in the script: {total_words}\n")
    output_file.write(f"Total number of unique words in the script: {unique_words_count}\n\n")
    
    # Sort by most frequent 
    output_file.write("Most frequent words:".ljust(50))
    sorted_by_frequency = sorted(zip(words, counts), key=lambda pair: pair[1], reverse=True)

    #Sort by alphabetical order
    sorted_alphabetically = sorted(zip(words, counts), key=lambda pair: pair[0], reverse=False)
    output_file.write("Words in alphabetical order:\n")
    
    # Formatting output in 2 different columns
    for (word_alphetically_sorted, count_alphetically_sorted), (word_sorted_by_frequency, count_sorted_by_frequency) in zip(sorted_by_frequency, sorted_alphabetically):
        output_file.write(f"{word_alphetically_sorted}: {count_alphetically_sorted}".ljust(50))
        output_file.write(f"{word_sorted_by_frequency}: {count_sorted_by_frequency}\n")

    '''
    To do:
    Focus word lists
    focus_lists = []  
    '''