import sys

class BookAnalyzer:
    def __init__(self, filepath):
        self.filename = filepath
        self.book_name = filepath.split("/")[-1].split(".")[0]
        with open(self.filename) as f:
            self.text = f.read()
        self.character_dict = {}
        print(f"--- Begin report of {self.filename} ---")

    def file_contents(self):
        return self.text

    def count_words(self):
        word_count = 0
        text = self.text
        words = text.split()
        word_count = len(words)
        print (f"\n{word_count} words were found in the document")
        return word_count
    
    def count_characters(self):
        for character in self.text.lower():
            if character not in self.character_dict:
                self.character_dict[character] = 1
            else:
                self.character_dict[character] += 1
        return self.character_dict
    
    def alphabet_only(self):
        alpha_dict = {}
        for char in self.character_dict:
            if char.isalpha():
                alpha_dict[char] = self.character_dict[char]
        for key in sorted(alpha_dict, key=lambda x: alpha_dict[x], reverse=True):
            if alpha_dict[key] == 1:
                print(f"{key}: {alpha_dict[key]}")
            else:
                print(f"{key}: {alpha_dict[key]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print("\nTry 'books/[book_name].txt' for example")
        sys.exit(1)

    book_analyzer = BookAnalyzer(sys.argv[1])
    print(f"{book_analyzer.count_words(book_analyzer.text)} words found in the document")
    book_analyzer.count_characters()
    book_analyzer.alphabet_only()
    print(f"--- End report ---")

if __name__ == "__main__":
    main()
