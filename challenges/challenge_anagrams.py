def is_anagram(first_string, second_string):
    
    if len(first_string) != len(second_string):
        return False

    first_str_to_list = list(first_string.lower())
    sec_str_to_list = list(second_string.lower())

    for letter in first_str_to_list:
        if letter in sec_str_to_list:
            sec_str_to_list.remove(letter)
        else:
            return False
    return True
