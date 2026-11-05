class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row
        for row in board:
            set_row = set()

            for num in row:

                if num.isdigit() and num in set_row:
                    return False
                
                set_row.add(num)

        # check column
        for col in zip(*board):
            set_col = set()

            for num in col:

                if num.isdigit() and num in set_col:
                    return False
                
                set_col.add(num)

        # check window 3x3
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):

                set_window = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):

                        if board[r][c].isdigit() and board[r][c] in set_window:
                            return False
                        
                        set_window.add(board[r][c])
                        

        return True


# board = [["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#         [".","9","8",".",".",".",".",".","3"],
#         ["5",".",".",".","6",".",".",".","4"],
#         [".",".",".","8",".","3",".",".","5"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".",".",".",".",".",".","2",".","."],
#         [".",".",".","4","1","9",".",".","8"],
#         [".",".",".",".","8",".",".","7","9"]]


board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]


print(Solution().isValidSudoku(board))