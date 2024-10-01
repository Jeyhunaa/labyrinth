#  Labyrinth solver 
## Project Overview
This project is a **Labyrinth Maze Solver** that utilizes **Q-learning**, a reinforcement learning algorithm, to find the optimal path from a start point to a goal in a dynamically generated maze. The maze is represented as a grid where the player has to navigate through non-blocking cells to reach the goal.

Users can customize several parameters, such as the maze size, learning rate (alpha), and discount factor (gamma) using the Streamlit interface.

**Try the live demo:** https://labyrinth.streamlit.app/

## Tools & Technologies Used
- **Numpy**: Used for creating and manipulating the maze as a grid.
- **Matplotlib**: For visualizing the maze and the optimal path.
- **Streamlit**: For creating a user-friendly web-based interface where users can interact with the algorithm by adjusting parameters and viewing the maze.

## Parameters
- **Maze Size**: Adjusts the grid size.
- **Learning Rate (alpha)**: Controls Q-learning updates.
- **Discount Factor (gamma)**: Balances future rewards.
