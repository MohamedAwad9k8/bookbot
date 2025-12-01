def get_word_count(content):
    words_list = content.split()
    return len(words_list)

def count_chars(content):
    content = content.lower()
    chars_count_dict = {}
    for char in content:
        if char in chars_count_dict:
            chars_count_dict[char] += 1
        else:
            chars_count_dict[char] = 1
    return chars_count_dict

def sort_output(chars_dict):
    list_of_dicts = []
    for key, value in chars_dict.items():
        new_dict = {"char":key, "num":value}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(key=lambda char_dict : char_dict["num"], reverse=True)
    return list_of_dicts
