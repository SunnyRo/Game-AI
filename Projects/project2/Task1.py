# python3
import os


def fractionalKnapsack(profit, weight, capacity):
    """
    @brief: just fractional knapsack
    @param profit: the profit list of objects
    @param weight: the weight list of objects
    @param capacity: the capacity of the knapsack
    @return: the maximum profit and list of objects
    """
    # index = [0, ., n - 1] for n items
    index = list(range(len(profit)))
    # ratios of profit to weight
    ratio = [v / w for v, w in zip(profit, weight)]
    # sort index according to ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    totalProfit = 0
    listItems = []
    for i in index:
        if weight[i] <= capacity:
            totalProfit += profit[i]
            capacity -= weight[i]
            listItems.append([1, profit[i], weight[i]])
        else:
            totalProfit += profit[i] * capacity / weight[i]
            listItems.append([capacity / weight[i], profit[i], weight[i]])
            break
    return totalProfit, listItems


# main
capacity = int(input("Please enter Knapsack capacity: "))
weight = input("Please enter the positive weights of the item(s) in order: ").split()
weight = [int(w) for w in weight]
profit = input("Please enter the profits of the item(s) in order: ").split()
profit = [int(p) for p in profit]
totalProfit, listItems = fractionalKnapsack(profit, weight, capacity)
print("The maximum profit:", totalProfit)
print(
    "The list objects [fraction, profit, weight] that maximize the profit:",
    tuple(listItems),
)
# os.system('pause') #this line is only for executable file to pause the program
