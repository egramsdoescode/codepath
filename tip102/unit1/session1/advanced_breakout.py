# 1

# U: Write a function that accepts a list of strings and a target string,return the first index of target in items and -1 if target is not in items
# P: iterate through list of strings using enumerate to get index and value, return the first instance of target, otherwise return -1 if the target is not found during the loop


def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


print("--- Problem 1 ---")
items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
print(linear_search(items, target))

# 2

# U: Write a function that takes a list of strings of "bouncy", "flouncy", "trouncy", or "pouncy", and increment a variable named tigger (starts at 1) for each instance of bouncy or flouncy and decrement for each instance of trouncy or pouncy

# P: Create two sets, one with the incrementing strings and one with the decrementing strings, declare a variable starting at 1, iterate through the list, if in the incrment list, increment tigger, and the opposit for the other. Return tigger


def final_value_after_operations(operations):
    up = set(["bouncy", "flouncy"])
    down = set(["trouncy", "pouncy"])
    tigger = 1
    for op in operations:
        if op in up:
            tigger += 1
        elif op in down:
            tigger -= 1
    return tigger


print("\n--- Problem 2 ---")
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# 3

# U: Write a function that removes the letters t, i, g, e, and r from a string and returns the resulting string

# P: iterate over a list of the characters to be removed, and perform str.replace on the input string


def tiggerfy(s):
    s = s.lower()
    removeable_letters = [
        "t",
        "i",
        "gg",
        "er",
    ]
    for letter in removeable_letters:
        s = s.replace(letter, "")

    return s


print("\n--- Problem 3 ---")
word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

# 4

# U: Write a function that accepts a list of integers that determines if the function could become non-decreasing by changing 1 element at most

# P: Declare and initialize count variable. Iterate through list, check if nums[i] <= nums[i+1], if so keep going, else increment count. If count is > 1, return False


def non_decreasing(nums):
    count = 0
    for i in range(1, len(nums)):
        if not nums[i] >= nums[i - 1]:
            count += 1
    return count <= 1


print("\n--- Problem 4 ---")
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

# 5

# U: Write a function that accepts a lower bound, upper bound, and a list of clue integers, return a nested list of all the ranges of numbers that are missing from the upper and lower bound

# P: Iterate through clues, if next number is more than one away from the previous, append a range of the missing numbers. If the last element is less than the upper bound, append a range from the next number to the upper bound


def find_missing_clues(clues, lower, upper):
    missing_clues = []
    for i in range(1, len(clues)):
        if lower <= clues[i - 1] and upper >= clues[i]:
            if clues[i] - 1 > clues[i - 1]:
                missing_clues.append([clues[i - 1] + 1, clues[i] - 1])
        if i == len(clues) - 1 and clues[i] < upper:
            missing_clues.append([clues[i] + 1, upper])
    return missing_clues


print("\n--- Problem 5 ---")
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

# 6

# U: Implement a function that accepts a 2D list and return the amount of c's in the list

# P: Take a naive approach with a for loop first, then use a built in list function to count


def harvest(vegetable_patch):
    ready = 0

    # Naive approach
    # for _, row in enumerate(vegetable_patch):
    #     for _, value in enumerate(row):
    #         if value == "c":
    #             ready += 1

    # Clean approach
    for row in vegetable_patch:
        ready += row.count("c")
    return ready


print("\n--- Problem 6 ---")
vegetable_patch = [["x", "c", "x"], ["x", "x", "x"], ["x", "c", "c"], ["c", "c", "c"]]
print(harvest(vegetable_patch))

# 7

# U: Accept two integer lists: pile1 and pile2, and an integer k. Give the amount of pairs (i, j) such that pile1[i] is divisible by pile2[j] * k

# P: Iterate through pile1, for each integer in pile1, iterate through pile2 and find the proper pairs.


def good_pairs(pile1, pile2, k):
    pairs_count = 0
    for i in pile1:
        for j in pile2:
            if i % (j * k) == 0:
                pairs_count += 1
    return pairs_count


print("\n--- Problem 7 ---")
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
