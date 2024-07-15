def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while len(a) > 0:
        c.append(a[0])
        a.pop(0)
    while len(b) > 0:
        c.append(b[0])
        b.pop(0)
    return c


def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == "__main__":
    lst = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(lst))
