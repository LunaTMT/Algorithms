function whoIsWinner(PPL){
    const mat =  Array.from({ length: 6 }, () => Array.from({ length: 7 }).fill(0));
    const get_rc = new Map([
    ["A", 0],
    ["B", 1],
    ["C", 2],
    ["D", 3],
    ["E", 4],
    ["F", 5],
    ["G", 6]]);
    
    const checkRow = (row, player) => mat[row].join('').includes(player.repeat(4));
    const checkCol = (col, player) => mat.map(r => r[col]).join('').includes(player.repeat(4));
    
    const findNextFreeRow = (col) => {
      for (let row = 5; row >= 0; row--) { 
        if (mat[row][col] == 0) { return row }
      }
    }
  
    for (const move of PPL) {
      let col = get_rc.get(move[0]);
      let player = move[2];
      let row = findNextFreeRow(col)
      
      mat[row][col] = player
      
      if (checkRow(row, player) || checkCol(col, player) || checkDiagonal(mat, player, row, col)) {
        return move.substring(2);
      }
    }
    return 'Draw'
  }
  
    function checkDiagonal(matrix, player, row, col) {
      const rows = matrix.length;
      const cols = matrix[0].length;
    
      const check = (dr, dc) => {
          let consecutiveCount = 0;
          for (let i = -3; i <= 3; i++) {
            const r = row + dr * i;
            const c = col + dc * i;
      
            if (r >= 0 && r < rows && c >= 0 && c < cols) {
              if (matrix[r][c] === player) {
                if (++consecutiveCount === 4) {
                  return true; // Player has won diagonally
                }
              } else {
                consecutiveCount = 0;
              }
            }
          }
          return false;
        };
      
        return check(1, 1) || check(-1, 1); 
      }