def is_sanskrit(word):
    sanskrit_range = range(0x0900, 0x097F + 1)
    return all(ord(char) in sanskrit_range for char in word)

def filter_sanskrit_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
        words = text.split()

    sanskrit_words = [word for word in words if is_sanskrit(word)]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sanskrit_words))


input_file = 'input.txt'
output_file = 'sanskrit_words.txt'
filter_sanskrit_words(input_file, output_file)