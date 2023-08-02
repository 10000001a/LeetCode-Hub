class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      count_map = {}
      
      for element in arr:
        if element in count_map.keys():
          count_map[element] += 1
        else:
          count_map[element] = 1
      
      return len(count_map.values()) == len(set(count_map.values()))
        