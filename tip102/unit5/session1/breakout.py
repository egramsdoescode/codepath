class Villager:
    def __init__(self, name, species, catchprase):
        self.name = name
        self.species = species
        self.catchphrase = catchprase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchprase):
        cleaned_catchphrase = new_catchprase.replace(" ", "")
        if len(new_catchprase) < 20 and str.isalpha(cleaned_catchphrase):
            self.catchphrase = new_catchprase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase :(")

    def add_item(self, item_name):
        valid_items = {
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree",
        }
        if item_name in valid_items:
            self.furniture.append(item_name)

    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
            return

        freq_map = {}
        res = ""
        for item in self.furniture:
            freq_map[item] = freq_map.get(item, 0) + 1
        for item, quantity in freq_map.items():
            res += f"{item}: {quantity}, "
        print(res[: len(res) - 2])


class Villager2:
    def __init__(self, name, species, personality, catchprase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchprase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchprase):
        cleaned_catchphrase = new_catchprase.replace(" ", "")
        if len(new_catchprase) < 20 and str.isalpha(cleaned_catchphrase):
            self.catchphrase = new_catchprase
            print("Catchphrase updated!")
        else:
            print("Invalid catchphrase :(")

    def add_item(self, item_name):
        valid_items = {
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree",
        }
        if item_name in valid_items:
            self.furniture.append(item_name)

    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
            return

        freq_map = {}
        res = ""
        for item in self.furniture:
            freq_map[item] = freq_map.get(item, 0) + 1
        for item, quantity in freq_map.items():
            res += f"{item}: {quantity}, "
        print(res[: len(res) - 2])


def of_personality_type(townies, personality_type):
    return [townie.name for townie in townies if townie.personality == personality_type]


# 1
apollo = Villager("Apollo", "Eagel", "pah")

print("--- Problem 1 ---")
print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)

# 2
bones = Villager("Bones", "dog", "yip yip")

print("\n--- Problem 2 ---")
print(bones.greet_player("Ethan"))

# 3
bones.catchphrase = "ruff it up"

print("\n--- Problem 3 ---")
print(bones.greet_player("Samia"))

# 4
alice = Villager("Alice", "Koala", "guvnor")
print("\n--- Problem 4 ---")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

bobby = Villager("Bobby", "Human", "keep rollin'")

# 5
print("\n--- Problem 5 ---")
print(bobby.furniture)

bobby.add_item("acoustic guitar")
print(bobby.furniture)

bobby.add_item("cacao tree")
print(bobby.furniture)

bobby.add_item("nintendo switch")
print(bobby.furniture)

# 6
print("\n--- Problem 6 ---")
alice.print_inventory()

bobby.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
bobby.print_inventory()

print("\n--- Problem 7 ---")
isabelle = Villager2("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager2("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager2("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


print("\n--- Problem 9 ---")
tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
tom_nook.next = tommy
print(tom_nook.value)
print(tom_nook.next.value)
print(tommy.value)
print(tommy.next)

print("\n--- Problem 10 ---")
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)

print("\n--- Problem 11 ---")
saharah = Node("Saharah")
tom_nook.next = None
tommy.next = saharah

print(tom_nook.next)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next.value)
print(saharah.value)
print(saharah.next)

print("\n--- Problem 12 ---")


def print_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> " if curr.next else "\n")
        curr = curr.next


isabelle = Node("Isabelle")
ethan = Node("Ethan")
cj = Node("C.J.")

isabelle.next = ethan
ethan.next = cj
print_list(isabelle)
