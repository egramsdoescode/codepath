# Lecture Problem


def nanana_batman(x):
    na_str += ""
    for _ in range(x):
        na_str += "na"
    return f"{na_str} batman!"


print("\n--- Lecture Problem ---")
print(nanana_batman(6))
print(nanana_batman(0))

# 1

# U: Write a function that takes in a string with words, separated by spaces, and return the string with the words in reverse order

# P: Split the words into a list using split() with spaces as the delimiter, reverse the list, and then join back togeter with spaces


def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])


print("\n--- Problem 1 ---")
sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

# 2

# U: Write a funciton that takes in a list of unique positive integers and returns any number that is not the minimum or maximum

# P: Store the min and max of the list in separate variables, loop through the array and return the first non-min non-max number. Return -1 if that is not found


def goldilocks_approved(nums):
    # If nums is 2 or less, the min and max are the only numbers
    if len(nums) < 3:
        return -1

    min_num = min(nums)
    max_num = max(nums)
    for num in nums:
        if num != min_num and num != max_num:
            return num
    return -1


print("\n--- Problem 2 ---")
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))

# 3

# U: Write a function that continuosly removes the minimum element of an integer list until the list is empty. Return a new list of elements in the order in which they were removed

# P: Create result list, use a while loop to continue while input list is not empty, keep track of the minimum and remove it each iteration, appending it to the resulting list.


def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while hunny_jar_sizes:
        min_size = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(min_size)
        result.append(min_size)
    return result


print("\n--- Problem 3 ---")
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

# 4

# U: Write a function that accepts an integer and returns the sum of its digits. Ex. 423 -> 4 + 2 + 3 -> 9

# P: Use a while loop and iterate on num while it is not zero. Use modulo operator to store current digit and use // to take num down to the remaining digits each iteration


def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


print("\n--- Problem 4 ---")
num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))

num = 12345
print(sum_of_digits(num))

# 5

# U: Write a function that takes in a string list of 4 different operations. Two of the words, bouncy and flouncy increment a variable <tigger> and the other two decrement tigger. tigger will start at 1. Return the resulting tigger variable after all operations

# P: Create two arrays to hold the different operations. iterate over the operations and increment or decrement tigger. Return tigger.


def final_value_after_operations(operations):
    tigger = 1
    up = set(["bouncy", "flouncy"])
    down = set(["trouncy", "pouncy"])
    for op in operations:
        if op in up:
            tigger += 1
        elif op in down:
            tigger -= 1
    return tigger


print("\n--- Problem 5 ---")
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# 6

# U: Given a string list words and a string s, write a functino to see if the string is an acronym for words. Ex. ["Ethan, "Grams"] == "EG", but not "GE"

# P: First check if the length of words is the same as length of s, if they are not equal it is not possible to be an acronym. Then iterate over the range of len(words), check that the first letter of each word matches with each letter of s.


def is_acronym(words, s):
    if len(words) != len(s):
        return False
    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False
    return True


print("\n--- Problem 6 ---")

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["ethan", "taylor", "grams"]
s = "ebg"
print(is_acronym(words, s))

# 7

# U: Write a function that takes an integer list and tells you how many operations it will take to make all the elements divisible by 3. An operation is adding or subtraction by 1

# P: Iterate through each number and take the remainder modulo three of that number. If the result is 0, move on, if not add that to operations.


def make_divisible_by_k(nums, k):
    ops = 0
    for num in nums:
        remainder = num % k
        if remainder != 0:
            ops += min(remainder, k - remainder)

    return ops


print("\n--- Problem 7 ---")
nums = [1, 2, 3, 4]
print(make_divisible_by_k(nums, 3))

nums = [3, 6, 9]
print(make_divisible_by_k(nums, 4))

# 8:

# U: Given two string list, return a new list containing elements that are in list 1 and not list 2 and elements in list2 that are not in list 1

# P: Turn list1 and list2 into sets and use the set.difference() method to get the list of elements without those in common


def exclusive_elemts(lst1, lst2):
    return list(set(lst1).difference(set(lst2))) + list(set(lst2).difference(set(lst1)))


print("\n--- Problem 8 ---")
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

# 9

# U: Write a function that accepts two strings and alternately concatentate them to a a new string, if one is longer than the other, add all the remaing letters to the end

# P: Use a while loop, loop over both strings and concatenate one after the other


def merge_alternately(word1, word2):
    result = []
    for a, b in zip(word1, word2):
        result.append(a)
        result.append(b)
    result.append(word1[len(word2) :])
    result.append(word2[len(word1) :])
    return "".join(result)


print("\n--- Problem 9 ---")
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))

# 10

# U: Write a function that takes two integer arrays and a positive intger, and return the number of good pairs. A pair is good if arr1[i] is divisible by arr2[j] * k

# P: Iterate through the integers in pile1 and check them agains each integer in pile2


def good_pairs(pile1, pile2, k):
    result = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                result += 1
    return result


print("\n--- Problem 10 ---")
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
