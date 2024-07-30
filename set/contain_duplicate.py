from typing import List

def contains_duplicate(list: List[int]) -> bool:
    seen = set()

    for num in list:
        if num in seen:
            return True
        seen.add(num)
    return False


print(contains_duplicate([1,4,652,12,4]))