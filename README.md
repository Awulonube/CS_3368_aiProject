TrekTech: Step-Goal Routes

CS 3368 — Introduction to Artificial Intelligence
Team: FollowThru
Texas Tech University

Project Overview

TrekTech is an AI pathfinding project designed to encourage physical activity among college students by exploring walking routes between campus locations.

The project compares two pathfinding algorithms using Texas Tech University's walking network obtained through OpenStreetMap.

Algorithms

Dijkstra's Algorithm — Emmanuel Ojo

Computes the shortest walking route between two nodes.

Uses a priority queue and graph-based search.

Validates the shortest-path distance against NetworkX.

Displays performance metrics and a route visualization.

Weighted A — Ebun Olowolayemo*

Uses a weighted straight-line distance heuristic to guide pathfinding.

Prioritizes faster exploration of promising routes.

Reports runtime, nodes expanded, and maximum frontier size.

Visualizes the calculated route.

Both implementations use Python, OSMnx, NetworkX, and Matplotlib.

Repository Structure

CS_3368_aiProject/
├── emmanuel/
│   ├── emmanuel.py
│   ├── requirements.txt
│   └── setup.md
├── ebun/
│   ├── ebun.py
│   ├── requirements.txt
│   └── setup.md
└── README.md

Setup and Execution

Clone the repository:

git clone https://github.com/Awulonube/CS_3368_aiProject.git
cd CS_3368_aiProject

Run Emmanuel's implementation:

cd emmanuel
python3 -m pip install -r requirements.txt
python3 emmanuel.py

Run Ebun's implementation:

From the repository root:

cd ebun
python3 -m pip install -r requirements.txt
python3 ebun.py

Refer to each implementation's setup.md for detailed instructions.

Future Development

The next phase will focus on implementing bidirectional Dijkstra, adding step-goal optimization to Weighted A*, and comparing both algorithms across 100+ campus routes.

Contributors

Emmanuel Ojo: Dijkstra implementation, performance evaluation, and repository integration.

Ebun Olowolayemo: Weighted A* implementation, heuristic search, documentation and performance evaluation.

