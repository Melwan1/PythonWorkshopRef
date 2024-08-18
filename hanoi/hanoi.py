def hanoi(disks, pillar_from, pillar_to, pillar_other):
    if disks == 0:
        return 0
    steps = 0
    steps += hanoi(disks - 1, pillar_from, pillar_other, pillar_to)
    print("Disk has been moved from", pillar_from, "to", pillar_to)
    steps += 1
    steps += hanoi(disks - 1, pillar_other, pillar_to, pillar_from)
    return steps
