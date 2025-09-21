import sys
from stats import get_num_words, num_char, sorted_char_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    result = ""
    with open(filepath) as f:
        result = f.read()
    return result

def main(path):
    result = get_book_text(path)
    return result

book_string = main(filepath)
num_words = get_num_words(book_string)

char_dict = num_char(book_string)

final_list = sorted_char_list(char_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for item in final_list:
    print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")