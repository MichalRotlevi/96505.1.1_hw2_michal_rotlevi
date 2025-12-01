def dual_pivot_partition(a, key):
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]  # ensure pivot1 <= pivot2

    pivot1 = a[0]
    pivot2 = a[-1]

    i = 1       # boundary for < pivot1
    j = 1       # current element
    k = len(a)-2  # boundary for > pivot2

    while j <= k:
        if key(a[j]) < key(pivot1):
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif key(a[j]) > key(pivot2):
            a[j], a[k] = a[k], a[j]
            k -= 1
        else:
            j += 1

    a[0], a[i-1] = a[i-1], a[0]
    a[-1], a[k+1] = a[k+1], a[-1]

    return i-1, k+1

# -----------------------
# Example usage:

arr = [4, 3, 8, 2, 5, 9, 1, 6, 7]
print("Before partition:", arr)

pivot1_idx, pivot2_idx = dual_pivot_partition(arr, key=lambda x: x)

print("After partition: ", arr)
print("a[] len:", len(arr))
print("Pivot1 index:", pivot1_idx)
print("Pivot2 index:", pivot2_idx)


#Before partition: [4, 3, 8, 2, 5, 9, 1, 6, 7]
#After partition:  [1, 3, 2, 4, 5, 6, 7, 8, 9]
#a[] len: 9
#Pivot1 index: 3
#Pivot2 index: 6
