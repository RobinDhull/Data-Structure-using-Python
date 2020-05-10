''' A person can climb either 1 stair or 2 stairs or 3 stairs at a time. Count the number of ways, the person can reach the top.'''

def countPaths(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    return countPaths(steps - 1) + countPaths(steps - 2) + countPaths(steps - 3)

steps = int(input("Enter the number of steps : "))
res = countPaths(steps)
print(res)
