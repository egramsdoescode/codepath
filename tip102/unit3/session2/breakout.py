# 1
def manage_stage_changes(changes):
    canceled = []
    stack = []
    for change in changes:
        if change == "Cancel" and stack:
            canceled.append(stack.pop())
        elif change == "Reschedule" and canceled:
            stack.append(canceled.pop())
        else:
            stack.append(change[-1])
    return stack


print("--- Problem 1 ---")
print(
    manage_stage_changes(
        ["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]
    )
)
print(
    manage_stage_changes(
        ["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]
    )
)
print(
    manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])
)


# 2


def process_performance_requests(requests):
    sorted_requests = sorted(requests, key=lambda x: x[0], reverse=True)
    return [request[1] for request in sorted_requests]


print("--- Problem 2 ---")
print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
print(
    process_performance_requests(
        [(2, "Poetry"), (1, "Magic Show"), (4, "Concert"), (3, "Stand-up Comedy")]
    )
)
print(
    process_performance_requests(
        [
            (1, "Art Exhibition"),
            (3, "Film Screening"),
            (2, "Workshop"),
            (5, "Keynote Speech"),
            (4, "Panel Discussion"),
        ]
    )
)


# 3
def collect_festival_points(points):
    sum = 0
    stack = []
    for point in points:
        stack.append(point)

    while stack:
        sum += stack.pop()

    return sum


print("--- Problem 3 ---")
print(collect_festival_points([5, 8, 3, 10]))
print(collect_festival_points([2, 7, 4, 6]))
print(collect_festival_points([1, 5, 9, 2, 8]))


# 4
def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue == "back" and stack:
            stack.pop()
        elif clue != "back":
            stack.append(clue)
    return stack


print("--- Problem 4 ---")
clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues))

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues))

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))


# 5
def merge_schedules(schedule1, schedule2):
    result = ""
    left = 0
    right = 0
    while left < len(schedule1) and right < len(schedule2):
        result += schedule1[left]
        result += schedule2[right]
        left += 1
        right += 1

    if left < len(schedule1):
        result += schedule1[left:]
    elif right < len(schedule2):
        result += schedule2[right:]

    return result


print("--- Problem 5 ---")
print(merge_schedules("abc", "pqr"))
print(merge_schedules("ab", "pqrs"))
print(merge_schedules("abcd", "pq"))
# # 6
# print("--- Problem 6 ---")
#
# # 7
# print("--- Problem 7 ---")
