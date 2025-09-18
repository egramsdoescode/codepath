# 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")


welcome()


# 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


greeting("Shelly")


# 3
def print_catchphrase(character):
    phrases = {
        "Pooh": "Oh bother!",
        "Tigger": "TFFN: Ta-ta for now!",
        "Eeyore": "Thanks for noticing me.",
        "Christopher Robin": "Silly old bear.",
    }

    if character in phrases:
        print(phrases[character])
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


print_catchphrase("Pooh")
print_catchphrase("Mordecai")


# 4
def get_item(items, x):
    if not 0 <= x <= len(items) - 1:
        return None
    return items[x]


print(get_item([1, 2, 3, 4], 3))


# 5
# U: write a function that accepts a list of integers and returns the sum
# P: write a funtion, sum_honey(), that takes a list of integers, declare a sum variable, use a for loop to iterate through the list and adding each element to sum, return sum
def sum_honey(hunny_jars):
    hunny = 0
    for jar in hunny_jars:
        hunny += jar

    return hunny


print(sum_honey([1, 2, 3, 4]))


# 6
# U: write a function that doubles the values in a list and returns the doubled list
# P: use a for loop to iterate through all the elements in the list, doubling the values
def doubled(hunny_jars):
    return [x * 2 for x in hunny_jars]


print(doubled([1, 2, 3, 4]))

# 7

# U: write a function that accepts a list of integers <race_times> and aninteger <threshold> and return all integers less than <threshold> in <race_times>


# P: Initialize a counter for the return value, loop over race_times and increment every time an element is less than threshold
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []

threshold = 4
print(count_less_than(race_times, threshold))

# 8
