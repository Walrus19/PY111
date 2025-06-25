from typing import List


def majority_element(nums: List[int]) -> int:
    counter = 0
    majoristy_element = None
    for i in nums:
        if counter == 0:
            majoristy_element = i
            counter += 1
        elif i == majoristy_element:
            counter += 1
        else:
            counter -= 1

    return majoristy_element

