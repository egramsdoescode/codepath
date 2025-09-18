# 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")


print("\n--- Problem 1 ---")
welcome()


# 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


print("\n--- Problem 2 ---")
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


print("\n--- Problem 3 ---")
print_catchphrase("Pooh")
print_catchphrase("Mordecai")


# 4
def get_item(items, x):
    if not 0 <= x <= len(items) - 1:
        return None
    return items[x]


print("\n--- Problem 4 ---")
print(get_item([1, 2, 3, 4], 3))


# 5
# U: write a function that accepts a list of integers and returns the sum
# P: write a funtion, sum_honey(), that takes a list of integers, declare a sum variable, use a for loop to iterate through the list and adding each element to sum, return sum
def sum_honey(hunny_jars):
    hunny = 0
    for jar in hunny_jars:
        hunny += jar

    return hunny


print("\n--- Problem 5 ---")
print(sum_honey([1, 2, 3, 4]))


# 6
# U: write a function that doubles the values in a list and returns the doubled list
# P: use a for loop to iterate through all the elements in the list, doubling the values
def doubled(hunny_jars):
    return [x * 2 for x in hunny_jars]


print("\n--- Problem 6 ---")
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


print("\n--- Problem 7 ---")
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))


# 8

# U: Accept a list of strings named task and format them

# P: Print the title of the todo list, then iterate over the list of tasks, printing them out as we go with a task number and a space between each


def print_todo_list(tasks: list[str]):
    print("Pooh's To Do's")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    print("")


print("\n--- Problem 8 ---")
task = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
print_todo_list(task)

task = []
print_todo_list(task)

# 9

# U: Accept a list of integers and return true if every integer is even, false if otherwise

# P: Loop through list, if current integer is odd, return false


def can_pair(item_quantities):
    for quantitiy in item_quantities:
        if quantitiy % 2 != 0:
            return False
    return True


print("\n--- Problem 9 ---")
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))


# 10

# U: Make a function that takes a positive integer and returns all divisors of that positive integer.

# P: Iterate from the range 1 -> quantity (inclusive) and find all numbers that divide evenly into quantity by using the modulo operator. If the modulo operation results in zero, append it to the resulting list.


def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)

    return divisors


print("\n--- Problem 10 ---")
quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

quantity = 2
print(split_haycorns(quantity))

# 11

# U: Write a function that removes the letters t, i, g, e, and r from a string and returns the resulting string

# P: iterate over a list of the characters to be removed, and perform str.replace on the input string


def tiggerfy(s):
    s = s.lower()
    removeable_letters = ["t", "i", "g", "e", "r"]
    for letter in removeable_letters:
        s = s.replace(letter, "")

    return s


print("\n--- Problem 11 ---")
s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

# 12

# U: Write a function that takes in a list of strings and returns all indices of the string "thistle"

# P: Use for loop with enumerate to iterate over list and obtain the index and values, append to the resulting list the indices of strings with thistle


def locate_thistles(items):
    result = []
    for index, value in enumerate(items):
        if value == "thistle":
            result.append(index)
    return result


print("\n--- Problem 12 ---")
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
