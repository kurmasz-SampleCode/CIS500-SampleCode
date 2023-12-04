def merge(arr, left_array, right_array):
    left_pointer = right_pointer = result_pointer = 0

    while left_pointer < len(left_array) and right_pointer < len(right_array):
        if left_array[left_pointer] < right_array[right_pointer]:
            arr[result_pointer] = left_array[left_pointer]
            left_pointer += 1
        else:
            arr[result_pointer] = right_array[right_pointer]
            right_pointer += 1
        result_pointer += 1

    # Copy the remaining elements of left, if any
    while left_pointer < len(left_array):
        arr[result_pointer] = left_array[left_pointer]
        left_pointer += 1
        result_pointer += 1

    # Copy the remaining elements of right, if any
    while right_pointer < len(right_array):
        arr[result_pointer] = right_array[right_pointer]
        right_pointer += 1
        result_pointer += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)    


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
