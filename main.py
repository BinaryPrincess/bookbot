def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def count_words():
    word_count = 0
    words = []
    with open("books/frankenstein.txt") as f:
        for words in f:
            words = f.split()
            for word in words:
                word_count += 1
    print (word_count)
main()