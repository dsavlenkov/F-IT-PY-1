def get_count_char(str_):
    dict_ = {}
    str_clear = "".join(str_.lower().split())
    DEFAULT_COUNT = 0
    for char in str_clear:
        if char.isalpha():
            dict_[char] = dict_.get(char, DEFAULT_COUNT) + 1
    return dict_


def char_percentage(dict_):
    sum_ = 0
    for pair in dict_:
        sum_ += dict_[pair]
    for pair in dict_:
        dict_[pair] = round(dict_[pair] / sum_ * 100, 2)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(char_percentage(get_count_char(main_str)))
