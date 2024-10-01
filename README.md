# labyrinth
Project Overview
This project is a Labyrinth Maze Solver that utilizes Q-learning, a reinforcement learning algorithm, to find the optimal path from a start point to a goal in a dynamically generated maze. The maze is represented as a grid where the player has to navigate through non-blocking cells to reach the goal.

Users can customize several parameters, such as the maze size, learning rate (alpha), and discount factor (gamma) using the Streamlit interface.

Features
Q-learning algorithm to train the model and find the optimal path.
Randomly generated maze with varying maze size.
Streamlit sidebar for user-controlled parameters (e.g., maze size, learning rate, discount factor).
Visualization of the maze and the optimal path using Matplotlib.
A clear indication of the start and goal points in the maze.
Tools & Technologies Used
Python: The core programming language used for developing the algorithm.
Numpy: Used for creating and manipulating the maze as a grid.
Matplotlib: For visualizing the maze and the optimal path.
Streamlit: For creating a user-friendly web-based interface where users can interact with the algorithm by adjusting parameters and viewing the maze.

Parameters Explained
Maze Size: Controls the size of the maze grid. Larger sizes will make the task more challenging.
Learning Rate (alpha): The rate at which the Q-learning algorithm updates its values.
Discount Factor (gamma): The importance of future rewards in the Q-learning algorithm.
