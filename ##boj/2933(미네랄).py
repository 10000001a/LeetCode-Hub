import sys


class Cluster:
  def __init__(self, minerals: set[tuple]):
    self.minerals = minerals

  def contains(self, mineral: tuple):
    if len(list(filter(lambda e: e[0] == mineral[0] and e[1] == mineral[1],
                       self.minerals))) > 0:
      return True

    return False

  def isBottom(self) -> bool:
    return any(map(lambda m: m[0] == 0, self.minerals))

  def getBottomMinerals(self) -> list[tuple]:
    return list(
        filter(
            lambda m: m[0] == 0 or (m[0] - 1, m[1]) not in self.minerals,
            self.minerals
        )
    )

  def drop(self):
    self.minerals = list(map(lambda m: (m[0] - 1, m[1]), self.minerals))


class Cave:
  def __init__(self, minerals: dict[int, list[int]], rows: int, cols: int):
    self.minerals = minerals
    self.rows = rows
    self.cols = cols

  def _destroyMineral(self, r: int, from_right: bool) -> tuple:
    target_row = sorted(
        self.minerals[r],
        reverse=from_right
    )

    if len(target_row) == 0:
      return -1, -1

    self.minerals[r].remove(target_row[0])

    return r, target_row[0]

  def throwStick(self, row: int, phase: int):
    removed_mineral = self._destroyMineral(row, bool(phase % 2))
    if (-1, -1) == removed_mineral:
      return

    adjacent_minerals = self._getAdjacentMineral(removed_mineral)

    clusters = []

    for i, start_mineral in enumerate(adjacent_minerals):
      if i == 0:
        clusters.append(self._getCluster(start_mineral))
      else:
        if not any(map(lambda c: c.contains(start_mineral), clusters)):
          clusters.append(self._getCluster(start_mineral))

    for cluster in clusters:
      if cluster.isBottom():
        continue

      for mineral in cluster.minerals:
        if mineral[0] in self.minerals:
          self.minerals[mineral[0]].remove(mineral[1])

      while not self._getIsClusterIsBottom(cluster):
        cluster.drop()
        # print('dropped cluster', cluster.minerals)

      for mineral in cluster.minerals:
        if mineral[0] in self.minerals:
          self.minerals[mineral[0]].append(mineral[1])
        else:
          self.minerals[mineral[0]] = [mineral[1]]

  def _getCluster(self, mineral: tuple) -> Cluster:
    will_visit = [mineral]
    visited = set([])
    while will_visit:
      current_visit = will_visit.pop()
      if current_visit in visited:
        continue
      visited.add(current_visit)
      will_visit += list(filter(lambda m: m not in visited,
                                self._getAdjacentMineral(current_visit)))

    return Cluster(minerals=visited)

  def _getIsClusterIsBottom(self, cluster: Cluster) -> bool:
    for bottom_mineral_from_cluster in cluster.getBottomMinerals():
      x = self._contains(
          (bottom_mineral_from_cluster[0] - 1, bottom_mineral_from_cluster[1]))
      if bottom_mineral_from_cluster[0] == 0 or x:
        return True

    return False

  def _contains(self, mineral: tuple) -> bool:
    if mineral[0] in range(self.rows):
      return mineral[1] in self.minerals[mineral[0]]
    return False

  def _getAdjacentMineral(self, mineral: tuple) -> list[tuple]:
    adjacent = [
      (mineral[0] - 1, mineral[1]),
      (mineral[0] + 1, mineral[1]),
      (mineral[0], mineral[1] - 1),
      (mineral[0], mineral[1] + 1),
    ]

    return list(
        filter(
            self._contains,
            adjacent
        )
    )


IN = sys.stdin.readline

R, C = map(int, IN().split(' '))

minerals = {
  i: [] for i in range(R)
}

for row in range(R - 1, -1, -1):
  for col, v in enumerate(IN()[:-1]):
    if v == 'x':
      if row in minerals:
        minerals[row].append(col)
      else:
        minerals[row] = [col]

N = int(IN())

throws = list(map(lambda x: int(x) - 1, IN().split(' ')))

cave = Cave(minerals=minerals, rows=R, cols=C)

for i, v in enumerate(throws):
  cave.throwStick(v, i)

for row in range(R - 1, -1, -1):
  row_text = ''
  for col in range(C):
    row_text += (
      'x' if row in cave.minerals and col in cave.minerals[row] else '.')
  print(row_text)
