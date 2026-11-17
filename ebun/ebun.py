import osmnx as ox  # pyright: ignore[reportMissingImports]
import networkx as nx
import heapq
import os
import time
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]




def generate_path(came_from, current):
    # Reconstructs the path from the goal node back to the start
    path = [current]
    while current in came_from and came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path




def weighted_a_star(graph, start, goal, weight=1.5):
    # Executes a Weighted A* search using an atomic state representation
    # The state is only the geographic node ID.
    start_time = time.time()


    # Priority queue for the frontier: stores tuples of (f_score, node_id)
    frontier = []
    heapq.heappush(frontier, (0, start))


    came_from = {start: None}
    g_score = {start: 0}


    # Metrics to track for the presentation slide
    nodes_expanded = 0
    max_frontier_size = 1


    while frontier:
        # Update maximum frontier size metric
        if len(frontier) > max_frontier_size:
            max_frontier_size = len(frontier)


        current_f, current_node = heapq.heappop(frontier)
        nodes_expanded += 1


        # Check if goal is reached
        if current_node == goal:
            run_time = time.time() - start_time
            path = generate_path(came_from, current_node)
            return path, run_time, nodes_expanded, max_frontier_size


        # Expand neighbors
        for neighbor in graph.neighbors(current_node):
            # Get the physical walking distance between the current node and neighbor
            edge_data = graph[current_node][neighbor][0]
            edge_length = edge_data.get('length', 1.0)


            tentative_g_score = g_score[current_node] + edge_length


            # If a better path is found, or neighbor is unvisited
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score


                # Retrieve the straight-line heuristic and calculate f(n)
                h_score = graph.nodes[neighbor].get('heuristic', 0)
                f_score = tentative_g_score + (weight * h_score)


                heapq.heappush(frontier, (f_score, neighbor))


    # Return if no path is found
    return None, time.time() - start_time, nodes_expanded, max_frontier_size




if __name__ == "__main__":
    # 1. Download the Campus Graph
    place_name = "Texas Tech University, Lubbock, Texas, USA"
    graph_file = "texas_tech.graphml"
    if os.path.exists(graph_file):
        # Load the saved map so the script works when OpenStreetMap is busy
        print("Loading saved Texas Tech campus map...")
        G = ox.io.load_graphml(graph_file)
    else:
        print("Downloading Texas Tech campus map from OpenStreetMap...")
        # Uses OpenStreetMap data for walking paths
        G = ox.graph_from_place(place_name, network_type='walk')
        ox.io.save_graphml(G, graph_file)


    # Define start and goal Nodes
    nodes = list(G.nodes)
    start_node = nodes[0]   # will input test cases later
    goal_node = nodes[-1]   # will input test cases later


    # Calculate the heuristic
    # Get the coordinates of the goal node
    goal_y = G.nodes[goal_node]['y']
    goal_x = G.nodes[goal_node]['x']


    # Add the straight-line distance to the goal for every node in the graph
    for node, data in G.nodes(data=True):
        # ox.distance.great_circle_vec(lat1, lon1, lat2, lon2)
        dist = ox.distance.great_circle(data['y'], data['x'], goal_y, goal_x)
        data['heuristic'] = dist


    # Run the Weighted A* Model (Aggressive weighting)
    print("\nRunning Weighted A* Search...")
    weight_value = 1.5
    path, run_time, nodes_expanded, max_frontier = weighted_a_star(G, start_node, goal_node, weight=weight_value)


    # Actual results for the model
    print("\n--- WEIGHTED A* METRICS ---")
    print(f"Run Time:          {run_time:.4f} seconds")
    print(f"Nodes Expanded:    {nodes_expanded}")
    print(f"Max Frontier Size: {max_frontier}")
    print(f"Path Length:       {len(path)} nodes")


    #  Generating path in matplotlib
    if path:
        # Set show=False and close=False so we can modify the plot before displaying it
        fig, ax = ox.plot_graph_route(
            G,
            path,
            route_color='blue',
            route_linewidth=3,
            node_size=0,
            show=False,
            close=False
        )
        # Add the title using matplotlib directly
        plt.title(f"Weighted A* Route (Weight = {weight_value})")
        plt.show()
    else:
        print("No valid path found between the start and goal nodes.")
