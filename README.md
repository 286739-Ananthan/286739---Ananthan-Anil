# Strops: Python String Operations Module

**Strops** is a Python module that provides various string manipulation functions. This module allows you to easily perform operations like finding substring spans, reversing words, removing punctuation, and more.

## Features

The following functions are available in the `strops` module:

1. **getspan(s, ss)**: Returns the start and end index (span) of substring `ss` in string `s`.
2. **reverseWords(s)**: Reverses the order of words in `s`.
3. **removePunctuation(s)**: Removes all punctuation from `s`.
4. **countWords(s)**: Counts the number of words in `s`.
5. **characterMap(s)**: Returns a dictionary with characters of `s` as keys and their frequencies as values.
6. **makeTitle(s)**: Converts `s` to title case.
7. **normalizeSpaces(s)**: Removes extra spaces, leaving only single spaces between words.
8. **transform(s)**: Reverses the string and swaps case.
9. **getPermutations(s)**: Returns all permutations of the string `s`.

## Installation

You can install the `strops` module in your Python environment using the following steps:

1. Clone this repository or download the source code.
2. Set up a **virtual environment** (optional but recommended).
   ```bash
   python -m venv venv
