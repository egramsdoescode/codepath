# 1

# U: Write a function that transposes a matrix along its main diagonal and return the resulting transposition

# P: Create a result matrix of the same dimensions as the input matrix. Iterate over rows and columns of the input matrix, setting result[j][i] = matrix[i][j]. Return transposed result


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


print("\n--- Problem 1 ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))

# 2

# U: Two pointer reverse list, use the two pointer approach to reverse a list of strings, return the resulting list. Modify the list in place.

# P: set a left and right pointer on each end of the list. Use a while loop to make the pointers move closer to each other, incrementing left and decrementing right. On each iteration, swap the strings. Return the modified list


def reverse_list(lst):
    l, r = 0, len(lst) - 1
    while l < r:
        temp = lst[r]
        lst[r] = lst[l]
        lst[l] = temp
        l += 1
        r -= 1
    return lst


print("\n--- Problem 2 ---")
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

lst = ["pooh", "christopher robin", "pikachu", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

# 3

# U: Write a function that accepts a sorted array and removes the duplicates in place. Return the lenght of the modified array


# P: Use two pointers method, a left pointer, pointed at the last known unique value, and a right pointer, the scanner for the duplicates. When you reach a duplicate, pop it off the list and do not move either pointer. Otherwise, remove each pointer
def remove_dupes(items):
    l, r = 0, 1
    while r < len(items):
        if items[r] == items[l]:
            items.pop(r)
        else:
            r += 1
            l += 1
    return len(items)


print("\n--- Problem 3 ---")
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

# 4

# U: Write a function that takes all even numbers of an integer array and puts them all at the beginning, followed by the odds. Return the resultant array

# P: Declare and initialize a results array, iterate through the input array and pop all evens onto the results array, return the results array with concatenated with the input array with just odds.


def sort_by_parity(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] % 2 == 0:
            l += 1
        elif nums[r] % 2 == 1:
            r += 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    return nums


print("\n--- Problem 4 ---")
nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [3, 1, 6, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))

# 5
