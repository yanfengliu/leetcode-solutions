# On a 2-dimensional grid, there are 4 types of squares:

# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

# Example 1:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:

# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.

# https://leetcode.com/problems/unique-paths-iii/

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row = len(grid)
        num_col = len(grid[0])
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    end = [i, j]
        return self.uniquePaths(grid, start, end)
        
    def uniquePaths(self, grid, start, end):
        if start == end:
            return 0
        
        if (start[0] - 1 == end[0] and start[1] == end[1] and self.check_grid(grid)):
            return 1
        if (start[0] + 1 == end[0] and start[1] == end[1] and self.check_grid(grid)):
            return 1
        if (start[0] == end[0] and start[1] - 1 == end[1] and self.check_grid(grid)):
            return 1
        if (start[0] == end[0] and start[1] + 1 == end[1] and self.check_grid(grid)):
            return 1
        
        num_row = len(grid)
        num_col = len(grid[0])
        total = 0
        if start[0]-1 >= 0 and grid[start[0]-1][start[1]] != -1:
            grid_copy = copy.deepcopy(grid)
            grid_copy[start[0]][start[1]] = -1
            grid_copy[start[0]-1][start[1]] = 1
            start_copy = copy.deepcopy(start)
            start_copy[0] -= 1
            total += self.uniquePaths(grid_copy, start_copy, end)
            
        if start[0]+1 < num_row and grid[start[0]+1][start[1]] != -1:
            grid_copy = copy.deepcopy(grid)
            grid_copy[start[0]][start[1]] = -1
            grid_copy[start[0]+1][start[1]] = 1
            start_copy = copy.deepcopy(start)
            start_copy[0] += 1
            total += self.uniquePaths(grid_copy, start_copy, end)
            
        if start[1]-1 >= 0 and grid[start[0]][start[1]-1] != -1:
            grid_copy = copy.deepcopy(grid)
            grid_copy[start[0]][start[1]] = -1
            grid_copy[start[0]][start[1]-1] = 1
            start_copy = copy.deepcopy(start)
            start_copy[1] -= 1
            total += self.uniquePaths(grid_copy, start_copy, end)
            
        if start[1]+1 < num_col and grid[start[0]][start[1]+1] != -1:
            grid_copy = copy.deepcopy(grid)
            grid_copy[start[0]][start[1]] = -1
            grid_copy[start[0]][start[1]+1] = 1
            start_copy = copy.deepcopy(start)
            start_copy[1] += 1
            total += self.uniquePaths(grid_copy, start_copy, end)
            
        return total
    
    def check_grid(self, grid):
        already_start = 0
        already_end = 0
        num_row = len(grid)
        num_col = len(grid[0])
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 0:
                    return False
                elif grid[i][j] == 1 and already_start == 0:
                    already_start = 1
                elif grid[i][j] == 2 and already_end == 0:
                    already_end = 1
                elif grid[i][j] != -1 and already_start and already_end:
                    return False
        return True