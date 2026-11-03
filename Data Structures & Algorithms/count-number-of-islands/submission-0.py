class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited_map = [
            [False] * len(grid[0])
            for _ in range(len(grid))
        ]
        islands = 0
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == "1" and not visited_map[i][j]:
                    self.explore_island(i, j, grid, visited_map)
                    islands += 1
                j += 1
            i += 1
        return islands

    def explore_island(self, i, j, grid, visited_map):
        if grid[i][j] == "0" or visited_map[i][j]:
            return
        else:
            visited_map[i][j] = True
            if i > 0:
                self.explore_island(i-1, j, grid, visited_map)
            if j > 0:
                self.explore_island(i, j-1, grid, visited_map)
            if i < len(grid) - 1:
                self.explore_island(i+1, j, grid, visited_map)
            if j < len(grid[0]) - 1:
                self.explore_island(i, j+1, grid, visited_map)
