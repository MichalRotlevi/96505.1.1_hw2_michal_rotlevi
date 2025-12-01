def partition_lomuto(a, key):
    pivot = a[-1]
    print("pivot value:",pivot)
    i = 0
    for j in range(len(a) - 1):
        if key(a[j]) <= key(pivot):
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[-1] = a[-1], a[i]
    return i

def partition_hoare(a, key):
    pivot = a[0]
    print("pivot value:",pivot)
    i = -1
    j = len(a)
    while True:
        while True:
            i += 1
            if key(a[i]) >= key(pivot):
                break
        while True:
            j -= 1
            if key(a[j]) <= key(pivot):
                break
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

a = [7, 2, 11, 9, 1, 5]
print("lomuto")
print("brfor partition:", a)
idx = partition_lomuto(a, key=lambda x: x)
print("pivot index:", idx)
print("after partition:", a , "\n")


a = [7, 2, 11, 9, 1, 5]
print("hoare")
print("before partition:", a)
idx = partition_hoare(a, key=lambda x: x)
print("pivot index:", idx)
print("after partition:", a)




#lomuto
#brfor partition: [7, 2, 11, 9, 1, 5]
#pivot value: 5
#pivot index: 2
#after partition: [2, 1, 5, 9, 7, 11] 
#
#hoare
#before partition: [7, 2, 11, 9, 1, 5]
#pivot value: 7
#pivot index: 2
#after partition: [5, 2, 1, 9, 11, 7]