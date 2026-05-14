import merge as m

def merge_sort(numbers, low, high):
    
    if low < high:

        mid = (low + high) // 2

        merge_sort(numbers, low, mid) # for left half
        merge_sort(numbers, mid + 1, high) # for right half
        m.merge(numbers, low, high, mid) # merging the sorted arrays)
    return numbers