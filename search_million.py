#Instead of using a simple linear search (O(N)), we can use Exponential Search(O(log N)) followed by Binary Search O(log N), which is much faster.
def find_integer_in_stream(stream, target):
    # Step 1: Find an appropriate range using exponential search
    index = 1
    while index < len(stream) and stream[index] < target:
        index *= 2  # Double the step size

    # Step 2: Apply binary search within the found range
    left, right = index // 2, min(index, len(stream) - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if stream[mid] == target:
            return mid  # Found the target
        elif stream[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

# Example Usage
stream = list(range(1, 10000000, 2))  # Sorted stream (odd numbers)
target = 999999
print(find_integer_in_stream(stream, target))  # Returns the index of target
