def greet(name):
    return f"Hello, {name}"

def rectrangle_area(width, height):
    return width * height

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def is_even(number):
    return number % 2 == 0

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def finding_longest_word(sentence):
    word = sentence.split
    return max(word, key=len)

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 80:
        return "D"
    else:
        return "F"

def list_stats(number):
    if not number:
        return None, None, None
    lowest, heighest, average = min(number), max(number), sum(number) / len(number)
    return lowest, heighest, average

def is_palindrome(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def word_frequency(text):
    clean = "".join(char.lowe() if char.isalnum() or char.isspacr() else " " for char in text)
    words = clean.split
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

import string
# open and read the file
with open("sample.txt", "r") as file:
    text = file.read()

print(text)
# split the sentence in words
words = text.split()
#lenth of the words
print(f"Total words: {len(words)}")
# use the first 20 words
print(words[:20])

# clean them
cleaned_words = []
for word in words:
    cleaned = word.strip(string.punctuation).lower()
    if cleaned:
        cleaned_words.append(cleaned)
print(cleaned_words[:20])

#count
counts = {}
for word in cleaned_words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# sort and display
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print("\nTop 10 most common words:\n")
for word, count in sorted_counts[:10]:
    print(f"{word:15} {count}")

# the finished program
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: could not find '{filename}'")
        return None

def clean_words(text):
    words = text.split()
    cleaned = []
    for word in words:
        word = word.strip(string.punctuation).loweer()
        if word:
            cleaned.appen(word)
    return cleaned

def count_words(words):
    counts= {}
    for word in words:
        counts[word] = counts.get(word, 0) +1
    return counts

def show_results(counts, top_n=10):
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse = True)
    print(f"\nTotal unique words: {len(counts)}")
    print(f"\nTop {top_n} most common words:\n")
    for word, count in sorted_counts[:top_n]:
        print(f"{word:15} {count}")

def main():
    filename = input("Enter the filename: ")

    text = read_file(filename)
    if text is None:
        return

    words = clean_words(text)
    print(f"\nTotal words: {len(words)}")

    counts = count_words(words)
    show_results(counts)

main()
