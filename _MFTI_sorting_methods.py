def insert_sort(a):
    for top in range(1, len(a)):
        while top > 0 and a[top - 1] > a[top]:
            a[top], a[top - 1] = a[top - 1], a[top]
            top -= 1


def choice_sort(a):
    for pos in range(0, len(a)-1):
        for k in range(pos + 1, len(a)):
            if a[pos] > a[k]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def test_sort(sort_algorithm):
    a = [3, 2, 4, 5, 1]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('case 1: ')
    sort_algorithm(a)
    print('Test passed' if a == a_sorted else 'Test failed')

    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    print('case 2: ')
    sort_algorithm(a)
    print('Test passed' if a == a_sorted else 'Test failed')

    a = [4, 2, 2, 3, 5, 1]
    a_sorted = [1, 2, 2, 3, 4, 5]
    print('case 3: ')
    sort_algorithm(a)
    print('Test passed' if a == a_sorted else 'Test failed')


if __name__ == '__main__':
    print('insert_sort: ')
    test_sort(insert_sort)
    print('choice_sort: ')
    test_sort(choice_sort)
    print('bubble_sort: ')
    test_sort(bubble_sort)
