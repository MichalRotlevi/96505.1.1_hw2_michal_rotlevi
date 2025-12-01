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

def merge_sorted_lists(lists, key):
    if not lists:
        return []
    merged = lists[0]
    for lst in lists[1:]:
        merged = merge(merged, lst, key)
        if merged is None:
            return None
    return merged

a = [(1, 5), (3, 7)]
b = [(2, 6), (4, 1)]
c = [(0, 9), (5, 2)]
lists_sorted = [a, b, c]
merged_sorted = merge_sorted_lists(lists_sorted, key=lambda x: x[0])
print("Merged sorted lists:", merged_sorted)

d = [(3, 5), (1, 7)]
lists_unsorted = [a, d, c]
merged_unsorted = merge_sorted_lists(lists_unsorted, key=lambda x: x[0])
print("Merged with unsorted list:", merged_unsorted)
