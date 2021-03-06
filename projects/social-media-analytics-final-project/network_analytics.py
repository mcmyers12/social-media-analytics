"""TODO"""
from igraph import *


class NetworkAnalytics:

    def __init__(self):
        self.g = Graph()
        self.num_vertices = 0

    # --------Graph access, manipulation, and display-------- #
    '''Adds vertices to the graph with labels
       Param: list of strings representing vertex labels'''
    def add_vertices(self, vertex_labels, color):
        self.num_vertices = len(vertex_labels)

        '''self.g.vs['color'] = [color] * self.num_vertices
        pp(color)'''

        for label in vertex_labels:
            try:
                self.get_vertex_by_name(label)
                self.get_vertex_by_name(label)['color'] = 'gray'
            except ValueError:
                self.g.add_vertex(label, color=color) #, label=label)

    '''Adds vertex to the graph with label
       Param: strings representing vertex label'''
    def add_vertex(self, vertex_label, color):
        self.g.add_vertex(vertex_label, label=vertex_label, color=color)

    '''Adds an edge to the graph given two vertex names'''
    def add_edge(self, name1, name2):
        self.g.add_edge(name1, name2)

    '''Displays a plot of the graph'''
    def display_graph(self):
        plot(self.g)

    '''Returns a vertex given a vertex name'''
    def get_vertex_by_name(self, name):
        return self.g.vs.find(name)

    '''Returns a vertex given a vertex index'''
    def get_vertex_by_index(self, index):
        return self.g.vs.find(index)

    '''Displays the graph'''
    def display_graph(self):
        plot(self.g)

    # --------Graph analytics methods-------- #
    '''Computes the betweenness centrality score of all agents in the graph
       Returns a list of betweenness centralities'''
    def get_betweenness(self):
        denominator = ((self.num_vertices - 1.0) * (self.num_vertices - 2.0)) / 2.0
        return [round(x / denominator, 3) for x in self.g.betweenness()]

    '''Computes the closeness centrality score of all agents in the graph
       Returns a list of closeness centralities'''
    def get_closeness(self):
        return [round(x, 3) for x in self.g.closeness()]

    '''Computes degree centrality for each agent in the graph
       Returns a list of degree centralities'''
    def calculate_degree_centralities(self):
        return [x / (self.num_vertices - 1.0) for x in self.g.degree()]

    '''Returns the density of the graph'''
    def get_density(self):
        return self.g.density()

    '''Returns the diameter of the graph'''
    def get_diameter(self):
        return self.g.diameter()

    '''Returns the common elements between two lists'''
    @staticmethod
    def get_common_elements(list_a, list_b):
        a_set = set(list_a)
        b_set = set(list_b)
        if a_set & b_set:
            return a_set & b_set
        return []


