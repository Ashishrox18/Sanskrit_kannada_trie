import re

def split_kannada_letters(word):
    consonant_set = {'ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಙ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಞ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ', 'ತ', 'ಥ', 'ದ', 'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಱ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ', 'ೞ'}
    dependent_vowel_set = {'ಾ', 'ಿ', 'ೀ', 'ು', 'ೂ', 'ೃ', 'ೄ', 'ೆ', 'ೇ', 'ೈ', 'ೊ', 'ೋ', 'ೌ'}

    letters = []
    current_letter = ''
    for character in word:
        if character in consonant_set:
            if current_letter != '':
                letters.append(current_letter)
                current_letter = ''
            current_letter += character
        elif character in dependent_vowel_set or character == '್':
            current_letter += character
        else:
            if current_letter != '':
                letters.append(current_letter)
                current_letter = ''
            letters.append(character)

    if current_letter != '':
        letters.append(current_letter)

    return letters

def combine_letter_ottakshara_subscript(letters):
    subscript_offset = 837

    combined_word = ''
    for letter in letters:
        if len(letter) > 1 and letter[-1] == '್':
            combined_word += letter[:-1] + chr(subscript_offset) + letter[-1] + '\n'
        else:
            combined_word += letter + '\n'

    return combined_word


with open(r'C:\Users\HP\OneDrive\Desktop\kannada.txt', 'r', encoding='utf-8') as input_file, open(r'C:\Users\HP\OneDrive\Desktop\kannada - Copy.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        word = line.strip()
        letters = split_kannada_letters(word)
        combined_word = combine_letter_ottakshara_subscript(letters)
        output_file.write(combined_word)
        print(combined_word, end='')

