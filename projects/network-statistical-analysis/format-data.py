from pprint import pprint as pp

def createAdjacencyMatrix(nodes, edgesFile, matrixFile):
    matrix = [[0] + nodes]
    for node in nodes:
        matrix.append([node] + [0 for i in range(len(nodes))])
    with open(edgesFile, 'r') as f:
        for line in f:
            edges = line.split()
            edge1 = int(edges[0])
            edge2 = int(edges[1])            
            matrix[edge1][edge2] = 1
    
    return matrix


def getNodes(featuresFile):
    nodes = []
    with open(featuresFile, 'r') as f:
        for line in f:
            node = line.split()[0]
            if node not in nodes:
                nodes.append(node)
    return nodes
    

def getFeatures(nodes, featureNames, featuresFile):
    features = [['id'] + featureNames]
    with open(featuresFile, 'r') as f:
        for line in f:
            features.append(line.split())
    
    return features
            
            
def getFeatureNames(featureNamesFile):
    featureNames = []
    with open(featureNamesFile, 'r') as f:
        for line in f:
            splitLine = line.split()
            featureName = splitLine[1].replace('anonymized', '') + splitLine[-1]
            featureNames.append(featureName)
    
    return featureNames


def main():
    nodes = getNodes('0.feat')
    matrix = createAdjacencyMatrix(nodes, '0.edges', 'adjacency-matrix.txt')
    featureNames = getFeatureNames('0.featnames')
    getFeatures(nodes, featureNames, '0.feat')
        
    '''for row in matrix:
        print(row)'''

main()