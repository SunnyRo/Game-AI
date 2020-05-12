# python3
import os


def knapSack(capacity, weight, profit):
    """
    @brief: calculate the maximum profit knapsack 0/1
    @param capacity: the capacity of knapsack
    @param weight: the weight list of objects
    @param profit: the profit list of objects
    @return: the maximum profit and list of objects
    """
    n = len(profit)
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(profit[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    maxProfit = K[n][capacity]
    listItems = []
    currentCapacity = capacity
    # add selected items to the listItems
    for i in range(n, 0, -1):
        # stop when maxProfit is zero
        if maxProfit <= 0:
            break
        if maxProfit == K[i - 1][currentCapacity]:
            continue
        else:  # maxProfit == profit[i-1]  + K[i-1][w-weight[i-1]]
            # This item is included.
            listItems.append([profit[i - 1], weight[i - 1]])
            # update the new maxProfit and weight
            maxProfit = maxProfit - profit[i - 1]
            currentCapacity = currentCapacity - weight[i - 1]
    return K[n][capacity], listItems


# main
capacity = int(input("Please enter Knapsack capacity: "))
weight = input("Please enter the positive weights of the item(s) in order: ").split()
weight = [int(w) for w in weight]
profit = input("Please enter the profits of the item(s) in order: ").split()
profit = [int(p) for p in profit]
totalProfit, listItems = knapSack(capacity, weight, profit)
print("The maximum profit:", totalProfit)
print("The list objects [profit, weight] that maximize the profit:", tuple(listItems))
# os.system('pause')     #this line is only used for executable file to pause the program
