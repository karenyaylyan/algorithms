lst_search = list(map(int, input().split()))[1:]
lst_numbers = list(map(int, input().split()))[1:]

def binary_search(lst, number):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if number == lst[m]:
            return m + 1
        elif number < lst[m]:
            r = m - 1
        else:
            l = m + 1

    return -1

for number in lst_numbers:
    print(binary_search(lst_search, number), end=' ')
