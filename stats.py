def get_num_words(text):
    word_count = len(text.split())
    return word_count

def character_counter(text):
    counter = {

    }
    for character in text.lower():
        if character in counter:
            counter[f"{character}"] += 1
        else:
            counter[f"{character}"] = 1
    return counter

def sort_on(counter):
    return counter["num"]

def sorted_characters(counter):
    final_sort = []
    for letter in counter:
        if f"{letter}".isalpha():
            new_dictionary = {"name": f"{letter}", "num": counter[letter]}
            final_sort.append(new_dictionary)
    final_sort.sort(reverse=True, key=sort_on)
    return final_sort