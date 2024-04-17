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
# This function takes a word as input, converts it to lowercase, 
# and removes any leading or trailing punctuation characters, including single and double quotation marks.
# Note string.punctuation is a list of sets of all punctutations: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~‘ !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~‘ 
def clean_word(word):
    word = word.lower().strip(string.punctuation + "‘’“”") 
    return word

# Function to count occurrences of focus words
# This function calculates the total count of focus words in the script by iterating through the focus list 
# and summing up the counts of each focus word found in the words list.
def count_focus_words(focus_list, words, counts):
    total_count = sum(counts[words.index(word)] for word in focus_list if word in words)
    return total_count

# Read script from input file and get total number of lines
with open("myMarvelScript.txt", 'r', encoding='utf-8') as file:
    script_lines = file.readlines()
    total_lines = len(script_lines)

words = []
counts = []

# This section counts the total number of words in the script, counts the occurrences of each unique word, 
# and stores them in the lists 'words' and 'counts'.
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
    output_file.write("Sorted by frequency:".ljust(50))
    sorted_by_frequency = sorted(zip(words, counts), key=lambda pair: pair[1], reverse=True)

    #Sort by alphabetical order
    sorted_alphabetically = sorted(zip(words, counts), key=lambda pair: pair[0], reverse=False)
    output_file.write("Sorted alphabetically:\n")
    
    # Formatting output in 2 different columns
    # This loop iterates over pairs of words and their corresponding counts, one pair sorted by frequency and the other sorted alphabetically.
    # It writes each word along with its count to the output file, left-aligned to a width of 50 characters, followed by the word itself, maintaining two columns of data.
    for (word_sorted_by_frequency, count_sorted_by_frequency) , (word_alphetically_sorted, count_sorted_by_alphabetically) in zip(sorted_by_frequency, sorted_alphabetically):
        output_file.write(f"{word_sorted_by_frequency} : {count_sorted_by_frequency} time(s)".ljust(50))
        output_file.write(f"{word_alphetically_sorted}\n")
    
    # Focus word lists
    focus_lists = [
    #List #1
        ["life", "face", "hero", "monster", "mask"],
    #List #2
        ["christmas", "vanessa", "love", "dopinder", "gita"],
    #List  #3
        ["francis", "torture", "cure", "kill"]
    ]

    output_file.write("\n")

    # Count focus words
    # This loop iterates over each focus list, calculates the total count of focus words in the script, 
    # and writes the results to the output file.
    for idx, focus_list in enumerate(focus_lists, start=1):
        total_focus_words = count_focus_words(focus_list, words, counts)
        output_file.write(f"Focus List {idx}: {focus_list}\n")
        output_file.write(f"Total count of focus words: {total_focus_words} times\n\n")

        output_file.write("Words sorted alphabetically (and their frequency):\n")
        # Sort the focus words and their corresponding frequencies alphabetically. 
        # Pairs each focus word from focus_list with its frequency retrieved from the counts list using list comprehension. 
        # The key parameter specifies that sorting should be based on the first element of each pair (the focus word)
        sorted_focus_words = sorted(zip(focus_list, [counts[words.index(word)] for word in focus_list]), key=lambda pair: pair[0], reverse=False)
        for word, count in sorted_focus_words:
            output_file.write(f"{word}: {count} time(s)\n")
        output_file.write("\n")