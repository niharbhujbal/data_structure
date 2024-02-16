def bubble_sort(array):
    """
    Bubble sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    for n in range(len(array) - 1, 0, -1):
        is_sorted = True
        for i in range(n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        if is_sorted:
            return array

    return array


def selection_sort(array):
    """
    Selection sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_pointer = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def insertion_sort(array):
    """
    Insertion sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0:
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                j -= 1
                i -= 1
            else:
                break
    return array


def merge_sort(array):
    """
    Merge sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    middle_pointer = len(array) // 2
    if middle_pointer > 0:
        left_array, right_array = array[:middle_pointer], array[middle_pointer:]
        # sort each array
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        # now merge the array
        merged_array = []
        i = 0
        j = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                merged_array.append(left_array[i])
                i += 1
            elif left_array[i] > right_array[j]:
                merged_array.append(right_array[j])
                j += 1

        while i < len(left_array):
            merged_array.append(left_array[i])
            i += 1

        while j < len(right_array):
            merged_array.append(right_array[j])
            j += 1
        return merged_array
    else:
        return array


def _partition(array, start, end):
    """
    Private method for quick sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    start: int
        start index
    end: int
        end index
    -------------
    Returns
    -------------
    bounday: int
        boundary index
    """
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[end]) = (array[end], array[i + 1])
    return i + 1


def quick_sort(array, start=0, end=-1):
    """
    Quick sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    start: int
        start index
    end: int
        end index
    -------------
    Returns
    -------------
    array : list
        sorted list
    """

    if end == -1:
        end = len(array) - 1

    if start < end:
        boundary = _partition(array, start, end)
        quick_sort(array, start, boundary - 1)
        quick_sort(array, boundary + 1, end)
    return array


def counting_sort(array, max):
    """
    Counting sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    max : int
        maximum number in array
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    counter = {}
    for i in array:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 0

    k = 0
    for i in range(max):
        if i in counter.keys():
            array[k] = i
            counter[i] -= 1
            if counter[i] == 0:
                del counter[i]
            k += 1
    return array


def bucket_sort(array, no_of_buckets):
    """
    Bucket sort algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    no_of_buckets : int
        number of buckets
    -------------
    Returns
    -------------
    array : list
        sorted list
    """
    buckets = {}
    for i in range(no_of_buckets):
        buckets[i] = []
    for i in array:
        bucket_no = i // no_of_buckets
        buckets[bucket_no].append(i)

    sorted_array = []
    for i in range(no_of_buckets):
        sorted_array.extend(sorted(buckets[i]))
    return sorted_array


def linear_search(array, item):
    """
    Linear search algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    item : int
        item to search
    -------------
    Returns
    -------------
    index : int
        index of item in array
        returns -1 if item is not found in array
    """
    for index, array_item in enumerate(array):
        if item == array_item:
            return index
    else:
        return -1


def binary_search(array, item, start=0, end=-1):
    """
    Binary search algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    item : int
        item to search
    start : int
        start index
    end : int
        end index
    -------------
    Returns
    -------------
    index : int
        index of item in array
        returns -1 if item is not found in array
    """
    # array has to be sorted
    if end == -1:
        end = len(array)
    if start >= end:
        return -1

    middle = (start + end) // 2
    if item == array[middle - start]:
        return middle
    elif item < array[middle - start]:
        return binary_search(array[:middle], item, start, middle)
    elif item > array[middle - start]:
        return binary_search(array[middle + 1 :], item, middle + 1, end)


def ternary_search(array, item, start=0, end=-1):
    """
    Ternary search algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    item : int
        item to search
    start : int
        start index
    end : int
        end index
    -------------
    Returns
    -------------
    index : int
        index of item in array
        returns -1 if item is not found in array
    """
    # array has to be sorted
    if end == -1:
        end = len(array)
    if start >= end:
        return -1

    partition = (end - start) // 3
    mid1 = start + partition
    mid2 = end - partition
    if item == array[mid1 - start]:
        return mid1
    if item == array[mid2 - start]:
        return mid2
    if item < array[mid1 - start]:
        return ternary_search(array[:mid1], item, start, mid1)
    if item > array[mid1 - start] and item < array[mid2 - start]:
        return ternary_search(array[mid1 + 1 : mid2], item, mid1 + 1, end)
    if item > array[mid2 - start]:
        return ternary_search(array[mid2 + 1 :], item, mid2 + 1, end)


def jump_search(array, target):
    """
    Jump search algorithm
    -------------
    Parameters
    -------------
    array : list
        list of numbers
    target : int
        target number
    -------------
    Returns
    -------------
    index : int
        index of target number in array
        returns -1 if target is not found in array
    """
    block_size = int((len(array)) ** (1 / 2))
    start = 0
    next = block_size

    # find the block
    while start < len(array) and array[next - 1] < target:
        start = next
        next += block_size
        if next > len(array):
            next = len(array)

    for i in range(start, next):
        if array[i] == target:
            return i
    else:
        return -1
