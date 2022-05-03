# a*bfs

graph = { 
   'A' : [['B', 11],
          ['C', 14],
          ['D', 7]],
   'B' : [['A', 11], 
          ['E', 15]],
   'C' : [['A', 14],
          ['E', 8],
          ['F', 10]],
   'D' : [['A', 7],
          ['F', 25]],
   'E' : [['B', 15],
          ['C', 8],
          ['H', 9]],
   'F' : [['C', 10],
          ['G', 20]],
   'G' : [['F', 20],
          ['H', 10]],
   'H' : [['E', 9],
          ['G', 10]]
}

H = {
    "A" : 40,
    "B" : 32,
    "C" : 25,
    "D" : 35,
    "E" : 19,
    "F" : 17,
    "G" : 0,
    "H" : 10,
}

startstate = 'A'
goalstate = 'G'

queue = [[startstate, 0]]

def fun(ele):
  return ele[1]+H[ele[0][-1]]

while(len(queue)>0):
    print(queue)
    currpath, currcost = queue.pop(0)
    if(currpath[-1] == goalstate):
        print("\nPath: ", currpath, " ( Cost=", currcost, ")")
        break
    for node, cost in graph[currpath[-1]]:
        if node in currpath:
            continue
        queue.append([currpath+node, currcost+cost])
    queue=sorted(queue,key=fun)