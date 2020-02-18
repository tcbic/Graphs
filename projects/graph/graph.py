"""
Simple graph implementation...
"""
from util import Stack, Queue  # These may come in handy.

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Make an empty queue.
        queue = Queue()

        # Make an empty set to store the visited nodes.
        visited = set()

        # Add the starting vertex id to the queue.
        queue.enqueue(starting_vertex)

        # How do we know we can stop?
        # If the queue is not empty, there are more nodes to visit.
        while queue.size() > 0:
            # Dequeue the first vertex.
            current_node = queue.dequeue()
            # Check if it has been visited.
            if current_node not in visited:
                # If not, mark as visited.
                visited.add(current_node)
                print(current_node)
                # Get its neighbors.
                edges = self.get_neighbors(current_node)
                # Put them in line to be visited.
                for edge in edges:
                    queue.enqueue(edge)          

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Make an empty stack.
        stack = Stack()

        # Make an empty set to store the visited nodes.
        visited = set()

        # Push the starting vertex id to the stack.
        stack.push(starting_vertex)

        # While the stack is not empty, there are more nodes to visit.
        while stack.size() > 0:
            # Pop the first vertex.
            current_node = stack.pop()

            # Check if it has been visited.
            if current_node not in visited:
                # If not, mark it as visited.
                visited.add(current_node)
                print(current_node)
                # Get its neighbors.
                edges = self.get_neighbors(current_node)
                # Push all neighbors to the top of the stack.
                for edge in edges:
                    stack.push(edge)

    # You can only do depth first traversal in a recursive way, not breadth.
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # BASE CASE
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        edges = self.get_neighbors(starting_vertex)

        for child_vertex in edges:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Make an empty queue.
        queue = Queue()

        # Make an empty set to store the visited nodes.
        visited = set()

        # Push the starting vertex id to the stack.
        # Use a list as our path.
        queue.enqueue([starting_vertex])

        # While the stack is not empty, there are more nodes to visit.
        while queue.size() > 0:
            # Pop the first vertex.
            path = queue.dequeue()
            current_node = path[-1]

            # Check if it has been visited...
            if current_node not in visited:
                # and it's the destination vertex.
                if current_node == destination_vertex:
                    return path
                
                visited.add(current_node)
                
                # Get its neighbors.
                edges = self.get_neighbors(current_node)
                
                for edge in edges:
                    # Copy path to avoid pass by reference bug.
                    new_path = list(path)
                    new_path.append(edge)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Make an empty stack.
        stack = Stack()

        # Make an empty set to store the visited nodes.
        visited = set()

        # Push the starting vertex id to the stack.
        # Use a list as our path.
        stack.push([starting_vertex])

        # While the stack is not empty, there are more nodes to visit.
        while stack.size() > 0:
            # Pop the first vertex.
            path = stack.pop()
            current_node = path[-1]

            # Check if it has been visited...
            if current_node not in visited:
                # and it's the destination vertex.
                if current_node == destination_vertex:
                    return path
                
                visited.add(current_node)
                
                # Get its neighbors.
                edges = self.get_neighbors(current_node)
                
                for edge in edges:
                    # Copy path to avoid pass by reference bug.
                    new_path = list(path)
                    new_path.append(edge)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # BASE CASE
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        else:
            edges = self.get_neighbors(starting_vertex)

            for child_vertex in edges:
                if child_vertex not in visited:
                    new_path = self.dfs_recursive(child_vertex, destination_vertex, visited, path) 
                    if new_path:
                        return new_path
            return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Print graph vertices.")
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Runnung BFT.")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Running DFT.")
    graph.dft(1)
    print("Running DFT recursive.")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running BFS.")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running DFS.")
    print(graph.dfs(1, 6))
    print("Running DFS recursive.")
    print(graph.dfs_recursive(1, 6))
