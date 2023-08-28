class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        need_to_success = sorted([success // i if success % i == 0 else success // i + 1 for i in potions])
        # [5, 1, 3]
        # [7, 4, 3, 2, 2]
        # return [len([i for i in need_to_success if i <= spell]) for spell in spells]

        print(need_to_success)

        for spell in spells:
            result.append(b_search(spell, need_to_success))
        
        return result

def b_search(target: int, list: List[int]) -> int:
    start, end = 0, len(list) - 1

    if target < list[start]:
        return 0
    
    if target >= list[end]:
        return len(list)

    while end - start > 1:
        half = (start + end) // 2

        if target < list[half]:
            end = half
        else:
            start = half
        
    return start + 1

