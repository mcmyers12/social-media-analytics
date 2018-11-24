# -*- coding: utf-8 -*-

"""find active discussions on a particular hashtag"""

from network_analytics import NetworkAnalytics
from pprint import pprint as pp
import urllib2
import json


class InstagramAnalytics:

    def __init__(self):
        self.na = NetworkAnalytics()

    '''Gets the post owners of a given hashtag'''
    def get_hashtag_post_owners(self, htag):
        owners = []
        search_url = 'https://www.instagram.com/explore/tags/' + htag + '/?__a=1'
        # search_url = 'https://api.instagram.com/tags/snowy/media/recent'

        contents = urllib2.urlopen(search_url).read()
        results = json.loads(contents)
        edges = results['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        for edge in edges:
            node = edge['node']
            owner_id = node['owner']['id']
            if owner_id not in owners:
                owners.append(owner_id)

        return owners

    '''Adds hashtag and owners as vertices
       Adds an edge between each owner and corresponding hashtag'''
    def add_hashtag_connections(self, tag, tag_color, vertices, vertices_color):
        self.na.add_vertex(tag, tag_color)
        self.na.add_vertices(vertices, vertices_color)

        for name in vertices:
            self.na.add_edge(tag, name)

    '''Given a dict formatted as follows, build a graph
       net = {
        'acro': {'tagColor': 'purple', 'ownerColor': 'lavender'},
        'partneryoga': {'tagColor': 'blue', 'ownerColor': 'lightblue'}}'''
    def build_network(self, network):
        for tag in network:
            owners = self.get_hashtag_post_owners(tag)
            self.add_hashtag_connections(tag, network[tag]['tagColor'], owners, network[tag]['ownerColor'])


if __name__ == '__main__':
    net = {
        'ポアント': {'tagColor': 'purple', 'ownerColor': 'lavender'},  # pointe
        'ダンス': {'tagColor': 'magenta', 'ownerColor': 'lightpink'},  # dance
        'バレエ': {'tagColor': 'blue', 'ownerColor': 'lightblue'}  # ballet
    }

    ia = InstagramAnalytics()
    ia.build_network(net)
    ia.na.display_graph()

