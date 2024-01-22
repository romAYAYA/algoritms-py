# def arr_search(a: list, n: int, x: int):
#     """makes search int x in list a from 0 including n-1.
#     returns index element x in list a.
#     or -1 if there is not such element.
#     if there are multiple same elements, return index of the first found element
#     """
#     for k in range(n):
#         if a[k] == x:
#             return k
#     return -1
#
#
# def test_arr_search():
#     a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     m = arr_search(a1, 5, 10)
#     if m == -1:
#         print('#test1 - ok')
#     else:
#         print('#test1 - failed')
#
#     a2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
#     m = arr_search(a2, 5, -3)
#     if m == 2:
#         print('#test2 - ok')
#     else:
#         print('#test2 - failed')
#
#     a3 = [10, 20, 20, 10, 20, 30]
#     m = arr_search(a3, 5, -3)
#     if m == 0:
#         print('#test3 - ok')
#     else:
#         print('#test3 - failed')
#
#
# test_arr_search()

# def invert_arr(x: list) -> list:
#     for i in range(len(x) // 2):
#         x[i], x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
#     return x
#
#
# print(invert_arr([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# TODO Решето Эратосфена

# N = 23
# A = [True] * N
# A[0] = A[1] = False
#
# for k in range(2, N):
#     if A[k]:
#         for m in range(2 * k, N, k):
#             A[m] = False
#
# for i in range(N):
#     print(i, '-', 'prime' if A[i] else 'composite')


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = []

for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i] ** 2)

print(B)

C = [x ** 2 for x in A if x % 2 == 0]
print(C)
