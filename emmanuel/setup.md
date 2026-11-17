# Emmanuel's Implementation — Setup Guide

## Overview

This implementation uses Python to execute and compare pathfinding algorithms on real-world road networks. It uses OSMnx for geographic road network data, NetworkX for graph operations, and Matplotlib for route visualization.

The program reports performance metrics, including:

- Algorithm runtime
- Number of nodes expanded
- Maximum frontier size
- Graphical visualization of the calculated routes

## 1. Prerequisites

Before running the program, ensure you have:

- Python 3.x installed
- pip (Python package manager)
- An internet connection to download map data
- Visual Studio Code or another Python-compatible editor

## 2. Install Dependencies

Open a terminal in VS Code and navigate to the `emmanuel` directory.

Install the required Python libraries by running:

```bash
python3 -m pip install -r requirements.txt
```

The requirements file contains:

```text
osmnx
networkx
matplotlib
```

## 3. Run the Program

From the `emmanuel` directory, execute:

```bash
python3 emmanuel.py
```

The program will load the required road network, execute the implemented pathfinding algorithms, and display the results.

## 4. Expected Output

After execution:

1. The terminal displays a comparison of algorithm performance metrics, including runtime, nodes expanded, and maximum frontier size.
2. A Matplotlib window opens to display the calculated route or routes on the road network.

## 5. Troubleshooting

**ModuleNotFoundError:** Ensure all dependencies have been installed using the command in Section 2.

**Map data fails to load:** Check your internet connection because OSMnx may need to retrieve map data from OpenStreetMap.

**Matplotlib window does not appear:** Ensure the program is running in a Python environment with graphical display support.

**Python command not found:** Verify that Python 3.x is installed and accessible from your terminal.

## Author

Implementation: Emmanuel Ojo

Course: CS 3368 — Introduction to Artificial Intelligence
