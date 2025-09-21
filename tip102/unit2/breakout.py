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
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
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
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print("\n--- Problem 4 ---")
print(identify_conflicts(venue1_schedule, venue2_schedule))
