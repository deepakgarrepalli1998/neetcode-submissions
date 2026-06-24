class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnsave=[[],[],[],[],[],[],[],[],[]]
        gridsave=[[],[],[],[],[],[],[],[],[]]
        for rowsno in range(9):
            rowcurr=["."]
            for columnsno in range (9):
                if board[rowsno][columnsno] not in rowcurr:
                    rowcurr.append(board[rowsno][columnsno])
                    gridno=int((rowsno// 3) * 3 + (columnsno// 3))
                    if board[rowsno][columnsno] not in columnsave[columnsno]:
                        columnsave[columnsno].append(board[rowsno][columnsno])
                        if board[rowsno][columnsno] not in gridsave[gridno]:
                            gridsave[gridno].append(board[rowsno][columnsno])
                        else:
                            return False
                    elif board[rowsno][columnsno] in columnsave[columnsno]:
                        return False
                elif board[rowsno][columnsno]!=".":
                    return False
                else:
                    continue
        return True
        