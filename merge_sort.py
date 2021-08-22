# Merge sort is a divide and conquer algorithm
# 1. Split array in half
# 2. Call Merge sort on each half to sort them recursively
# 3. Merge both sorted halves into one sorted array

# First implementation
"""
def merge_sort(arr):
    if len(arr) >  1:
        # // is floor division in python - it rounds the result to the nearest whole number 
        left_arr = arr[0:len(arr)//2]
        right_arr = arr[len(arr)//2:len(arr)]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge arrays
        i = 0 # left_array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else: 
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1



arr_test = [9,8,7,6,5,4,3,2,1]
merge_sort(arr_test)
print(arr_test)
"""
# Second implementation - Same logic but variables that make more sense

def mergeSort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursion call for each step 
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing left and right side
        i = 0 # Traverse left side
        j = 0 # Traverse right side

        # Iterator for main list 
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                my_list[k] = left[i]
                # Move iterator i forward one
                i = i + 1 # Shortcut for i = i + 1 or can write i++
            else: 
                my_list[k] = right[j]
                # Move right iterator forward
                j = j + 1
            
            # Move to the next slot
            k += 1

        # Check for values that weren't sorted
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

my_list = [9,8,7,6,5,4,3,2,1]
mergeSort(my_list)
print(my_list)



