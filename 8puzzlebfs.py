
import copy

startstate =[[1, 2, 3],
             [8, 5, 6],
             [4, 7, '_']]
goalstate = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, '_']]

visited = []
queue = [startstate]
nextStates = []

def getNext(node):
    global nextStates
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

def printFun(state):
  for row in state:
    print(row)
  print()


while(len(queue)>0):
    node = queue.pop(0)
    printFun(node)
    if(node == goalstate):
            break
    neighbours = getNext(node)
    for neighbour in neighbours:
        if neighbour not in visited:
            queue.append(neighbour)
            visited.append(neighbour)