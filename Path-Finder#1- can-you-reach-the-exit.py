#https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python
def path_finder(maze):
    maze = [list(row) for row in maze.split("\n")]
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '.'
    def explore(x, y):
        if not is_valid(x, y):
            return False
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return True
        maze[x][y] = 'W' 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if explore(x + dx, y + dy):
                return True
        return False
    return explore(0, 0)