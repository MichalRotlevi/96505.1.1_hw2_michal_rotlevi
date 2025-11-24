def merge(a, b, key):
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

a = [(1, 5), (3, 7), (5, 2)]
b = [(2, 6), (4, 1)]

#for checks..
merged = merge(sorted(a, key=lambda x: x[0]),
               sorted(b, key=lambda x: x[0]),
               key=lambda x: x[0])
print(merged)
