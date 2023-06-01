import re

def extract_kannada_words(input_file, output_file):
    kannada_words = set()
    kannada_pattern = re.compile(r'^[ಀ-೿]+$')  # Regex pattern to match Kannada words

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                if kannada_pattern.match(word):
                    kannada_words.add(word)

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in kannada_words:
            file.write(word + '\n')

# Example usage
input_file_path = 'input.txt'  # Replace with your input file path
output_file_path = 'output.txt'  # Replace with your output file path

extract_kannada_words(input_file_path, output_file_path)
