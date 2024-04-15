# Input word replacement pairs as a string
replacement_input = input().strip()

# Split the input into pairs of original and replacement words
replacement_pairs = replacement_input.split()

# Construct the replacement dictionary
replacement_dict = {}
for i in range(0, len(replacement_pairs), 2):
    original = replacement_pairs[i].strip('()')
    replacement = replacement_pairs[i + 1].strip('()')
    replacement_dict[original] = replacement

# Read the sentence
sentence = input()

# Split the sentence into words and replace words from the original list
words = sentence.split()
replaced_words = [replacement_dict.get(word, word) for word in words]

# Join the modified words back together to form the replaced sentence
replaced_sentence = ' '.join(replaced_words)

print(replaced_sentence)
