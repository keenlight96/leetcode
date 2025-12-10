from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    reservoir = [[set() for _ in range(9)] for _ in range(3)]
    # reservoir[0]: row
    # reservoir[1]: column
    # reservoir[2]: sub-board 3x3
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                # check rows
                count = len(reservoir[0][i])
                reservoir[0][i].add(board[i][j])
                if count == len(reservoir[0][i]):
                    return False

                # check columns
                count = len(reservoir[1][j])
                reservoir[1][j].add(board[i][j])
                if count == len(reservoir[1][j]):
                    return False

                # check sub-board
                idx = (i // 3) * 3 + j // 3
                count = len(reservoir[2][idx])
                reservoir[2][idx].add(board[i][j])
                if count == len(reservoir[2][idx]):
                    return False
    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))


def isValidSudoku_bak(board: List[List[str]]) -> bool:
    for i in range(9):
        # Check row
        row = []
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in row:
                    return False
                else:
                    row.append(board[i][j])

        # Check column
        col = []
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] in col:
                    return False
                else:
                    col.append(board[j][i])

        # Check box
