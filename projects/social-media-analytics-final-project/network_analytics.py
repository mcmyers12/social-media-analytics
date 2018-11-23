"""TODO"""
from igraph import *


class NetworkAnalytics:

    def __init__(self):
        self.g = Graph()
        self.num_vertices = 0

    # --------Graph access, manipulation, and display-------- #
    '''Adds vertices to the graph with labels
       Param: list of strings representing vertex labels'''
    def add_vertices(self, vertex_labels):
        self.num_vertices = len(vertex_labels)

        for label in vertex_labels:
            self.g.add_vertex(label) #, label=label)

    '''Adds vertex to the graph with label
       Param: strings representing vertex label'''
    def add_vertex(self, vertex_label):
        self.g.add_vertex(vertex_label)

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

    # --------Graph analytics methods-------- #
    '''Computes the betweenness centrality score of all agents in the graph
       Returns a list of betweenness centralities'''
    def get_betweenness(self):
        denominator = ((self.num_vertices - 1.0) * (self.num_vertices - 2.0)) / 2.0
        return [round(x / denominator, 3) for x in g.betweenness()]

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

    def display_graph(self):
        plot(self.g)


