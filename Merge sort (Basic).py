# Merge sort is a recursive sort function. Merge sort function is O(n*logn).
def merge_sort(data):
    if len(data) == 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    result = []

    # The loop stops when either left or right becomes empty. With each iteration it puts the smallest item in result
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:  # If there are remaining items in left, put them in result.
        result += left
    if right:  # If there are remaining items in right, put them in result.
        result += right

    return result
