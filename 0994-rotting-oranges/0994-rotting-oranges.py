class Cell:

  def __init__(self, _type):
    self.is_orange = True if _type >= 1 else False
    self.is_rotted = True if _type == 2 else False
  
  def rot(self):
    if self.is_orange:
      self.is_rotted = True

class Solution:
  
  
    def orangesRotting(self, grid: List[List[int]]) -> int:
      
        def getAdjacentOrange(grid: List[List[Cell]], position: Tuple[int, int]) -> List[Tuple[int, int]]:
          adjacent_position = [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1)
          ]
          
          def filterCb(t: Tuple[int, int]):
            return t[0] >= 0 and t[0] < len(grid) and t[1] >= 0 and t[1] < len(grid[0]) and grid[t[0]][t[1]].is_orange and not grid[t[0]][t[1]].is_rotted
          
          return list(filter(filterCb, adjacent_position))
      
        count_orange = 0
        count_rotted = 0
        rotted_cell_list: List[Tuple[int, int]] = []
        new_grid = [[] for _ in range(len(grid))]
        
        for i, row in enumerate(grid):
          for j, _type in enumerate(row):
            new_grid[i].append(Cell(_type))    
            if _type == 2:
              rotted_cell_list.append((i, j))
              count_rotted += 1
            if _type >= 1:
              count_orange += 1
        
        will_rot = set([])
        
        for rotted_cell in rotted_cell_list:
          will_rot.update(getAdjacentOrange(new_grid, rotted_cell)) 
        
        _round = 0
        
        while will_rot:
          should_rot_list = list(will_rot)
          new_will_rot = set([])
          
          for should_rot in should_rot_list:
            count_rotted += 1
            new_grid[should_rot[0]][should_rot[1]].rot()
            new_will_rot.update(getAdjacentOrange(new_grid, should_rot)) 
          
          will_rot = set(new_will_rot - will_rot)
          _round += 1
        
        return _round if count_rotted == count_orange else -1