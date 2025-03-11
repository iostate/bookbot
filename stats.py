def get_word_count(string):
    words = string.split()
    num_words = len(words)

    return (f"Found {num_words} total words")

def sort_on(dict, key):
    return dict[key]
    

def get_sorted_char_count_dict(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
        
    sorted_items = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    sorted_char_count = [{"char": char, "count": count} for char, count in sorted_items]
    
    return sorted_char_count
    
    
