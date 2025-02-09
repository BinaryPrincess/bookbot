def file_contents():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        for contents in f:
            words = contents.split()
            for word in words:
                word_count += 1
    print (word_count)

def main():
    file_contents()
    count_words()
if __name__ == "__main__":
    main()
