
# Function accepts a list of words from a file,
# and a letter to search for.
# Returns count of the words containing that letter.

def count_letter(letter, word_list):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count

word_list = []
# word_list is populated from a file. Code not shown.
word_list = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']

# letter = input('Which letter would you like to count?')
letter = 'e'

letter_count = count_letter(letter, word_list)

print('There are', letter_count, 'words with the letter', letter)
# There are 3 words with the letter e
