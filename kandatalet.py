import re
from collections import Counter

def get_most_common_letters(input_file):
    kannada_letters = re.findall(r'[ಀ-೿]', open(input_file, 'r', encoding='utf-8').read())
    letter_counts = Counter(kannada_letters)
    most_common_letters = letter_counts.most_common()

    for letter, count in most_common_letters:
        print(letter, count)

# Example usage
input_file_path = 'input.txt'  # Replace with your input file path

get_most_common_letters(input_file_path)
