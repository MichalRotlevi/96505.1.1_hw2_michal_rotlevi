from itertools import pairwise

def is_sorted(a, key):
    for x, y in pairwise(a):
        if key(x) > key(y):
            return False
    return True

def merge(a, b, key):
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

#for checks.. sorted
a = [(1, 5), (3, 7), (5, 2)]
b = [(2, 6), (4, 1)]
merged = merge(a,b,
               key=lambda x: x[0])
print("sorted:\n" + str(merged))

#for checks.. not sorted
a = [(1, 5), (9, 7), (5, 2)]
b = [(2, 6), (4, 1)]
merged = merge(a,b,
               key=lambda x: x[0])
print("not sorted:\n" + str(merged))
