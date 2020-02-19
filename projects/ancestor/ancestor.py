# When looking for the shortest path --> Breadth First Search (BFS)!

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)

        else:
            return None

    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("That vertex does not exist!")

# Why do we need to build a graph to solve this problem?
# 1) The data is not presented in a way that we can easily manipulate it.
# 2) Most economical in the long run (i.e. dveloper to time) to
# just build out the graph.

# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph.
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])

#         # Build edges in reverse.
#         graph.add_edge(pair[1], pair[0])

#     # Perform BFS. (Storing the path.)
#     queue = Queue()
#     queue.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while queue.size() > 0:
#         path = queue.dequeue()
#         current_node = path[-1]

#         # If the path is longer or equal and the value is smaller,
#         # or if the path is longer:
#         # DO THE THING
#         if (len(path) >= max_path_len and current_node < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = current_node
#             max_path_len = len(path)

#         for neighbor in graph.vertices[current_node]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             queue.enqueue(path_copy)

#     return earliest_ancestor

# 3 steps to solving this:
# 1) Describe the problem in terms of graphs.
# 2) 
# 3) 

# Grab the graph class.


def earliest_ancestor(ancestors, starting_node):

    # Make a graph.
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # Add an edge from the child to the parent.
        graph.add_edge(child, parent)

    # BFS

    # Note: Determined that we could just return the last node
    # to be visited.
    # What if our input node is 8? Should return 4.
    # What if our input is 11? Should return -1.

    queue = Queue()
    # Path of the starting node.
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        current_node = path[-1]

        if len(path) >= longest_path_length and current_node < earliest_ancestor:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = graph.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)
    
    return earliest_ancestor