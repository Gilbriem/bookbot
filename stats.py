def count_words(file_path):
    with open(file_path) as f:
        text = f.read()
    word_count = len(text.split())
    return word_count

def char_stats(file_path):
    with open(file_path) as f:
        text = f.read()
    l_text = text.lower()
    #print(l_text)
    chr_dict = {}
    for chr in l_text:
        if chr in chr_dict:
            chr_dict[chr] += 1
        else:
            chr_dict[chr] = 1
    return chr_dict


def convert_dict_to_list_of_dicts(char_count_dict):
    result = []
    for char, count in char_count_dict.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)
    result.sort(reverse=True, key=sort_on)    
    return result

def sort_on(dict):
    return dict["count"]
