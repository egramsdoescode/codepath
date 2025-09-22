# 1

# U: Write a function that maps 2 lists with keys and values in a dictionary

# P: Iterate over both lists with zip, input them into a dictionary, return it


def lineup(artists, set_times):
    lineup_dict = {}
    for artist, time in zip(artists, set_times):
        lineup_dict[artist] = time
    return lineup_dict


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print("\n--- Problem 1 ---")
print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))


# 2

# U: Write a function a that accepts a string and a dictionary, using the string, return the corresponding value in the dictionary

# P: See if the string key corresponds to a value in the provided dictionary, if so return the corresponding value, other wise return a default value


def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, {"message": "Artist not found"})


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"},
}

print("\n--- Problem 2 ---")
print(get_artist_info("Blood Orange", festival_schedule))
print(get_artist_info("Taylor Swift", festival_schedule))

# 3

# U: Write a function that accepts a dictionary of type {<str>: <Int>} and return the sum of all the keys

# P: Iterate throught the dictionary with a for loop and return the sum


def total_sales(ticket_sales):
    sum = 0
    for value in ticket_sales.values():
        sum += value
    return sum


print("\n--- Problem 3 ---")
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

# 4

# U: Write a function that accpets two dictionaries and return a dictionary with key-value pairs that are in common with both

# P: Use zip to iterate through key-value pairs of each dictionary, add them tothe resulting dictionary


def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}
    for (k1, v1), (k2, v2) in zip(venue1_schedule.items(), venue2_schedule.items()):
        print(k1, k2, v1, v2)
        if k1 == k2 and v1 == v2:
            result[k1] = v1
    return result


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM",
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM",
}

print("\n--- Problem 4 ---")
print(identify_conflicts(venue1_schedule, venue2_schedule))

# 5

# U: Write a function that takes a dictionary votes that maps ID numbers, to artist voted for, return the artists with the highest number of votes

# P: Create a frequency map with artist name as the key and num votes as the values, iterate through the input dict, tallying up the votes for each artist in the frequency map, return the artist with the highest votes.


def best_set(votes):
    freq_map = {}
    for artist in votes.values():
        freq_map[artist] = freq_map.get(artist, 0) + 1

    return max(freq_map, key=freq_map.get)


votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA",
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
}

print("\n--- Problem 5 ---")
print(best_set(votes1))
print(best_set(votes2))

# 6

# U: Write a function given an array of integers, that returns the sum of every integer that is the maximum of the array

# P: Make a frequency map out of the input array, the elements being the values and the frequency of each as the keys. Return the sum of the most frequent element


def max_audience_performances1(audiences):
    freq_map = {}
    for num in audiences:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_size = max(freq_map.keys())

    return max_size * freq_map[max_size]


print("\n--- Problem 6 ---")
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances1(audiences1))
print(max_audience_performances1(audiences2))

# 7

# U: Same as above, without a dictionary

# P: Get the maximun value of audiences, return the max value times its frequency with the list.count() class method


def max_audience_performances2(audiences):
    max_size = max(audiences)
    return max_size * audiences.count(max_size)


print("\n--- Problem 7 ---")
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances2(audiences1))
print(max_audience_performances2(audiences2))

# 8

# U: Write a function that returns the amount of pairs i and j such that arr[i] == arr[j] and i < j

# P: Make a frequency map counting the individual values of input array , for each value in freq_map that is > 1, add value / value - 1 // 2 to the result. Return result


def num_popular_pairs(pop_scores):
    freq_map = {}
    for score in pop_scores:
        freq_map[score] = freq_map.get(score, 0) + 1

    result = 0
    for value in freq_map.values():
        result += (value * (value - 1)) // 2

    # This one-liner does the same, but is less readable
    # sum(v * (v - 1) // 2 for v in freq_map.values())

    return result


print("\n--- Problem 8 ---")
popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))

# 9

# U: Write a function that takes in two lists of strings, one is a permutation of the other, that calculates the absolute difference between the same string in both lists. Ex. str at index 0 in first list and that same str being at index 3 would be a difference of 3.

# P: Do a brute force implementation first with a nested for loop, getting the difference for each string, return the sum of all differences. Work to find an optimized solution


def find_stage_arrangement_difference(s, t):
    difference = 0

    # Brute Force O(n^2) time, O(1) space
    # for i in range(len(s)):
    #     for j in range(len(t)):
    #         if s[i] == t[j]:
    #             difference += abs(i - j)

    # Optimized O(n) time, O(n) space
    freq_map = {}
    for idx, el in enumerate(s):
        freq_map[el] = idx

    for idx, el in enumerate(t):
        difference += abs(idx - freq_map[el])

    return difference


print("\n--- Problem 9 ---")
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

# 10

# U: Write a function that takes in two strings, return how many of str1's characters are present in str2

# P: Create an empty set, for each character in str1 add it to the set, count how many characters in str2 are in the set of str1.


def num_VIP_guests(vip_passes, guests):
    vip_set = set(c for c in vip_passes)
    counter = 0
    for c in guests:
        if c in vip_set:
            counter += 1
    return counter


print("\n--- Problem 10 ---")
vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

# 11

# U: Debug the given function

# P: Run the code and implement print-debugging as I go along, refactoring to a solution


def schedule_pattern(pattern, schedule):

    genres = schedule.split()
    # old
    # if len(genres) == len(pattern):
    #     return True

    # new, if the lengths do not match up, patterns can't be the same
    if len(genres) != len(pattern):
        return False

    char_to_genre = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            # old
            # if char_to_genre[char] == genre:
            #     return True
            # new, return false if genres do not match pattern
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        # new, completely removed genre_to_char code, only one association needed

    return True


print("\n--- Problem 11 ---")
pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))


# 12

# U: Write a function that takes a list of strings and list of integers, both of length n. strs[i] and ints[i] are directly correlated. Sort the strings based on their associated integers in reverse order

# P: Put both into a dictionary, where key is string and value is integer, reverse sort by the values, then return the list of keys


def sort_performers(performer_names, performance_times):
    # This is the approach I wanted to use, but breaks if there are two people with the same name
    # performer_dict = {n: t for n, t in zip(performer_names, performance_times)}
    # result = sorted(performer_dict, reverse=True)
    # return result

    pairs = list(zip(performer_names, performance_times))
    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    return [name for name, _ in pairs]


print("\n--- Problem 12 ---")
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))
print(sort_performers(performer_names2, performance_times2))
