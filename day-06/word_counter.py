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