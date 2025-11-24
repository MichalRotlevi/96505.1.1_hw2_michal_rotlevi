def create_random_tuples(n, k, types=None):
    """
    Create a list of n tuples, each containing k random elements of specified types.

    Parameters:
    n (int): Number of tuples to create.
    k (int): Number of elements in each tuple.
    types (list): List of types for each element in the tuple. Length must be k.

    Returns:
    list: A list of n tuples with random elements.
    """
    import random
    import string

    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result


    
# יוצרים רשימה של 10 tuples עם טיפוסים [int, float, str]
data = create_random_tuples(10, 3, [int, float, str])

print("Original list:")
for item in data:
    print(item)

# מיון לפי הרכיב הראשון (int)
sorted_by_first = sorted(data, key=lambda x: x[0])
print("\nSorted by first element (int):")
for item in sorted_by_first:
    print(item)

# מיון לפי הרכיב השני (float)
sorted_by_second = sorted(data, key=lambda x: x[1])
print("\nSorted by second element (float):")
for item in sorted_by_second:
    print(item)

# מיון לפי הרכיב השלישי (str)
sorted_by_third = sorted(data, key=lambda x: x[2])
print("\nSorted by third element (str):")
for item in sorted_by_third:
    print(item)
