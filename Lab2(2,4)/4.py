import os
import re

def get_data(file_name):
    if os.path.exists(os.getcwd() + '\\' + file_name):
        with open(file_name) as file:
            text = [i for i in file]
        return text


def get_substr(text, reg):
    for i in range(len(text)):
        count = 0
        substr = re.search(reg, text[i])

        while substr != None:
            yield i + 1, substr.string
            count += substr.regs[0][1]
            text[i] = text[i][substr.regs[0][1]:]
            substr = re.search(reg, text[i])


def search_type():
    reg = r'(int|short|byte) \w+ = \d+'
    reg_num = r'\+38071\d{7}'
    output_text = 'Строка №{0} : {1}'
    input_text = get_data(input('Введите название файла: '))
    for index, substr in get_substr(input_text, reg):
        print(output_text.format(index, substr))
    for index, substr in get_substr(input_text, reg_num):
        print(output_text.format(index, substr))

search_type()