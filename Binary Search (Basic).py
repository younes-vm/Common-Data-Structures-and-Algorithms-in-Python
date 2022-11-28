# Ah yes, the good old binary search.
# My implementation returns the index of the target. If you want to return True/False, just change line 9 and line 14
# to return False and True instead of -1 and mid_point respectively.
def binary_search(input_array, target, low=0, high=None):
    if high is None:
        high = len(input_array) - 1

    if low > high:      # If the target is not found, high will be less than low.
        return -1

    mid_point = (low + high) // 2

    if target == input_array[mid_point]:
        return mid_point
    elif target < input_array[mid_point]:
        return binary_search(input_array, target, low, mid_point - 1)
    else:
        return binary_search(input_array, target, mid_point + 1, high)
