import os
import heapq
import time


import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt




# Reconstruct the shortest path


def generate_path(came_from, current):
    path = [current]


    while came_from[current] is not None:
        current = came_from[current]
        path.append(current)


    path.reverse()
    return path




# Implementing Dijkstra's Algorithm


def dijkstra(graph, start, goal):


    start_time = time.perf_counter()


    # Priority queue: (distance, node)
    frontier = []
    heapq.heappush(frontier, (0, start))


    # Track shortest known distances
    distances = {start: 0}


    # Track previous nodes
    came_from = {start: None}


    # Performance metrics
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1


    while frontier:


        current_distance, current_node = heapq.heappop(frontier)


        # Skip outdated queue entries
        if current_distance > distances[current_node]:
            continue


        nodes_expanded += 1


        # Check if destination is reached
        if current_node == goal:


            run_time = time.perf_counter() - start_time
            path = generate_path(came_from, current_node)


            return (
                path,
                run_time,
                nodes_expanded,
                nodes_generated,
                max_frontier_size,
                distances[goal]
            )


        # Expand neighboring nodes
        for neighbor in graph.neighbors(current_node):


            # Use shortest available edge
            edge_length = min(
                data["length"]
                for data in graph[current_node][neighbor].values()
            )


            # Calculate total distance
            tentative_distance = current_distance + edge_length


            # Check whether the new path is better
            if tentative_distance < distances.get(
                neighbor, float("inf")
            ):


                distances[neighbor] = tentative_distance
                came_from[neighbor] = current_node


                heapq.heappush(
                    frontier,
                    (tentative_distance, neighbor)
                )


                nodes_generated += 1


                max_frontier_size = max(
                    max_frontier_size,
                    len(frontier)
                )


    # No route found
    run_time = time.perf_counter() - start_time


    return (
        None,
        run_time,
        nodes_expanded,
        nodes_generated,
        max_frontier_size,
        None
    )




if __name__ == "__main__":
    # Download the campus graph


    print("Loading Texas Tech campus map...")


    place_name = "Texas Tech University, Lubbock, Texas, USA"
    graph_file = "texas_tech.graphml"


    ox.settings.use_cache = True
    ox.settings.log_console = True
    ox.settings.requests_timeout = 120


    # Use the default Overpass server
    ox.settings.overpass_url = "https://overpass-api.de/api"


    if os.path.exists(graph_file):
        print("Loading previously saved campus graph...")
        G = ox.io.load_graphml(graph_file)


    else:
        print("Downloading Texas Tech campus map from OpenStreetMap...")


        try:
            G = ox.graph_from_place(
                place_name,
                network_type="walk"
            )


        except Exception as e:
            print("Campus boundary download failed:", e)
            print("Trying a smaller area around campus...")


            try:
                G = ox.graph_from_point(
                    (33.5843, -101.8783),
                    dist=750,
                    network_type="walk"
                )


            except Exception as fallback_error:
                raise RuntimeError(
                    "Could not download the walking network. "
                    "Check the internet connection or try "
                    "loading a saved GraphML file."
                ) from fallback_error


        ox.io.save_graphml(G, graph_file)
        print("Campus graph saved!")


    print("Total Nodes:", G.number_of_nodes())
    print("Total Edges:", G.number_of_edges())


    # Defining start and goal Nodes


    # Select the largest strongly connected component
    # so the test locations can reach one another.
    largest_component = max(
        nx.strongly_connected_components(G),
        key=len
    )


    G = G.subgraph(largest_component).copy()


    nodes = list(G.nodes)


    start_node = nodes[0]
    goal_node = nodes[-1]


    print("\nStart Node:", start_node)
    print("Goal Node:", goal_node)


    # Run Dijkstra's algorithm


    print("\nRunning Dijkstra's Algorithm...")


    path, run_time, nodes_expanded, nodes_generated, max_frontier, distance = dijkstra(
        G,
        start_node,
        goal_node
    )


    # Output performance metrics


    print("\n--- DIJKSTRA METRICS ---")


    print(f"Run Time:          {run_time:.6f} seconds")
    print(f"Nodes Expanded:    {nodes_expanded}")
    print(f"Nodes Generated:   {nodes_generated}")
    print(f"Max Frontier Size: {max_frontier}")


    if path is not None:
        print(f"Path Length:       {len(path)} nodes")
        print(f"Walking Distance:  {distance:.2f} meters")


        # Verify Against NetworkX


        expected_distance = nx.shortest_path_length(
            G,
            source=start_node,
            target=goal_node,
            weight="length"
        )


        print("\n--- VERIFICATION ---")
        print(f"Dijkstra Distance: {distance:.2f} meters")
        print(f"NetworkX Distance: {expected_distance:.2f} meters")


        assert abs(distance - expected_distance) < 1e-6


        print("Dijkstra verification passed!")


        # Visualize the shortest route


        fig, ax = ox.plot_graph_route(
            G,
            path,
            route_color="red",
            route_linewidth=4,
            node_size=0,
            show=False,
            close=False
        )


        ax.set_title(
            "Dijkstra's Shortest Path - Texas Tech University",
            fontsize=14
        )


        plt.show()


    else:
        print("No valid path found between the selected nodes.")


