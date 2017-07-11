import operator

d = {
    1: 'hi',
    2: 'roses',
    3: 'bye',
}


def sort_by_key(d):
    return sorted(d)


def reverse_sort_by_key(d):
    return sorted(d.items(), reverse=True)


def sort_by_value(d):
    return sorted(d.items(), key=operator.itemgetter(1))


print(reverse_sort_by_key(d))
