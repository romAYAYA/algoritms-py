# TODO task 1
# Найти самый часто встречающийся символ в строке. Если нескольком символов встречаются одинаково часто, то можно вывести любой


# TODO decision 1:
# Что-то на питоновском
# s = input()
# print(max(map(lambda x: (s.count(x), x), s))[1])

# TODO decision 2 O(n^2):
# s = input()
# ans = ''
# anscnt = 0
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
#
# print(ans)

# TODO decision 2 O(n*k):

# s = input()
# ans = ''
# anscnt = 0
#
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
#
# print(ans)

# TODO decision 3 O(n + k) = O(n):

# s = input()
# ans = ''
# anscnt = 0
# s_dict = {}
#
# for now in s:
#     if now not in s_dict:
#         s_dict[now] = 0
#     s_dict[now] += 1
#
# for key in s_dict:
#     if s_dict[key] > anscnt:
#         anscnt = s_dict[key]
#         ans = key
#
# print(ans)

# s = input()
# ans = ''
# anscnt = 0
# symcnt = {}
#
# for now in s:
#     if now not in symcnt:
#         symcnt[now] = 0
#     symcnt[now] += 1
#     if symcnt[now] > anscnt:
#         ans = now
#         anscnt = symcnt[now]
#
# print(ans)

# TODO task 2
# Сумма последовательности

# TODO decision 1

# seq = list(map(int, input().split()))
# if len(seq) == 0:
#     print(0)
# else:
#     seqsum = seq[0]
#     for i in range(1, len(seq)):
#         seqsum += seq[i]
#     print(seqsum)

# TODO decision 2

# seq = list(map(int, input().split()))
# seqsum = 0
#
# for i in range(1, len(seq)):
#     seqsum += seq[i]
#     print(seq[i])
#
# print(seqsum)


# TODO Максимум последовательности

# TODO decision 1:

# seq = list(map(int, input().split()))
# seqmax = 0
#
# for i in range(len(seq)):
#     if seq[i] > seqmax:
#         seqmax = seq[i]
#
# print(seqmax)

# TODO decision 2:

# seq = list(map(int, input().split()))
#
# if len(seq) == 0:
#     print('-inf')
# else:
#     seqmax = seq[0]
#     for i in range(len(seq)):
#         if seq[i] > seqmax:
#             seqmax = seq[i]
#
#     print(seqmax)


# Что тестировать?
# TODO Тесты из условия (если таковые имеются)
# TODO Общие случаи
# TODO Особые случаи

# 1. Если есть примеры - можно решить их руками и сверить ответ. Если не совпадает, то либо правильных ответов несколько,
# либо неправильно понята задача
#
# 2. Сначала нужно составить несколько примеров и решить задачу руками, чтобы лучше понять условие и чтобы потом было
# с чем сравнивать
#
# 3. Проверить последовательность из одного элемента и пустую последовательность
#
# 4. "Краевые эффекты" - проверить, что программа работает корректно в начале и конце последовательности
#
# 5. Составить покрытие всех ветвлений так, чтобы был тест, который входит в каждый if и else
#
# 6. Подобрать тесты, чтобы не было ни одного входа в цикл
#
# 7. Один тест - одна возможная ошибка

# TODO task 3
# Даны три целых числа a, b, c
# Найти все корни уравнения ax^2+bx+c=0
# и вывести их в порядке возрастания

# TODO decision 1

# import math
#
# a = -5
# b = 4
# c = 1
#
# if a == 0:
#     if b != 0:
#         print(-c / b)
#     elif b == 0 and c == 0:
#         print('Infinite number of solutions')
# else:
#     d = b ** 2 - 4 * a * c
#     if d >= 0:
#         x1 = (-b - math.sqrt(d)) / (2 * a)
#         x2 = (-b + math.sqrt(d)) / (2 * a)
#
#         if x1 == x2:
#             print("One solution:", x1)
#         else:
#             print("Two solutions:", x1, x2)
#     else:
#         print("No real solutions")
