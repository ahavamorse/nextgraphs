"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from itertools import chain

"""
How to Solve Almost Any Graph Problem
- Translate problem into graph
- Build graph with code (could be as we go rather than ahead of time)
- Traverse graph

Do BFS
    create a queue
    create a visited set
    add start word to queue (as a path?)
    while queue is not empty
        pop current word off queue
        if word has not been visited
            if current word is end word return path
            add current word to visited set
            add neighbors of current word to queue (as a path?)

DFT
    create a stack
    create a way to keep track of visited vertices
    push starting vertex onto stack
    while stack is not empty
        pop off next vertex
        if vertex has not been visited
            add them to visited
            push neighbors onto stack
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create new key with vertex ID without any edges
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex v1 and v2 in out vertices and add v2 to the edges of v1
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        result = ""
        # create an empty queue and enqueue the starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # create an empty set to track visited vertices
        visited_vertices = set()

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex and dequeue it
            current_vertex = queue.dequeue()

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # print the current vertex
                result += str(current_vertex) + ", "

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # enqueue all the current vertex's neighbors
                for vertex in self.get_neighbors(current_vertex):
                    queue.enqueue(vertex)

        print(result[:len(result) - 2])

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and add the starting vertex
        stack = Stack()
        stack.push(starting_vertex)
        # create an empty set to track visited vertices
        visited_vertices = set()

        result = ""

        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex and pop it
            current_vertex = stack.pop()

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # print the current vertex
                result += str(current_vertex) + ", "

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # push up all the current vertex's neighbors
                for vertex in self.get_neighbors(current_vertex):
                    stack.push(vertex)

        print(result[:len(result) - 2])

    visited_vertices = set()

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex not in self.visited_vertices:
            print(starting_vertex, end=", ")
            self.visited_vertices.add(starting_vertex)

            for vertex in self.get_neighbors(starting_vertex):
                self.dft_recursive(vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the path to starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create an empty set to track visited vertices
        visited_vertices = set()

        shortest_path = None

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex path and dequeue it
            current_path = queue.dequeue()
            # set the current vertex to the last element of the path
            current_vertex = current_path[-1]

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # check if the current vertex is destination
                if current_vertex == destination_vertex:
                    # It is the shortest path so return it
                    return current_path

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # enqueue new paths with each neighbor
                for vertex in self.get_neighbors(current_vertex):
                    # take current path
                    new_path = current_path.copy()
                    # append neighbor to it
                    new_path.append(vertex)
                    # queue up new path
                    queue.enqueue(new_path)

        return shortest_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push the path to starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # create an empty set to track visited vertices
        visited_vertices = set()

        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex path and pop it
            current_path = stack.pop()
            # set the current vertex to the last element of the path
            current_vertex = current_path[-1]

            # check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # check if the current vertex is destination
                if current_vertex == destination_vertex:
                    # if it is stop and return it
                    return current_path

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # push new paths with each neighbor
                for vertex in self.get_neighbors(current_vertex):
                    # take current path
                    new_path = current_path.copy()
                    # append neighbor to it
                    new_path.append(vertex)
                    # queue up new path
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = list()
        path.append(starting_vertex)
        if starting_vertex not in self.visited_vertices:
            if starting_vertex == destination_vertex:
                return path

            self.visited_vertices.add(starting_vertex)

            for vertex in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(vertex, destination_vertex)
                if new_path:
                    path = path.__add__(new_path)
                    return path


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
    graph.visited_vertices = set()
    print()

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
