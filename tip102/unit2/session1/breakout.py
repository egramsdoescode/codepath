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

    return sum(v * (v - 1) // 2 for v in freq_map.values())


print("\n--- Problem 8 ---")
popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))
