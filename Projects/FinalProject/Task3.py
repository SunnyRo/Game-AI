class node(object):
    def __init__(self, level=None, path=None, bound=None):
        # level of node in decision tree
        self.level = level
        # contains tour at the node
        self.path = path
        # upper bound of max profit in subtree of thise node
        self.bound = bound

    def __str__(self):
        return "level = {}, path = {}, bound = {}".format(
            self.level, self.path, self.bound
        )


def length(node):
    """
    @brief: calculate the total cost to travel to the node
    @param node: the node that is wanted to find the cost
    @return: the cost(length)
    """
    tour = node.path
    return sum([matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])


# function calculate the bound of the node
def bound(node):
    """
    @brief: calculate the bound for the current node
    @param node: the node that is wanted to find the bound
    @return: the bound of the node
    """
    path = node.path
    bound = 0
    # get the last item in path
    last = path[-1]
    # remain is index based
    remainEdges = list(filter(lambda x: x not in path, range(n)))
    # for the edges that are certain
    for i in range(len(path) - 1):
        bound += matrix[path[i]][path[i + 1]]
    # for the last item
    bound += min([matrix[last][i] for i in remainEdges])
    p = [path[0]] + remainEdges
    for j in remainEdges:
        bound += min([matrix[j][i] for i in filter(lambda x: x != j, p)])
    return bound


def travelsalesman(n, matrix):
    """
    @brief: solve the shortest length and optimal tour
    @param n: the number of vertices
    @param matrix: the table
    @return: the shortest length and optimal tour
    """
    priorityQueue = []
    u = node()
    v = node(0, path=[0])
    v.bound = bound(v)
    minLength = float("inf")
    shortestLength = 0
    priorityQueue.append(v)
    while priorityQueue:
        v = priorityQueue.pop(0)
        if v.bound < minLength:
            u.level = v.level + 1
            for i in filter(lambda x: x not in v.path, range(1, n)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == n - 2:
                    # put the last vertex to path
                    l = set(range(1, n)) - set(u.path)
                    u.path.append(list(l)[0])
                    # putting the first vertex at last
                    u.path.append(0)
                    tempLength = length(u)
                    if tempLength < minLength:
                        # update the new min length
                        minLength = tempLength
                        shortestLength = tempLength
                        # update the new optimal tour
                        optimalTour = u.path[:]
                else:
                    u.bound = bound(u)
                    if u.bound < minLength:
                        priorityQueue.append(u)
                u = node(u.level, 0, 0)
        # sort the queue based on bound in increasing order
        priorityQueue = sorted(priorityQueue, key=lambda item: item.bound)
    return shortestLength, optimalTour


# main
with open("input3.txt", "r") as file:
    matrix = [[int(num) for num in line.split(" ")] for line in file]
optimalTour = []
minLength = 0
n = len(matrix)
minLength, optimalTour = travelsalesman(n, matrix)
for i in range(len(optimalTour)):
    optimalTour[i] += 1
print("Optimal Tour = {}".format(optimalTour))
print("Length = {}".format(minLength))
# function calculate the total length of all edges in path.
