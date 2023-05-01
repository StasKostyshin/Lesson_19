import csv

# Напишите генератор, который на вход получает список чисел и возвращает только те числа,
# которые делятся на 3 без остатка.
# def number(a):
#     for i in a:
#         if i % 3 == 0:
#             yield i
#
# num = (a for a in range(1,30))
# numbers = number(num)
# for i in numbers:
#     print(i)
# Напишите итератор, который на вход получает строку и возвращает каждый второй символ этой строки.

# class String_iterator:
#     def __init__(self, string_):
#         self.string_ = string_
#
#     def __iter__(self):
#         print(self.string_[1::2])
#
# iter_str = String_iterator('rnjasdasddpwe')
# iter_str.__iter__()

# Напишите генератор, который на вход получает два списка чисел и возвращает только те числа, которые есть в обоих списках.

# def numbers_all(num_1,num_2):
#     for i in num_1:
#         if i in num_2:
#             yield i
#
# n_1 = (a for a in range(9,14))
# n_2 = (a for a in range(1,10))
# num = numbers_all(n_1, n_2)
# for i in num:
#     print(i)

# Напишите генератор, который на вход получает список строк и возвращает только те строки, которые содержат букву "a".
# def string_(str_):
#     for i in str_:
#         if 'а' in i:
#             yield i
#
# list_str = ["пасха", "прошла", "ждём", "майские", "праздники"]
# for i in string_(list_str):
#     print(i)

# Напишите итератор, который на вход получает список чисел и возвращает каждый третий элемент этого списка.
# class numbers_3:
#     def __init__(self,list_num):
#         self.list_num = list_num
#
#     def __iter__(self):
#         self.ind = 2
#         return self
#
#     def __next__(self):
#         if self.ind < len(self.list_num):
#             i = self.list_num[self.ind]
#             self.ind += 3
#             return i
#         else:
#             raise StopIteration
#
# list_num = [1,2,3,4,5,6,7,8,9,0,0,8,1]
# run = numbers_3(list_num)
#
# for i in run:
#     print(i)

# Реализуйте итератор колоды карт (52 штуки) CardDec. Каждая карта представлена в виде строки типа "2 Пик".
# При вызове функции next() будет представлена следующая карта. По окончании перебора всех элементов возникнет
# ошибка StopIteration

class Carsd:
    def __init__(self, list_card):
        self.list = list_card

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list):
            i = self.list[self.index]
            self.index += 1
            return i
        else:
            raise StopIteration


cards = []

with open('file.csv', 'r', newline='', encoding='UTF-8') as sh_c:
    card = csv.reader(sh_c)
    for row in card:
        for i in row:
            cards.append(i)

start = iter(Carsd(cards))
print(next(start))













