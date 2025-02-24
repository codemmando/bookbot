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

def word_counter(text):
    words = text.split()
    return len(words) 