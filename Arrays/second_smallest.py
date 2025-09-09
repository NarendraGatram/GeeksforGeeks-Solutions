'''
    Problem: Find the second smallest element in an array. If no such element exists, return -1.
    Category: Arrays
    Difficulty: Easy
'''



def second_smallest(arr):
    if len(arr) < 2:
        return -1

    mini = arr[0]
    second_smallest = float('inf')

    for i in range(1, len(arr)):
        if arr[i] < mini:
            second_smallest = mini
            mini = arr[i]
        elif arr[i] > mini and arr[i] < second_smallest:
            second_smallest = arr[i]

    if second_smallest != float('inf'):
        return second_smallest
    else:
        return -1
    
# Example usage:
arr = eval(input("Enter the array: "))
print("The second smallest element is:", second_smallest(arr))
