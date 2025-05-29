# Нужны
# add with key
# delete with key
# check for key
# edit with key
#
#
#


# class SimpleDict():
#     items = list()
#
#     def key_index(self, _key):
#         for key in self.items.:
#             if key[0] == _key:
#                 return
#
#     def add_item(self, _key, value):
#         pass


def quest_1():
    main_list = [10, -3, 4, 1, 0, -15]

    print(main_list)

    main_list.sort()
    print(f'По возростанию {main_list}')
    main_list.sort(reverse=True)
    print(f'По убыванию {main_list}')
    main_list.sort(key=lambda x: abs(x), reverse=False)
    print(f'По модулю числа {main_list}')


# quest_1()

def quest_2():
    main_list = ["книга", "стол", "ручка", "дом"]

    main_list.sort()
    print(f'В алфавитном порядке {main_list}')

    main_list.sort(key=lambda x: len(x), reverse=False)
    print(f'В алфавитном порядке {main_list}')

    main_list.sort(reverse=True)
    print(f'В алфавитном порядке {main_list}')


# quest_2()

def quest_3():
    main_list = [("Маша", 24), ("Саша", 19), ("Даша", 21)]

    main_list.sort(key=lambda x: x[0], reverse=False)
    print(f'По имени в алфавитном порядке {main_list}')

    main_list.sort(key=lambda x: x[1], reverse=False)
    print(f'По возрасту от младшего к старшему {main_list}')

    main_list.sort(key=lambda x: x[1], reverse=True)
    print(f'По возрасту от старшего к младшему {main_list}')


# quest_3()

def quest_4():
    students = [
        {"name": "Алексей", "grades": [5, 4, 3]},
        {"name": "Мария", "grades": [4, 4, 5]},
        {"name": "Иван", "grades": [2, 5, 4]}
    ]

    students.sort(key=lambda x: sum(x['grades']) / len(x['grades']), reverse=False)
    print(f'По среднему балу {students}')

    students.sort(key=lambda x: x['name'], reverse=True)
    print(f'По имени в обратном порядке {students}')

quest_4()