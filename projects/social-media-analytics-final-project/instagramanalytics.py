
from networkanalytics import NetworkAnalytics

if __name__ == '__main__':
    na = NetworkAnalytics()
    na.populate_graph(['miranda', 'danny', 'rick', 'rebecca', 'oscar', 'ely'])
    na.add_edge('miranda', 'danny')
    na.add_edge('miranda', 'rick')
    print na.g