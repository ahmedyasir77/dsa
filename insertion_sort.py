# First implementation

def insertion_sort(list_a):
    # Range starts at one because first item doesn't have to be sorted because there isn't a value to the left of it
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        # This is the value that will be sorted
        value_to_sort = list_a[i]

        # Compare value to the left
        while list_a[i-1] > value_to_sort and i>0:
            # If the number is larger than we switch the values
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            # Check next item in list by using i-1
            i = i-1 
        
    return list_a


print(insertion_sort([7,4,6,5,4,56,3,6,34,5,354,3,45,3,45,3,54,354,3,45,35]))

# Second implementation

def insertion_sort_two(A):
    for i in range(1, len(A)):
        for j in range (i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break 
    return A

print(insertion_sort_two([7,4,6,5,4,56,3,6,34,5,354,3,45,3,45,3,54,354,3,45,35]))

# Third implementation

def insertion_sort_three(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        # Look at elements that are one less than i
        j = i - 1
        # Code runs until anchor is greater than elements of j 
        while j >= 0 and key < elements[j]:
            # Swapping the elements
            elements[j + 1] = elements[j]
            # Remove one from j because its been sorted
            j = j - 1
        # After array is sorted the key stops at j + 1 
        elements[j+1] = key
    return elements

print(insertion_sort_three([4,8,98,52,484,3521,384,5,168,413,13,41]))
            
