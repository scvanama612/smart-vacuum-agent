import random

class Room:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['clean' for _ in range(cols)] for _ in range(rows)]
        self.start_pos = (random.randint(0, rows-1), random.randint(0, cols-1))

        for _ in range(rows):
            r, c = random.randint(0, rows-1), random.randint(0, cols-1)
            self.grid[r][c] = 'dirty'

        for _ in range(int(rows*cols*0.15)):
            r, c = random.randint(0, rows-1), random.randint(0, cols-1)
            if (r, c) != self.start_pos:
                self.grid[r][c] = 'wall'

    def get_neighbors(self, pos):
        r, c = pos
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != 'wall':
                    neighbors.append((nr, nc))
        return neighbors

    def find_nearest_dirt(self, pos):
        from collections import deque
        visited = set()
        queue = deque([pos])
        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if self.grid[r][c] == 'dirty':
                return (r, c)
            for neighbor in self.get_neighbors((r, c)):
                if neighbor not in visited:
                    queue.append(neighbor)
        return None

    def has_dirt(self):
        for row in self.grid:
            if 'dirty' in row:
                return True
        return False
