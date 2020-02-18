"""
Simple graph implementation
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
        # Make a queue.
        queue = Queue()

        # Make a set for the visited nodes.
        visited = set()

        # Put the starting node in line.
        queue.enqueue(starting_vertex)

        # How do we know we can stop?
        # If the queue is not empty, there are more nodes to visit.
        while queue.size() > 0:
            # Get the next node out of line.
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
        # Make a stack.
        stack = Stack()

        visited = set()

        # Put the starting node on top of the stack.
        stack.push(starting_vertex)

        # If the stack is not empty, there are more nodes to visit.
        while stack.size > 0:
            # Get the next node off the top of the stack.
            current_node = stack.pop()

            # Check if it has been visited.
            if current_node not in visited:
                # If not, mark it as visited.
                visited.add(current_node)
                print(current_node)
                # Get its neighbors.
                edges = self.get_neighbors(current_node)
                # Stack them on the stack to be visited.
                for edge in edges:
                    stack.push(edge)

    # You can only do depth first traversal in a recursive way.
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Make a queue.
        queue = Queue()
        # Make a set for visited.
        visited = set()

        # Enqueue a path to the starting vertex.

        # While the queue isn't empty:

            # Dequeue the next path.
            # Current node is the last thing in the path.

            # Check if it's the target (aka the destination vertex.)
            # If so, return the path.

            # Else, mark this as visited.
            # Get the neighbors.
            # Copy the path, add the neighbor to the copy.
            # For each one, add a path to it to our queue.


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
