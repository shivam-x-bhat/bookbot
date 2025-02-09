def main():
    book_path = "books/frankenstein.txt"

    book_contents = get_book_contents(book_path)    
    book_contents = book_contents.lower()


    word_count = get_word_count(book_contents)    

    character_count = get_character_count(book_contents)

    # Getting the alphabets count only
    alphabet_count = get_alphabet_count(character_count)

    # Sorting the alphabets on desceding values of appearance
    sorted_alpha_count = dict(sorted(alphabet_count.items(), key=lambda item: item[1], reverse=True)) 


    # Printing the final report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for char in sorted_alpha_count:
        print(f"The '{char}' character was found {sorted_alpha_count[char]} times")

    print("--- End report ---") 



# Getting contents out from the book
def get_book_contents(path):
    with open(path) as f:

        return f.read()

# Getting the number of words out of the book
def get_word_count(text):
    words = text.split()
    return len(words)

# Getting the count of each character inclusing whitespaces
# and special characters
def get_character_count(text):
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def get_alphabet_count(dict):
        alphabet_count = {}
        for char in dict:
            if char.isalpha():
                alphabet_count[char] = dict[char]
        return alphabet_count

main()