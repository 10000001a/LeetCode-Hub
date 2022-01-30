/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
  const M = grid.length; N = grid[0].length;
  const movement = [{dx: 0, dy: -1}, {dx: 0, dy: 1}, {dx: -1, dy: 0}, {dx: 1, dy: 0}];
  let result = 0;
  
  const find = () => {
    for (let i = 0; i < M; i++) {
      for (let j = 0; j < N; j++) {
        if (grid[i][j] === "1") {
          return {i, j};
        }
      }
    }
    
    return false;
  }

                                      
  const dfs = (i, j) => {
    grid[i][j] = -1
                                      
    for (const {dx, dy} of movement) {
      const x = i + dx;
      const y = j + dy;
      
      if (x >= 0 && x < M && y >= 0 && y < N && grid[x][y]==="1") {
        dfs(x, y);
      }
    }
  }
  
  
  while (1) {
    const next = find();
    
    if (next === false) return result;
    
    dfs(next.i, next.j);

    result++;
  }
  
};