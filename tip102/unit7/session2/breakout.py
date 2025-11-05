from typing import Counter


print("--- Problem 1 ---")


def find_cruise_length_iterative(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        mid = (low + high) // 2
        if cruise_lengths[mid] > vacation_length:
            high = mid - 1
        elif cruise_lengths[mid] < vacation_length:
            low = mid + 1
        else:
            return True

    return False


def find_cruise_length_recursive(cruise_lengths, low, high, vacation_length):
    if low > high:
        return False
    mid = (low + high) // 2
    if cruise_lengths[mid] > vacation_length:
        return find_cruise_length_recursive(
            cruise_lengths, low, mid - 1, vacation_length
        )
    elif cruise_lengths[mid] < vacation_length:
        return find_cruise_length_recursive(
            cruise_lengths, mid + 1, high, vacation_length
        )
    else:
        return True


print(find_cruise_length_iterative([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length_iterative([8, 9, 12, 13, 13, 14, 15], 11))

l1 = [9, 10, 11, 12, 13, 14, 15]
l2 = [8, 9, 12, 13, 13, 14, 15]
print(find_cruise_length_recursive(l1, 0, len(l1) - 1, 13))
print(find_cruise_length_recursive(l2, 0, len(l2) - 1, 11))

print("\n--- Problem 2 ---")


def find_cabin_index_iterative(cabins, preferred_deck):
    low = 0
    high = len(cabins) - 1
    while low <= high:
        mid = (low + high) // 2
        if cabins[mid] > preferred_deck:
            high = mid - 1
        elif cabins[mid] < preferred_deck:
            low = mid + 1
        else:
            return mid
    return mid + 1


def find_cabin_index_recursive(cabins, low, high, preferred_deck):
    mid = (low + high) // 2

    if low > high:
        return mid + 1
    if cabins[mid] > preferred_deck:
        return find_cabin_index_recursive(cabins, low, mid - 1, preferred_deck)
    elif cabins[mid] < preferred_deck:
        return find_cabin_index_recursive(cabins, mid + 1, high, preferred_deck)
    else:
        return mid


print("ITERATIVE:")
print(find_cabin_index_iterative([1, 3, 5, 6], 5))
print(find_cabin_index_iterative([1, 3, 5, 6], 2))
print(find_cabin_index_iterative([1, 3, 5, 6], 7))

arr1 = [1, 3, 5, 6]
n = len(arr1)

print("\nRECURSIVE:")
print(find_cabin_index_recursive(arr1, 0, n - 1, 5))
print(find_cabin_index_recursive(arr1, 0, n - 1, 2))
print(find_cabin_index_recursive(arr1, 0, n - 1, 7))

print("\n--- Problem 3 ---")

count = 0


def count_checked_in_passengers(rooms, low, high):
    mid = (low + high) // 2
    if rooms[mid] == 0:
        return count_checked_in_passengers(rooms, mid + 1, high)


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1, 0, len(rooms1) - 1))
print(count_checked_in_passengers(rooms2, 0, len(rooms2) - 1))
print(count_checked_in_passengers(rooms3, 0, len(rooms3) - 1))

# print("\n--- Problem 6 ---")
#
#
# def find_treasure(matrix, treasure):
#     for i in range(len(matrix)):
#         low = 0
#         high = len(matrix[i]) - 1
#
#         while low <= high:
#             mid = (low + high) // 2
#             if matrix[i][mid] > treasure:
#                 high = mid - 1
#             elif matrix[i][mid] < treasure:
#                 low = mid + 1
#             else:
#                 return (i, mid)
#     return (-1, -1)
#
#
# rooms = [[1, 4, 7, 11], [8, 9, 10, 20], [11, 12, 17, 30], [18, 21, 23, 40]]
#
# print(find_treasure(rooms, 17))
# print(find_treasure(rooms, 5))
