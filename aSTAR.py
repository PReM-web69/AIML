import heapq

# Node and heuristic setup
start = "A"  
goal = "G"   
nodes = {
    "A": {"B": 1, "C": 4},   
    "B": {"D": 2, "E": 5},   
    "C": {"E": 1},           
    "D": {"G": 3},           
    "E": {"G": 1},           
    "G": {}                  
}

# Heuristic values (estimated cost to reach the goal)
heuristic = {
    "A": 6,  # Estimated cost to reach G from A
    "B": 5,
    "C": 2,
    "D": 1,
    "E": 1,
    "G": 0  
}

open_list = []
closed_list = set()

# Starting node setup
heapq.heappush(open_list, (heuristic[start], 0, start))  # (f_score, g_score, node)
g_score = {start: 0}  
came_from = {}  # To reconstruct the path

while open_list:
    current_f, current_g, current_node = heapq.heappop(open_list)

    if current_node == goal:
        path = []
        while current_node in came_from:
            path.append(current_node)
            current_node = came_from[current_node]
        path.append(start)
        path.reverse()
        print("Path found:", path)
        break

    closed_list.add(current_node)

    # Explore neighbors
    for neighbor, cost in nodes[current_node].items():
        if neighbor in closed_list:
            continue

        tentative_g_score = current_g + cost

        
        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
            g_score[neighbor] = tentative_g_score
            f_score = tentative_g_score + heuristic[neighbor]
            heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
            came_from[neighbor] = current_node
else:
    print("no path found")