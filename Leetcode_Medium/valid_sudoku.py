from typing import List
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = {}
    columns = {}
    square = {}

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            if r not in rows:
                rows[r] = set()
            if c not in columns:
                columns[c] = set()
            if (r // 3, c // 3) not in square:
                square[(r//3, c//3)] = set()

            if ((board[r][c] in rows[r]) or
                (board[r][c] in columns[c]) or
                (board[r][c] in square[(r//3, c//3)])):
                return False
            columns[c].add(board[r][c])
            rows[r].add(board[r][c])
            square[(r//3, c//3)].add(board[r][c])
    return True


if __name__ == "__main__":
    output = isValidSudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]])
    print(output)