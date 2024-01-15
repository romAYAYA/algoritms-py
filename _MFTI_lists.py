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
