from typing import List


async def binary_search(lys: List[dict], val: str | int, key: str = "id") -> dict:
    """Searching for an element by id"""
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid].get(key) == val:
            index = mid
        else:
            if val < lys[mid].get(key):
                last = mid - 1
            else:
                first = mid + 1
    return lys[index] if index != -1 else None
