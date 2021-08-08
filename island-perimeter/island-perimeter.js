/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
  let answer = 0
  const height = grid.length;
  const width = grid[0].length;
  let i;
  let j;
  
  const queue = [];
  const visited = [];
  
  const countSides = ({i, j}) => {

    if (visited[i][j] === 1) return;
    visited[i][j] = 1;
    if (i === 0 || grid[i - 1][j] === 0) {
      answer++;
    } else {
      if (visited[i - 1][j] === 0) queue.push({i: i - 1, j});
    }
    
    if (j === 0 || grid[i][j - 1] === 0) {
      answer++;
    } else {
      if (visited[i][j - 1] === 0) queue.push({i, j: j - 1});
    }
    
    if (i === height - 1 || grid[i + 1][j] === 0) {
      answer++;
    } else {
      if (visited[i + 1][j] === 0) queue.push({i: i + 1, j});
    }
    
    if (j === width - 1 || grid[i][j + 1] === 0) {
      answer++;
    } else {
      if (visited[i][j + 1] === 0) queue.push({i, j: j + 1});
    } 
  }

  for (let x = 0; x < height && i == undefined && j == undefined; x++) {
    for (let y = 0; y < width; y++) {
      if (grid[x][y] === 1) {
        i = x;
        j = y;
        break;
      } 
    }
  }

  
  for (let x = 0; x < height; x++) {
    visited.push([]);
    for (let y = 0; y < width; y++) {
      visited[x].push(0);
    }
  }


  queue.push({i, j})
  
  while (queue.length > 0) {
    const visiting = queue.shift();
    
    countSides({i: visiting.i, j: visiting.j});
  }
  
  return answer;
};
