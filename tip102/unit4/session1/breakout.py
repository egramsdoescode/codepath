# 1


def extract_nft_names(nft_collection):
    return [collection["name"] for collection in nft_collection]


# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8},
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
]

nft_collection_3 = [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]

print("--- Problem 1 ---")
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


# 2


def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
]

nft_collection_2 = [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]

nft_collection_3 = []

print("--- Problem 2 ---")
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# 3


def identify_popular_creators(nft_collection):
    freq_map = {}
    for nft in nft_collection:
        freq_map[nft["creator"]] = freq_map.get(nft["creator"], 0) + 1

    return [key for key, value in freq_map.items() if value > 1]


print("--- Problem 3 ---")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5},
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3},
]

nft_collection_3 = [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))


# 4
def average_nft_value(nft_collection):
    if len(nft_collection) <= 0:
        return 0
    return sum(nft["value"] for nft in nft_collection) / len(nft_collection)


print("--- Problem 4 ---")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5},
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4},
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))

# 5


def search_nft_by_tag(nft_collections, tag):
    return [
        nft["name"]
        for collection in nft_collections
        for nft in collection
        if tag in nft["tags"]
    ]


print("--- Problem 5 ---")
nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]},
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]},
    ],
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]},
    ],
    [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}],
]

nft_collections_3 = [
    [{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]},
    ],
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))

# 6


def process_nft_queue(nft_queue):
    return [nft["name"] for nft in nft_queue]


print("--- Problem 6 ---")
nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1},
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3},
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6},
]
print(process_nft_queue(nft_queue_3))

# 7


def validate_nft_actions(actions):
    stack = []
    for action in actions:
        if action == "remove":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(action)
    return not stack


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print("--- Problem 7 ---")
print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))


# 8
def find_closest_nft_values(nft_values, budget):
    for i in range(len(nft_values)):
        if nft_values[i] < budget and nft_values[i + 1] >= budget:
            return (nft_values[i], nft_values[i + 1])


nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print("--- Problem 8 ---")
print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
