"""
binary search
"""
array = []

for i in range(1, 10001):
    array.append(i)

def linear_search(arr, value):
    """searching value
    Args:
        arr (_int_): _description_
        value (_int_): _description_

    Returns:
        _int_: _description_
    """
    count = 0
    for element in arr:
        count += 1
        if element == value:
            return count
    return None

def binary_search(arr, value):
    """_summary_

    Args:
        arr (_type_): _description_
        value (_type_): _description_
    """
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == value:
            return count
        if guess > value:
            high = mid - 1
        if guess < value:
            low = mid + 1
    return None

def interpolar_search(arr, value):
    """_summary_

    Args:
        arr (_type_): _description_
        value (_type_): _description_
    """
    low = 0
    high = len(arr) - 1
    count = 0
    
    while value >= array[low] and value <= high and low <= high:
        count += 1
        probe = int(low + (high - low) * (value - arr[low]) / (arr[high] - arr[low]))
        if arr[probe] == value:
            return count
        elif arr[probe] > value:
            high = probe - 1
        else:
            low = probe + 1
    return -1

print(f"Linear search: {linear_search(array, value=8562)}")
print(f"Binary search: {binary_search(array, value=8562)}")
print(f"Interpolar search: {interpolar_search(array, value=8562)}")
