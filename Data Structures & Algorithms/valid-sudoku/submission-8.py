class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares[(i//3, j//3)]:
                    print(i,j)
                    print(board[i][j])
                    print(rows[i]) 
                    print(columns[j])
                    print(squares[(i/3, j/3)])
                    return False
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    squares[(i//3, j//3)].add(board[i][j])
        print(rows)
        print(columns)
        print(squares)
        return True