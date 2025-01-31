"""Actividad 4.2 - Problema 3"""
import sys
import time


def word_count(file_paths):
    """
    Count the frequency of each distinct word in the given files.

    Args:
        file_paths (list): List of file paths to process.

    Returns:
        dict: Dictionary with words as keys and their frequencies as values.
    """
    word_freq = {}

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except ImportError as e:
            print(f"Error reading file {file_path}: {e}")
            continue

        word = ""
        for char in text:
            if char.isalnum():
                word += char.lower()
            else:
                if word:
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1
                    word = ""
        if word:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq


def save_results(word_freq, el_time):
    """
    Save the word frequency results and elapsed time to a file and print them.

    Args:
        word_freq (dict): Dictionary with words as keys and their frequencies as values.
        el_time (float): Time elapsed during the execution.
    """
    with open('WordCountResults.txt', 'w', encoding='utf-8') as result_file:
        for word, freq in sorted(word_freq.items()):
            result_file.write(f"{word}: {freq}\n")
            print(f"{word}: {freq}")
        result_file.write(f"\nTime elapsed: {time} seconds\n")
    print(f"\nTime elapsed: {el_time} seconds")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file_path1> <file_path2> ...")
        sys.exit(1)

    start_time = time.time()
    word_frequencies = word_count(sys.argv[1:])
    end_time = time.time()

    elapsed_time = end_time - start_time
    save_results(word_frequencies, elapsed_time)
