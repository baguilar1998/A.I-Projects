from Queue import Queue
from Stack import Stack

# Graph data structure that works for a single graph
# and not for multiple graphs

class AdjList:

    def __init__(self):
        self.graph = {}
        self.startVertex = None

    def addVertex(self,vertex):
        if vertex not in self.graph.items():
            self.graph[vertex] = []
        if self.startVertex is None:
            self.startVertex = vertex

    def addEdge(self,vertex1, vertex2):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return
        adjList = self.graph[vertex1]
        if vertex2 not in adjList:
            adjList.append(vertex2)

    def removeVertex(self,vertex):
        del self.graph[vertex]
        for v in self.graph.items():
            adjList = self.graph[v]
            for w in adjList:
                if w == vertex:
                    adjList.remove(w)
        
    def removeEdge(self,vertex1,vertex2):
        adjList = self.graph[vertex1]
        for v in adjList:
            if v == vertex2:
                adjList.remove(v)
                return

    def dfs(self,vertex):
        seen = set()
        s = Stack()
        s.push(self.startVertex)
        while not s.empty():
            v = s.pop()
            if vertex == v:
                print("Vertex Found")
                return
            seen.add(v)
            adjList = self.graph[v]
            for w in adjList:
                if w not in seen and not s.contains(w):
                    s.push(w)
        print("Vertex not found")
        return
    
    def recursive_dfs(self,vertex):
        seen = set()
        vertexFound = self.recursive_traversal(self.startVertex,vertex,seen)
        if vertexFound:
            print("Vertex Found")
        else:
            print("Vertex not found")
    
    def recursive_traversal(self,currentVertex,vertex,seen):
        if currentVertex == vertex:
            return True
        seen.add(currentVertex)
        adjList = self.graph[currentVertex]
        for v in adjList:
            if v not in seen:
                vertexFound = self.recursive_traversal(v,vertex,seen)
                if vertexFound:
                    return True
        return False

    
    def bfs(self,vertex):
        seen = set()
        q = Queue()
        q.enqueue(self.startVertex)
        while not q.empty():
            v = q.dequeue()
            if vertex == v:
                print("Vertex Found")
                return
            seen.add(v)
            adjList = self.graph[v]
            for w in adjList:
                if w not in seen and not q.contains(w):
                    q.enqueue(w)
        print("Vertex was not found")
        return
    
    def printGraph(self):
        print(self.graph)