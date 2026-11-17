# Ebun's Implementation — Setup Guide

## Overview

This implementation contains Ebun's contribution to the CS 3368 Artificial Intelligence pathfinding project.

The implementation is maintained separately from Emmanuel's code to allow independent execution, testing, and comparison.

## 1. Prerequisites

Before running the program, ensure you have:

- Python 3.x installed
- pip (Python package manager)
- Visual Studio Code or another Python-compatible editor

An internet connection may be required if the implementation downloads road network data.

## 2. Install Dependencies

Open a terminal in VS Code and navigate to the `ebun` directory.

Install the required libraries by running:

```bash
python3 -m pip install -r requirements.txt
```

The provisional requirements are:

```text
osmnx
networkx
matplotlib
```

These dependencies should be verified against the imports in `ebun.py` before the final submission.

## 3. Run the Program

From the `ebun` directory, execute:

```bash
python3 ebun.py
```

## 4. Expected Output

The program executes Ebun's pathfinding implementation.

The specific terminal output, performance metrics, and any graphical visualizations depend on the functionality implemented in `ebun.py` and should be verified by running the program.

## 5. Troubleshooting

**ModuleNotFoundError:** Install the required libraries using the command in Section 2.

**Python command not found:** Verify that Python 3.x is installed correctly.

**Program does not execute:** Confirm that the terminal is inside the `ebun` directory and that `ebun.py` exists.

**Additional dependencies required:** Check the imported libraries in `ebun.py` and update `requirements.txt` as needed.

## Author

Implementation: Ebun OLowolayemo

Course: CS 3368 — Introduction to Artificial Intelligence
