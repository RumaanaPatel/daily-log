# Word Frequency counter
    A python program that reads a text file and reports the most frequenty used words.

## What it does
    -Reads ay plain text file
    -cleans the text by removing punctuation and converting to lowercase 
    -Counts how many times each word appears
    -DIsplay the ten most common words, sorted by frequency

## How to run it
    1. Make sure Pythion 3 is installed
    2. Put your text file in the same folder
    3. Run:
```
python word_counter.py
```
    4. Enter the filename when prompted

# Example output
```
Total words: 847
Total unique words: 312

Top 10 most common words:
 the           52
 and           31
 to            24
 ```

 ## What I learned building this
    -Reading files safely with `with` and handling missing files
    -Cleaning text with `.struo()`, `.lower()` and `string.punctuation`
    -Using a dictionary to count occurrences
    -Sorting a dictionary by value using `sorted()` with a key functipon