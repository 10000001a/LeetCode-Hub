/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
  const m = board.length;
  const n = board[0].length;
  let isVisited = [];
  
  for (let i = 0; i < m; i++) {
    isVisited.push(new Array(n).fill(false));
  }

  for (let i = 1; i < m - 1; i++) {
    for (let j = 1; j < n - 1; j++) {
      if (isVisited[i][j] || board[i][j] === 'X') continue;

      let shouldFlip = true;
      const containingRegion = [];
      let currentVisiting;
      const willVisit = [[i, j]];

      while (willVisit.length !== 0) {
        currentVisiting = willVisit.shift();
        
        containingRegion.push([currentVisiting[0], currentVisiting[1]]);

        if (currentVisiting[0] === 0 || currentVisiting[0] === m - 1 || currentVisiting[1] === 0 || currentVisiting[1] === n - 1) {
          shouldFlip = false;
          continue;
        }
        
        if (isVisited[currentVisiting[0]][currentVisiting[1] + 1] === false && board[currentVisiting[0]][currentVisiting[1] + 1] === 'O') {
          willVisit.push([currentVisiting[0], currentVisiting[1] + 1]);
          isVisited[currentVisiting[0]][currentVisiting[1] + 1] = true;
        }
        
       

        if (isVisited[currentVisiting[0] + 1][currentVisiting[1]] === false && board[currentVisiting[0] + 1][currentVisiting[1]] === 'O') {
          willVisit.push([currentVisiting[0] + 1, currentVisiting[1]]);
          isVisited[currentVisiting[0] + 1][currentVisiting[1]] = true;
        }
        
       

        if (isVisited[currentVisiting[0]][currentVisiting[1] - 1] === false && board[currentVisiting[0]][currentVisiting[1] - 1] === 'O') {
          willVisit.push([currentVisiting[0], currentVisiting[1] - 1]);
          isVisited[currentVisiting[0]][currentVisiting[1] - 1] = true;
        }
        
       

        if (isVisited[currentVisiting[0] - 1][currentVisiting[1]] === false && board[currentVisiting[0] - 1][currentVisiting[1]] === 'O') {
          willVisit.push([currentVisiting[0] - 1, currentVisiting[1]]);
          isVisited[currentVisiting[0] - 1][currentVisiting[1]] = true;
        }
      }

      if (shouldFlip) {
        for (const x of containingRegion) {
          board[x[0]][x[1]] = 'X'
        }
      }
    }
  }
}