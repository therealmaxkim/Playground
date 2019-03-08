'''
Input
The first line of the input file contains two integers N and M --- number of nodes and number of edges in the graph (0 < N <= 10000, 0 <= M <= 20000). Next M lines contain M edges of that graph --- Each line contains a pair (u, v) means there is an edge between node u and node v (1 <= u,v <= N).

Output
Print YES if the given graph is a tree, otherwise print NO.

Example
Input:
3 2
1 2
2 3

Output:
YES
'''

numbers = input().split()
num_of_nodes = int(numbers[0])
num_of_edges = int(numbers[1])

#check that the # of edges is at most greater # of nodes -1.
if num_of_nodes - 1 != num_of_edges:
    print("NO")

#keep a set with each of the nodes visited. Each node will be unique with a unique number.
nodes_visited = set()
for _ in range(num_of_edges):
    numbers = input().split()
    a = numbers[0]
    b = numbers[1]

    #add the node into the set if not added
    nodes_visited.add(a)
    nodes_visited.add(b)

if len(nodes_visited) == num_of_nodes:
    print("YES")
else:
    print("NO")
