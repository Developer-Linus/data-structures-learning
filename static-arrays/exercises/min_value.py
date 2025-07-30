"""
Basic Positive Numbers
    Input: [4, 2, 8, 1, 9]
    Task: Return (1, 3)
(Minimum value is 1 at index 3)
"""


def get_min_and_index(numbers):
    min_num = numbers[0]
    min_index = 0
    for i in range(1, len(numbers)):
        if min_num > numbers[i]:
            min_num = numbers[i]
            min_index = i
    return (min_num, min_index)


print(get_min_and_index([4, 7, 9, 23, 0]))
