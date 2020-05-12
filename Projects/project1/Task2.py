"""
Name:           Son Vo
Course:         CS-3310-SPR20
Project:        1
Due:            03/06/20
Description:    Program Tower of Hanoi problem. Test algorithm with n = 2, 4, 8, 16, 32, ...
"""
#!/usr/bin/python3

import time


def hanoiTower(disks, source, auxiliary, target):
    if disks == 1:
        print("Move disk 1 from peg {} to peg {}.".format(source, target))
        return
    hanoiTower(disks - 1, source, target, auxiliary)
    print("Move disk {} from peg {} to peg {}.".format(disks, source, target))
    hanoiTower(disks - 1, auxiliary, source, target)


disks = int(input("Enter number of disks: "))
start_time = time.time()  # start time
hanoiTower(disks, "A", "B", "C")
# execution time = end time - start time
print("--- %.8f seconds ---" % (time.time() - start_time))
