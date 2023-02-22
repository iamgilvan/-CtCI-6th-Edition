from ast import List
import unittest
#O (P + D)
class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = {}
        self.dependencies = 0

    def addNeighbor(self, node):
        if not node.name in self.map.keys():
            self.children.append(node)
            self.map[node.name] = node
            self.increment()

    def increment(self):
        self.dependencies += 1

    def decrement(self):
        self.dependencies -= 1

    def getName(self):
        return self.name

    def getNumberDependencies(self):
        return self.dependencies

    def getChildren(self):
        return self.children

class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def getOrCreateNode(self, name):
        if not name in self.map.keys():
            node = Project(name)
            self.nodes.append(node)
            self.map[name] = node
        return self.map[name]

    def addEdge(self, startName, endName):
        start = self.getOrCreateNode(startName)
        end = self.getOrCreateNode(endName)
        start.addNeighbor(end)

    def getNodes(self):
        return self.nodes


def addNonDependent(order, projects, offset):
    # A helper function to insert projects with zero dependencies into the order
    # array, start at index offset.
    for project in projects:
        if project.getNumberDependencies() == 0:
            order[offset] = project
            offset += 1

    return offset



def orderProjects(projects):
    # Return a list of projects in correct build order
    order = [None] * len(projects)

    # Add "roots" to the build order first
    endOfList = addNonDependent(order, projects, 0)

    toBeProcessed = 0
    while toBeProcessed < len(order):
        current = order[toBeProcessed]

        # We have a circular dependency since we there are no remaining projects with zero dependencies
        if not current:
            return None

        # remove myself as dependency
        children = current.getChildren()
        for child in children:
            child.decrement()

        # Add children the have no one depending on them
        endOfList = addNonDependent(order, children, endOfList)
        toBeProcessed += 1
    return order

def buildGraph(projects, dependencies) -> Graph:
    # build the graph, adding the edge (a,b) if b is dependent on a.
    # Assume a pair is listed in "build order". The pair (a,b) in dependencies indicates that b
    # depends on a and a must be built before b.
    graph = Graph()
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.addEdge(first, second)
    return graph

def findBuildOrder(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return orderProjects(graph.getNodes())


def determine_build_order(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built = True
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")
    return build_order

class NoValidBuildOrderError(Exception):
    pass

class TestCase(unittest.TestCase):
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [
        ("a", "d"),
        ("f", "b"),
        ("b", "d"),
        ("f", "a"),
        ("d", "c")
    ]
    expected = ["e", "f", "b", "a", "d", "c"]

    def test_build_order(self):
        order = determine_build_order(self.projects, self.dependencies)
        print(order)
        assert self.expected == order, "Sometimes we don't have the correct order in terms of projects without dependencies due to line 109."

if __name__ == "__main__":
    unittest.main()