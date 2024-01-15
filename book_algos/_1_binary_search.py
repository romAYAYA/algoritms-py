def binary_search(sorted_list: list, item: int) -> int | None:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        print('mid: ', mid)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            print('high: ', high)
        else:
            low = mid + 1
            print('low: ', low)
    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
