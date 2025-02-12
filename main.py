class BookAnalyzer:
    def __init__(self, filename, book_name):
        self.filename = filename
        self.book_name = book_name
        with open(self.filename) as f:
            self.text = f.read()
        self.character_dict = {}
        print(f"--- Begin report of {self.filename} ---")

    def file_contents(self):
        print(f"\n=== Contents of {self.book_name} ===")
        
        print(self.text)
        return self.text

    def count_words(self):
        word_count = 0
        text = self.text
        words = text.split()
        word_count = len(words)
        print (f"\n{word_count} words were found in the document")
        return word_count
    
    def count_characters(self):
        book_text = self.text
        lowered_string = book_text.lower()
        for character in lowered_string:
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
                print(f"The '{key}' character was found {alpha_dict[key]} time")
            else:
                print(f"The '{key}' character was found {alpha_dict[key]} times")
        

def main():
    frankenstein = BookAnalyzer("books/frankenstein.txt", "Frankenstein")
    frankenstein.count_words()
    frankenstein.count_characters()
    frankenstein.alphabet_only()
    print(f"--- End report ---")


if __name__ == "__main__":
    main()
