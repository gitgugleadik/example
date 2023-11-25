#https://habr.com/ru/companies/vdsina/articles/563432/
# from random import choice
#
# # https://proglib.io/p/project-list
# # Этот пример может печатать любую строку n раз без использования циклов Python.
#
# n=5
# string="Hello World "
# print(string * n)
#
# # Отработать с дебагом и научится вводить переменные в watch
# a=3
# b=4
# a, b = b, a
# print(a, b) # a= 4, b =3
#
#
# # Поиск подстроки
# programmers = ["I'm an expert Python Programmer",
#                "I'm an expert Javascript Programmer",
#                "I'm a professional Python Programmer"
#                "I'm a beginner C++ Programmer"
# ]
# # #method 1
# # for p in programmers:
# #     if p.find("Python"):
# #         print(p)
# # #method 2
# for p in programmers:
#     if "Python" in p:
#         print(p)
#
#
# # случайно выбрать из списка
# lion = ['dfr','ffg','ddd','vvv','rrr','eee','www','uuu','iii']
# dd=choice(lion)
# print(dd)
strr = 'la_gugl'
for code in strr:
     print(code, ord(code))