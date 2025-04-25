import heapq

class VacuumAgent:
    def __init__(self, start_pos):
        self.position = start_pos

    def act(self, room):
        goal = room.find_nearest_dirt(self.position)
        if not goal:
            return

        path = self.a_star_search(room, self.position, goal)
        if path and len(path) > 1:
            self.position = path[1]  # Move to next cell
        if room.grid[self.position[0]][self.position[1]] == 'dirty':
            room.grid[self.position[0]][self.position[1]] = 'clean'

    def a_star_search(self, room, start, goal):
        frontier = [(0, start)]
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                break

            for next_pos in room.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + self.heuristic(goal, next_pos)
                    heapq.heappush(frontier, (priority, next_pos))
                    came_from[next_pos] = current

        if goal not in came_from:
            return []

        path = []
        current = goal
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
