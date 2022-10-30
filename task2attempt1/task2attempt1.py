def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}
    for i in str_:
        if i.isalpha() and i not in dict_:
            dict_[i] = str_.count(i)
    return dict_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
def get_count(dict_):
    new_dict_ = {}


