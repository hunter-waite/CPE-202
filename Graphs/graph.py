from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search
import re

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.previous = None
        self.color = None

    def is_visited(self):
        return self.visited

    '''def __repr__(self):
        ret_str = ''
        ret_str = ret_str + self.id + ' [ '
        for i in range(len(self.adjacent_to)):
            ret_str = ret_str + self.adjacent_to[i].id + ' '
        return(ret_str + ']')'''

    def __eq__(self,other):
        if self.id == other.id:
            return True
        return(False)


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        self.graph = {}

        infile = open(filename,'r')
        s = infile.read()
        l = re.split("\n| ",s)
        if l[0] == '':
            l =[]

        if len(l) != 0:
            for i in range(0,len(l),2):
                if str(l[i]) != '':
                    key1 = str(l[i])
                    key2 = str(l[i+1])
                    self.add_vertex(key1)
                    self.add_vertex(key2)
                    self.add_edge(key1,key2)
        infile.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if not key in self.graph:
            self.graph[key] = [Vertex(key),[]]

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        try:
            return self.graph[key][0]
        except:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        vertex1 = self.get_vertex(v1)
        vertex2 = self.get_vertex(v2)
        vertex1.adjacent_to.append(vertex2)
        vertex2.adjacent_to.append(vertex1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        ret_list = []
        for i in self.graph:
            ret_list.append(self.graph[i][0].id)
        ret_list.sort()
        return ret_list

    def all_unvisited(self):
        '''Returns true if all the vertices in the graph have been visited, returns false
           otherwise'''
        for i in self.graph:
            if self.graph[i][0].visited == False:
                return False
        return True

    def all_unvisited_in_graph(self):
        '''Returns true if all the vertices in the graph have been visited, returns false
           otherwise'''
        for i in self.graph:
            if self.graph[i][0].visited == False:
                return self.graph[i][0]
        return None

    def adjacent_verts_visited(self,vert):
        '''Returns true if all the adjacent vertices to the given vertez have been visited'''
        for i in range(len(vert.adjacent_to)):
            if not vert.adjacent_to[i].is_visited():
                return False
        return True

    def unvisited_adjacent_verts(self,vert):
        '''Returns a list of all the unvisited vertices ids of a vertex'''
        ret_list = []
        for i in range(len(vert.adjacent_to)):
            if vert.adjacent_to[i].visited == False:
                ret_list.append(vert.adjacent_to[i].id)
        return ret_list

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        #creates a stack to be used for the depth first search
        stack = Stack(50)
        #gets all the vertices in the graph
        vertices = self.get_vertices()

        if len(vertices) == 0:
            return  []
        #makes sure all the vertices are unvisted
        for v in vertices:
            self.get_vertex(v).visited = False
        #pushed the first value onto the stack
        stack.push(vertices[0])
        current_vert = self.get_vertex(vertices[0])
        current_vert.visited = True
        current_vert.previous = current_vert
        l = []
        final_list = []
        #l.append(current_vert.id)
        while not self.all_unvisited():
            #print('curr ' + current_vert.id + ' prev ' + current_vert.previous.id)
            if not self.adjacent_verts_visited(current_vert):
                temp = current_vert
                current_vert = self.get_vertex(min(self.unvisited_adjacent_verts(current_vert)))
                current_vert.visited = True
                current_vert.previous = temp
            elif not current_vert.previous == current_vert:
                l.append(current_vert.id)
                current_vert = current_vert.previous
            else:
                l.append(current_vert.id)
                l.sort()
                final_list.append(l)
                current_vert = self.all_unvisited_in_graph()
                current_vert.previous = current_vert
                current_vert.visited = True
                l = []

        while current_vert.previous != current_vert:
            l.append(current_vert.id)
            current_vert = current_vert.previous
        l.append(current_vert.id)
        l.sort()
        final_list.append(l)
        return final_list

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        q = Queue(len(self.get_vertices()))
        verts = self.conn_components()
        if len(verts) == 0:
            return False
        for i in range(len(verts)):
            q.enqueue(verts[i][0])
            temp = self.get_vertex(verts[i][0])
            temp.color = 'blue'
            while not q.is_empty():
                v = self.get_vertex(q.dequeue())
                adj = v.adjacent_to
                for x in adj:
                    if x.color == None:
                        q.enqueue(x.id)
                    if x.color == v.color:
                        return False
                    else:
                        if v.color == 'blue':
                            x.color = 'red'
                        else:
                            x.color = 'blue'
        return True
