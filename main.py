from stats import character_counter, word_counter
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]    
        text = set_file(book)
        number_of_characters = character_counter(text)
        make_report(number_of_characters, text, book)

def set_file(path_to_file):
    with open(path_to_file) as f:
        file = f.read()
    return file    

def print_book(text):
    print(text)

def make_report(number_of_characters, text, book):
    list_of_characters = []
    for character in number_of_characters:
        if character.isalpha():
            list_of_characters.append({
                "character": character,
                "num": number_of_characters[character]})
    list_of_characters.sort(reverse=True, key=sort_on)
    print_report(text, book, list_of_characters)    
    
def sort_on(dict):
    return dict["num"]   

def print_report(text, book, list_of_characters):
    print(f"--- Begin report of {book} ---") 
    print(f"{word_counter(text)} words found in the document")
    print()
    for character in list_of_characters:
        print(f"'{character['character']}: {character['num']}'")
    print("--- End report ---")    

main()
