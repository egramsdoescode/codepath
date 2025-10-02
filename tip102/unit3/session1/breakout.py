# 1

# U: Given a string of opening/closing brackets, write a function that returns whether these brackets open and close in the correct order

# P: Create a dictionary with each closing bracket type as the keys and ttheir associated opening brackets as values. Create an empty stack to push opening brackets onto. Iterate through the input string, if the bracket is an opening bracket, push it onto the stack, if it is a closing bracket, check to see if the top of the stack is the corresponding opening bracket and if the stack is not empty, if not, return False, otherwise, pop the opening bracket off the stack. At the end of the loop, if the stack is empty, return True.


def is_valid_post_format(posts):
    brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in posts:
        if c in brackets.values():
            stack.append(c)
        elif not stack or stack[-1] != brackets[c]:
            return False
        else:
            stack.pop()

    return not stack


print("\n--- Problem 1 ---")
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))

# 2

# U: Given a list of strings, reverse their order using a stack

# P: Create an empty stack and pop elements off of the comments list and append them to the stack, once the comments list is empty, return stack


def reverse_comments_queue(comments):
    stack = []
    while comments:
        stack.append(comments.pop())
    return stack


print("\n--- Problem 2 ---")
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# 3

# U: Given a string, write a function that tells if it is symmetrical. A string is symmetrical if it reads the same left to right as it does right to left, ignoring spacing, punctuation, and capitalization

# P: Make string lowercase, remove spaces and punctuation. Use two pointers, one on the left, one on the right, if one of the letters does not match up, return False, otherwise return True


def is_symmetrical_title(title):

    cleaned_title = ("".join(char for char in title if char.isalnum())).lower()

    left = 0
    right = len(cleaned_title) - 1
    while left < right:
        if cleaned_title[left] != cleaned_title[right]:
            return False
        left += 1
        right -= 1
    return True


print("\n--- Problem 3 ---")
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))

# 4


def engagement_boost(engagements):
    left = 0
    right = len(engagements) - 1
    position = len(engagements) - 1
    result = [0] * len(engagements)

    while left <= right:
        absolute_left = abs(engagements[left])
        absolute_right = abs(engagements[right])

        if absolute_left > absolute_right:
            result[position] = absolute_left * absolute_left
            left += 1
        else:
            result[position] = absolute_right * absolute_right
            right -= 1
        position -= 1

    return result


print("\n--- Problem 4 ---")
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

# 5

# U:

# P:


def clean_post(post):
    pass


print("\n--- Problem 5 ---")
print(clean_post("poOost"))
print(clean_post("abBAcC"))
print(clean_post("s"))
