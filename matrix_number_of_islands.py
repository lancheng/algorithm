import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        if not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = set()
        result = 0
        for i in range(m):
            for j in range(n):
                '''if grid[i][j] == 0:
                    continue

                if (i, j) in visited:
                    continue

                q = collections.deque()
                q.append((i, j))

                while q:
                    next_q = collections.deque()
                    while q:
                        pos = q.popleft()
                        visited.add((pos[0], pos[1]))

                        if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] == 1 and (pos[0] - 1, pos[1]) not in visited:
                            next_q.append((pos[0] - 1, pos[1]))
                        if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] == 1 and (pos[0], pos[1] - 1) not in visited:
                            next_q.append((pos[0], pos[1] - 1))
                        if pos[0] + 1 < m and grid[pos[0] + 1][pos[1]] == 1 and (pos[0] + 1, pos[1]) not in visited:
                            next_q.append((pos[0] + 1, pos[1]))
                        if pos[1] + 1 < n and grid[pos[0]][pos[1] + 1] == 1 and (pos[0], pos[1] + 1) not in visited:
                            next_q.append((pos[0], pos[1] + 1))

                    q = next_q

                result += 1'''
                if grid[i][j] == 1 and (i, j) not in visited:
                    q = set()
                    q.add((i, j))

                    while q:
                        next_q = set()
                        while q:
                            pos = q.pop()
                            visited.add((pos[0], pos[1]))

                            if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] == 1 and (
                                pos[0] - 1, pos[1]) not in visited:
                                next_q.add((pos[0] - 1, pos[1]))
                            if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] == 1 and (
                            pos[0], pos[1] - 1) not in visited:
                                next_q.add((pos[0], pos[1] - 1))
                            if pos[0] + 1 < m and grid[pos[0] + 1][pos[1]] == 1 and (pos[0] + 1, pos[1]) not in visited:
                                next_q.add((pos[0] + 1, pos[1]))
                            if pos[1] + 1 < n and grid[pos[0]][pos[1] + 1] == 1 and (pos[0], pos[1] + 1) not in visited:
                                next_q.add((pos[0], pos[1] + 1))

                        q = next_q

                    result += 1

        return result

if __name__ == '__main__':
    grid = [map(int, x) for x in map(list, raw_input().split())]

    print Solution().numIslands(grid)