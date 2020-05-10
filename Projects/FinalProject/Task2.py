class node(object):
        def __init__(self, level = None, profit = None, weight = None, bound = None):
            # level of node in decision tree
            self.level = level
            # profit of nodes on path from root to this node (including this node)
            self.profit = profit
            self.weight = weight
            # upper bound of max profit in subtree of thise node
            self.bound = bound
        def __str__(self):
             return "level = {}, profit = {}, weight = {}, bound = {}".format(self.level, self.profit, self.weight, self.bound)
# bound function 
def bound(node):
    # if weight > capacity return 0 
    if node.weight >= capacity:
        return 0;
    else:
        # init bound on profit by current profit
        profitBound = node.profit
        # start including items from index 1 more to current item index
        i = node.level + 1
        totalWeight = node.weight
        # check index and capacity conditions
        while (i <=  n) and (totalWeight + weight[i] <= capacity):
                totalWeight = totalWeight + weight[i]
                profitBound = profitBound + profit[i]
                i += 1
        # if k is not n, include last item partially for bound
        if  i <= n:
            profitBound = profitBound + (capacity - totalWeight) * profit[i] / weight[i]
            return profitBound
# knapsack function return max profit
def knapsack(n, profit, weight, capacity):
    priorityQueue = []
    v = node(-1,0,0,0) # init v as root node
    u = node()
    maxprofit = 0
    objectList = []
    v.bound = bound(v)
    priorityQueue.append(v)
    while(priorityQueue):
        # remove node with the best bound
        v = priorityQueue.pop(0)
        # if it is starting node, assign level to 0
        if(v.level == -1):
            u.level = 0
        if(v.bound > maxprofit):
            # taking current level's item add current level's weight and value to node v's weight and value
            u.level = v.level +1
            u.weight = v.weight + weight[u.level]
            u.profit = v.profit + profit[u.level]
            # if cumulated weight is less than cap and profit is greater than previous profit
            # then update maxprofit
            if(u.weight <= capacity and u.profit > maxprofit):
                maxprofit = u.profit
            # get the upper bound on profit to decide whether to add u to PO or not
            u.bound = bound(u)

            h = node(u.level,u.profit,u.weight,u.bound)
            # if bound value is greater than profit then only push into PO for further consideration
            if(h.bound >= maxprofit):
                priorityQueue.append(h)
            # do the same thing but without taking the item in knapsack
            u.weight = v.weight
            u.profit = v.profit
            u.bound = bound(u)
            h = node(u.level,u.profit,u.weight,u.bound)
            if h.bound is None:
                h.bound = 0
            if (h.bound >= maxprofit):
                priorityQueue.append(h)
        priorityQueue = sorted(priorityQueue, key=lambda item: item.bound, reverse=True)
        # print("~~~~~~~~~~~priority queue")
        # for i in range(len(priorityQueue)):
        #     print(priorityQueue[i])
    return maxprofit
# main
capacity = int(input('Please enter Knapsack capacity: '))
with open('input2.txt', 'r') as file:
    readLines = [[int(num) for num in line.split(' ')] for line in file]
    tempProfit= readLines[0]
    tempWeight = readLines[1]
# get the ratio of profit / weight array
ratio = [v/w for v, w in zip(tempProfit, tempWeight)]
index = list(range(len(tempProfit)))
# sort the index array in decreasing order
index.sort(key=lambda i: ratio[i], reverse =True)
weight = [] 
profit = [] 
# add weight and profit based on the index
for i in index:
    weight.append(tempWeight[i])
    profit.append(tempProfit[i])
profit.append(0)
weight.append(0)
n = len(weight) - 1
maxProfit = knapsack(n,profit,weight,capacity)
print('Max Profit = {}'.format(maxProfit))