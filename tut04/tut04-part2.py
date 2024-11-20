from collections import defaultdict
#function to make anagrams
def group_anagrams(words):
    anagram_dict = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    return anagram_dict
#function to calculate frequency of any anagram group
def calculate_frequency(anagram_group):
    frequency = defaultdict(int)
    for word in anagram_group:
        for char in word:
            frequency[char] += 1
    return frequency
#function to calculate higher frenquency group
def find_highest_frequency_group(anagram_dict):
    highest_freq = 0
    highest_group = None
    for key, group in anagram_dict.items():
        freq = calculate_frequency(group)
        total_freq = sum(freq.values())
        if total_freq > highest_freq:
            highest_freq = total_freq
            highest_group = key
    return highest_group, anagram_dict[highest_group]

# Taking user input
words = []
print("Enter words one by one, type 'done' to finish:")
while True:
    word = input("Enter a word: ").lower()
    if word == 'done':
        break
    words.append(word)

anagram_dict = group_anagrams(words)

print("\nAnagram Dictionary")
for key, group in anagram_dict.items():
    print(f"{key}: {group}")

highest_group_key, highest_group = find_highest_frequency_group(anagram_dict)
print(f"\nGroup with highest frequency: {highest_group_key} -> {highest_group}")
