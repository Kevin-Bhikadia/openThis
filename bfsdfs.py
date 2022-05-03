# bfs dfs

start=3
end=4
n=6

adj={}

def dfs(start, visited, adj, end):

    print(start, end=' ')
    visited[start]=1
    if(start==end):
        return
    for i in adj[start]:
        if(visited[i]==0):
            visited[i]=1
            dfs(i,visited, adj, end)
        if(visited[end]==1): return
    

def bfs(start, adj, end):
    queue=[start]
    visited=[0]*(n+1)
    visited[start]=1
    while(len(queue)>0):
        curr=queue.pop(0)
        print(curr, end=" ")

        if(curr==end): return

        for i in adj[curr]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=1




for i in range(1,n+1):
    adj[i]=[]


edge=int(input("enter edge "))

for i in range(edge):
    # print("enter a")
    a=int(input())
    # print("enter b")
    b=int(input())
    
    adj[a].append(b)
    adj[b].append(a)
print(adj)
print()
bfs(start, adj, end)
print()
visited=[0]*(n+1)
dfs(start, visited, adj, end)

    






#    1 
#   / \
#   2  3
#   |  | \
#   4  5  6