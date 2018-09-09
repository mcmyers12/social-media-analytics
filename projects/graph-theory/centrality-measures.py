from igraph import *
import math


def createGraphA():
    g = Graph()
    g.add_vertices(5)
    g.add_edges([(0,1), (0,2), (0,4), (3,1), (3,2), (4,1)])
    return g


def createGraphB():
    g = Graph()
    g.add_vertices(6)
    g.add_edges([(0, 5), (0, 3), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (3, 5), (4, 5)])
    return g


def getMaxAgents(list):
    m = max(list)
    return [i + 1 for i, j in enumerate(list) if j == m]


def calculateDegreeCentralities(g, numVertices, file):
    degreeCentralities = [x /(numVertices - 1.0) for x in g.degree()]
    file.write('Degree Centrality: \n\t' + str(degreeCentralities))
    file.write('\nAgents with Max Degree Centrality: \n\t' + str(getMaxAgents(degreeCentralities)) + '\n\n')


def createAdjacencyMatrix(g, file):
    file.write('Adjacency Matrix: \n')
    g.write_adjacency(file)


def getBetweenness(g, numVertices):
    denominator = ((numVertices - 1.0) * (numVertices - 2.0)) / 2.0
    return [round(x / denominator, 3) for x in g.betweenness()]


def calculateBetweenness(g, numVertices, file):
    betweenness = getBetweenness(g, numVertices)
    file.write('Betweenness: \n\t' + str(betweenness))
    file.write('\nAgents with Max Betweenness: \n\t' + str(getMaxAgents(betweenness)) + '\n\n')


def calculateCloseness(g, file):
    closeness = [round(x, 3) for x in g.closeness()]
    file.write('Closeness: \n\t' + str(closeness))
    file.write('\nAgents with Max Closeness: \n\t' + str(getMaxAgents(closeness)) + '\n\n')


def calculageDensity(g, file):
    file.write('Density: \n\t' + str(g.density()) + '\n\n')


def calculageDiameter(g, file):
    file.write('Diameter: \n\t' + str(g.diameter()) + '\n\n')


def writeResults(g, file):
    numVertices = g.vcount()
    calculateDegreeCentralities(g, numVertices, file)
    calculateBetweenness(g, numVertices, file)
    calculateCloseness(g, file)
    calculageDensity(g, file)
    calculageDiameter(g, file)
    createAdjacencyMatrix(g, file)


def setAgentNumbers(g):
    agents = []
    for i in range(1, g.vcount() + 1):
        agents.append(i)

    g.vs['agent'] = agents


def setLabels(g):
    numVertices = g.vcount()
    betweenness = getBetweenness(g, numVertices)
    maxAgents = getMaxAgents(betweenness)
    labels = []
    for i in range(1, g.vcount() + 1):
        if i in maxAgents:
            labels.append('agent-' + str(i))
        else:
            labels.append(' ')

    g.vs['label'] = labels


def setColors(g):
    colorDict = {True: 'purple', False: 'teal'}
    g.vs['color'] = [colorDict[agentNumber % 2 == 0] for agentNumber in g.vs['agent']]


def setVertexSize(g):
    numVertices = g.vcount()
    g.vs['size'] = [x * 200 for x in getBetweenness(g, numVertices)]


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def displayNetwork(g):
    setLabels(g)
    setAgentNumbers(g)
    setColors(g)
    setVertexSize(g)
    plot(g)


def main():
    fileA = open('centrality-measures-graph-a.txt', 'w')
    a = createGraphA()
    writeResults(a, fileA)

    fileB = open('centrality-measures-graph-b.txt', 'w')
    b = createGraphB()
    writeResults(b, fileB)

    displayNetwork(b)
    displayNetwork(a)


main()






