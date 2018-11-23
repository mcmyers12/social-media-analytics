"""find active discussions on a particular hashtag"""

from network_analytics import NetworkAnalytics
from pprint import pprint as pp
import urllib2
import json


def get_hashtag_post_owners(htag):
    owners = []
    search_url = 'https://www.instagram.com/explore/tags/' + htag + '/?__a=1'

    #search_url = 'https://api.instagram.com/tags/snowy/media/recent'

    contents = urllib2.urlopen(search_url).read()
    results = json.loads(contents)
    edges = results['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    for edge in edges:
        node = edge['node']
        owner_id = node['owner']['id']
        if owner_id not in owners:
            owners.append(owner_id)

    return owners


def get_common_elements(list_a, list_b):
    a_set = set(list_a)
    b_set = set(list_b)
    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No common elements")


def add_hashtag_connections(na, tag, tag_color, vertices, vertices_color):
    na.add_vertex(tag, tag_color)
    na.add_vertices(vertices, vertices_color)

    for name in vertices:
        na.add_edge(tag, name)


def build_network(network):
    na = NetworkAnalytics()

    for tag in network:
        owners = get_hashtag_post_owners(tag)
        add_hashtag_connections(na, tag, network[tag]['tagColor'], owners, network[tag]['ownerColor'])

    na.display_graph()


if __name__ == '__main__':
    network = {
        'acro': {'tagColor': 'purple', 'ownerColor': 'lavender'},
        'acroyoga': {'tagColor': 'magenta', 'ownerColor': 'lightpink'},
        'ballet': {'tagColor': 'black', 'ownerColor': 'gray'},
        'partneryoga': {'tagColor': 'blue', 'ownerColor': 'lightblue'}
    }
    build_network(network)

