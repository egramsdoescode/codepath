from math import inf

# Lecture Problem


def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i


print("\n--- Lecture Problem: Two Sum ---")

# answer should be [4, 5]
print(two_sum([1, 2, 3, 4, 5], 9))

# answer should be [1, 2]
print(two_sum([6, 3, 5], 8))


# 1

# U: Given a list of species dictionaries, return the name of the species with the smallest population

# P: Iterate through the species list and keep track of the minimum population, then return the name of the species with minimum population


def most_endangered(species_list):
    min = inf
    priority = {}
    for creature in species_list:
        if creature["population"] < min:
            min = creature["population"]
            priority = creature
    return priority["name"]


print("\n--- Problem 1 ---")
species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]

print(most_endangered(species_list))

# NOTE: Problem 2 was identical to one on the first problem set

# 3


def navigate_research_station(station_layout, observations):
    station_dict = {value: index for index, value in enumerate(station_layout)}
    # Starting distance
    distance = abs(0 - station_dict[observations[0]])
    for i in range(1, len(observations)):
        distance += abs(
            station_dict[observations[i]] - station_dict[observations[i - 1]]
        )

    return distance


print("\n--- Problem 3 ---")
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))
print(navigate_research_station(station_layout2, observations2))

# 4


def prioritize_observations(observed_species, priority_species):
    priority_dict = {}
    result = []
    leftover = []
    for species in priority_species:
        priority_dict[species] = []

    for species in observed_species:
        if species in priority_dict:
            priority_dict[species].append(species)
        else:
            leftover.append(species)

    for value in priority_dict.values():
        result.extend(value)

    result.extend(sorted(leftover))
    return result


print("\n--- Problem 4 ---")
observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2))
