def hanoiTower(disks,source,auxiliary,target):
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'.format(source,target))
        return
    hanoiTower(disks-1,source,target,auxiliary)
    print('Move disk {} from peg {} to peg {}.'.format(disks,source,target))
    hanoiTower(disks-1,auxiliary,source,target)

disks = int(input('Enter number of disks: '))
hanoiTower(disks,'A','B','C')