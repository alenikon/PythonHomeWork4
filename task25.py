# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

chars = input().split()
dict_chars = {}.fromkeys(chars, 0)
print(dict_chars)
for i in chars:
    print(f"{i}_{dict_chars[i]}" if dict_chars[i] else i, end=" ")
    dict_chars[i] += 1

# s = ('a a a b c a a d c d d')
# print(s)
# s_array = s.split()
# print(s_array)
# kol = s_array[0]
# count = 0
# i=1
# for i in range (len(s_array)):
#     if kol == s_array[i]:
#         count += 1
#         s_array[i] += (f'_{count}')
#     else: 
# #        s_array[i-1] += (f'_{count}')
#         count = 1
#         kol = s_array[i]
# print(s_array)
