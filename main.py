def main():
    text = set_file("books/frankenstein.txt")
    number_of_characters = character_counter(text)
    make_report(number_of_characters, text)

def set_file(path_to_file):
    with open(path_to_file) as f:
        file = f.read()
    return file    

def print_book(text):
    print(text)

def word_counter(text):
    words = text.split()
    return len(words) 

def character_counter(text):
    number_of_characters = {}
    words = text.lower()
    for word in words:
        for char in word:
            if char in number_of_characters:
                number_of_characters[char] += 1
            else:
                number_of_characters[char] = 1
    return number_of_characters

def make_report(number_of_characters, text):
    list_of_characters = []
    for character in number_of_characters:
        if character.isalpha():
            list_of_characters.append({
                "character": character,
                "num": number_of_characters[character]})
    list_of_characters.sort(reverse=True, key=sort_on)
    print_report(text, list_of_characters)    
    

def sort_on(dict):
    return dict["num"]   

def print_report(text, list_of_characters):
    print(f"--- Begin report of books/frankenstein.txt ---") 
    print(f"{word_counter(text)} words found in the document")
    print()
    for character in list_of_characters:
        print(f"The '{character['character']}' character was found {character['num']} times")
    print("--- End report ---")    

main()
