from string import ascii_lowercase

def main():
    book = "frankenstein"
    path = f"./books/{book}.txt"
    with open(path, "r") as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words found in document.")
    print()
    letter_frequency = count_letters(file_contents)
    for c in letter_frequency:
        print(f"The '{c['char']}' character was found {c['num']} times.")
    return

def count_words(string):
    return len(string.split())

def count_letters(string):
    lowercase_string = string.lower()
    string_letter_frequency = dict()
    for c in lowercase_string:
        if c in ascii_lowercase:
            if c in string_letter_frequency.keys():
                string_letter_frequency[c] += 1
            else:
                string_letter_frequency[c] = 1
    string_letter_frequency = [{"char": k, "num": string_letter_frequency[k]} for k in string_letter_frequency.keys()]
    string_letter_frequency.sort(reverse=True, key=sort_on)
    return string_letter_frequency

def sort_on(dict):
    return dict["num"]

main()