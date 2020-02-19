
# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are connected 
# to the north, south, east or west. 

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x+1] == 1:
        neighbors.append((x+1, y))

    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    if y < len(matrix) - 1 and matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    return neighbors

def dfs(x, y, matrix, visited):
    stack = Stack()
    stack.push((x, y))
    while stack.size() > 0:
        current_node = stack.pop()
        if not visited[current_node[1]][current_node[0]]:
            visited[current_node[1]][current_node[0]] = True
            for neighbor in get_neighbors(current_node[0], current_node[1], matrix):
                stack.push(neighbor)
    return visited

def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


# For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print_matrix(islands)

# Returns 4 
island_counter(islands)