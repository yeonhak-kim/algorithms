# Word Search (leetcode)

# Backtrack
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(visited:set(), x:int, y:int, i_th:int) -> bool:
            nonlocal N
            nonlocal word
            nonlocal board
            # base case
            if i_th == N - 1:
                return True
            # adjacents
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            # move to next possible neighbor
            for neighbor in neighbors:
                row, col = neighbor
                # condition checks
                if 0 <= row < len(board) and 0 <= col < len(board[0]):
                    if (row, col) not in visited and i_th + 1 < N and board[row][col] == word[i_th + 1]:
                        # backtrack
                        visited.add((row, col))
                        if backtrack(visited, row, col, i_th + 1):
                            return True
                        visited.discard((row, col))
            # return
            return False
        
        # initialize and search starting points
        N = len(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(set(((i, j), -1)), i, j, 0):
                    return True
        
        return False