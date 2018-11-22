"""find active discussions on a particular hashtag"""
from igraph import *
from pprint import pprint as pp
import math


class NetworkAnalytics:

    def __init__(self):
        self.g = Graph()
        self.vertex_map = {}
        self.num_vertices = 0

    '''Add vertices to the graph with labels
       Param: list of strings representing vertex labels'''
    def add_vertices(self, vertex_labels):
        self.num_vertices = len(vertex_labels)
        self.g.add_vertices(self.num_vertices)

        labels = []
        for i in range(self.num_vertices):
            labels.append(vertex_labels[i])

        self.g.vs['label'] = labels

    '''TODO: Add edges to the graph'''
    def add_edges(self):
        pass

    '''Populate graph vertices and edges'''
    def populate_graph(self, vertex_labels):
        self.add_vertices(vertex_labels)
        self.add_edges()

    '''Calculate degree centrality for each agent in the graph
       Returns a list of degree centralities'''
    def calculate_degree_centralities(self):
        return [x / (self.num_vertices - 1.0) for x in self.g.degree()]

    def display_graph(self):
        plot(self.g)


if __name__ == '__main__':
    na = NetworkAnalytics()
    na.populate_graph(['miranda', 'danny', 'rick', 'rebecca', 'oscar', 'ely'])
    na.display_graph()
    pp(na.calculate_degree_centralities())

