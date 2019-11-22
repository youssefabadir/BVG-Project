# BVG-Project

# Description of the problem:
If someone want to know the path from one U-Bahn station to another U-Bahn station.

# Data Structure:
We used search tree and lists

# Search Algorithms:
First search algorithm is Breadth First Search
We insert the first station and then check it's children if one of them is the destination station
We keep expanding the tree level by level until we reach a goal or traverse the whole tree which means there is no path from departure station to the destination station

Second search algorithm is Depth First Search
same as Breadth First Search however, we don't traverse the tree level by level we traverse the tree branch by branch

Third search algorithm is Greedy Search
We search by the heuristic function which is the actual cost between the two stations
Greedy check all the stations available stations to expand and expand the node with the least cost heuristic function

# Comparison:
BFS and Greedy are optimal 
DFS is the one with the most expanded nodes 
Greedy is the one with the lest expanded nodes
All three searches are complete
Greedy is the efficient search among them as it expand the least number of nodes
