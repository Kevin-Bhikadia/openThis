# a*8pz

import copy
from functools import reduce
goalstate = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, '_']]
lgoalstate = reduce(lambda x, y: x+y, goalstate)

def heuristic(state):
    lstate = reduce(lambda x, y: x+y, state)
    cost=0

    for a, b in zip(lstate, lgoalstate):
        if(a!=b):
            cost=cost+1
    return cost

def getNext(node):
    nextStates = []
    for row in range(0, len(node)):
        for col in range(0, len(node[row])):
            if(node[row][col]=='_'):
                break
        else:
            continue
        break

    if(row==0 or row==1):
        a = copy.deepcopy(node)
        a[row][col], a[row+1][col]=a[row+1][col], a[row][col]
        nextStates.append(a)

    if(row==1 or row==2):
        a = copy.deepcopy(node)
        a[row][col], a[row-1][col]=a[row-1][col], a[row][col]
        nextStates.append(a)
    
    if(col==0 or col==1):
        a = copy.deepcopy(node)
        a[row][col], a[row][col+1]=a[row][col+1], a[row][col]
        nextStates.append(a)

    if(col==1 or col==2):
        a = copy.deepcopy(node)
        a[row][col], a[row][col-1]=a[row][col-1], a[row][col]
        nextStates.append(a)
    
    return nextStates

startstate =[[1, 2, 3],
             [8, 5, 6],
             [4, 7, '_']]

queue = [[startstate]]

def orderByCost(queue):
    return sorted(queue, key = lambda x: (len(x)-1)+heuristic([x[-1]]))

while(len(queue)>0):
    currpath = queue.pop(0)
    if(currpath[-1] == goalstate):
        print("success", "\nPath: ")
        for state in currpath:
            print(state,"\n-")
        break
    for node in getNext(currpath[-1]):
        if node in currpath:
            continue
        path = copy.deepcopy(currpath)
        path.append(node)
        queue.append(path)

    queue = orderByCost(queue)
