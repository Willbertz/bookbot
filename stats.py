def get_num_words(book_string):
    num_words = len(book_string.split())
    return num_words

def num_char(book_string):
    char_dict = {}
    for char in book_string.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_char_list(char_dict):
    new_list = []
    for ch in char_dict:
        item = {"char": ch, "num": char_dict[ch]}
        if ch.isalpha():
            new_list.append(item)
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(item):
    return item["num"]