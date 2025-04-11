def word_count(text):
    return len(text.split())

def char_count(text):
    char_counts = {}
    words = text.split()
    for word in words:
        for char in word:
            char_low = char.lower()
            if char_low in char_counts:
                char_counts[char_low] += 1
            else:
                char_counts[char_low] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_count_dict):
    sorted_count = []
    for char, count in char_count_dict.items():
        sorted_count.append({"char": char, "count": count})
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count



