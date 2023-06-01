class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def autocomplete(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]

        suggestions = []
        self._collect_suggestions(current_node, prefix, suggestions)
        return suggestions

    def _collect_suggestions(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child in node.children.items():
            self._collect_suggestions(child, prefix + char, suggestions)


def build_trie_from_file(file_path):
    trie = Trie()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            trie.insert(word)
    return trie


# Example usage
input_file_path = './kannadaexcel/sanletexa.txt'  # Path to the input file
trie = build_trie_from_file(input_file_path)

# Autocomplete
prefix = 'अ'  # The prefix to autocomplete
suggestions = trie.autocomplete(prefix)
print(f"Suggestions for '{prefix}':")
for suggestion in suggestions:
    print(suggestion)
