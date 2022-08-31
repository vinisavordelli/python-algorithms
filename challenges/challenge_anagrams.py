def str_sort(str):
    strLen = len(str)

    for index in range(strLen - 1):
        for search_index in range(strLen - 1 - index):
            if str[search_index] > str[search_index + 1]:
                current_element = str[search_index]
                str[search_index] = str[search_index + 1]
                str[search_index + 1] = current_element
    return str


def is_anagram(first_string, second_string):
    order_fisrt_string = str_sort(list(first_string.lower()))
    order_second_string = str_sort(list(second_string.lower()))

    if order_fisrt_string == order_second_string:
        return True
    return False
