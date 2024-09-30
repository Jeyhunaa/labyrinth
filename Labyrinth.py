import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle

# Streamlit UI
st.title("Labyrinth Maze Solver")

# Parameters for user input
gamma = st.sidebar.slider("Discount factor (gamma)", 0.0, 1.0, 0.8)
alpha = st.sidebar.slider("Learning rate (alpha)", 0.0, 1.0, 0.9)
maze_size = st.sidebar.slider("Maze Size", 5, 100, 10)

# Create maze
maze = np.random.choice([0, -1], (maze_size, maze_size), p=[0.8, 0.2])
maze[0, 0] = 0  # Start position remains a normal cell
maze[-1, -1] = 100  # Goal position

# Define states and actions
states = [(i, j) for i in range(maze.shape[0]) for j in range(maze.shape[1])]
actions = ['up', 'down', 'left', 'right']
Q = np.zeros((len(states), len(actions)))

# Mapping functions
def state_to_index(state):
    return states.index(state)

def is_valid_move(state, action):
    i, j = state
    if action == 'up' and i > 0 and maze[i - 1, j] != -1:
        return True
    if action == 'down' and i < maze.shape[0] - 1 and maze[i + 1, j] != -1:
        return True
    if action == 'left' and j > 0 and maze[i, j - 1] != -1:
        return True
    if action == 'right' and j < maze.shape[1] - 1 and maze[i, j + 1] != -1:
        return True
    return False

def next_state(state, action):
    i, j = state
    if action == 'up':
        return (i - 1, j)
    elif action == 'down':
        return (i + 1, j)
    elif action == 'left':
        return (i, j - 1)
    elif action == 'right':
        return (i, j + 1)

def reward(state):
    i, j = state
    return maze[i, j]

# Training
for episode in range(1000):
    current_state = (0, 0)  # Start position
    while current_state != (maze_size - 1, maze_size - 1):  # Goal position
        state_index = state_to_index(current_state)
        possible_actions = [a for a in actions if is_valid_move(current_state, a)]

        if not possible_actions:
            break  # If no possible actions, stop the episode

        action = np.random.choice(possible_actions)
        action_index = actions.index(action)

        new_state = next_state(current_state, action)
        new_state_index = state_to_index(new_state)

        Q[state_index, action_index] += alpha * (reward(new_state) + gamma * np.max(Q[new_state_index]) - Q[state_index, action_index])

        current_state = new_state

# Finding the optimal path and getting the coordinates for visualization
def find_path_and_coords(start, goal):
    path = []
    path_coords = [start]  # Start with the initial position
    current_state = start
    while current_state != goal:
        state_index = state_to_index(current_state)
        action_index = np.argmax(Q[state_index])
        best_action = actions[action_index]
        path.append(best_action)
        
        current_state = next_state(current_state, best_action)
        path_coords.append(current_state)  # Add each new position to the coordinates

    return path, path_coords

optimal_path, path_coords = find_path_and_coords((0, 0), (maze_size - 1, maze_size - 1))

# Create a colormap for the maze visualization
cmap = mcolors.ListedColormap(['black', 'white', 'lightgray', 'green'])
bounds = [-1, 0, 1, 100]  # Bounds correspond to the values in the maze
norm = mcolors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(maze, cmap=cmap, norm=norm)

start_x, start_y = 0, 0
ax.add_patch(Rectangle((start_y - 0.5, start_x - 0.5), 1, 1, edgecolor='blue', facecolor='blue'))


# Add grid lines
ax.grid(which='both', color='black', linestyle='-', linewidth=1)
ax.set_xticks(np.arange(-0.5, maze.shape[1], 1))
ax.set_yticks(np.arange(-0.5, maze.shape[0], 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Convert the path coordinates to plot a thick line
path_x = [coord[1] + 0.045 for coord in path_coords]  # X-coordinates
path_y = [coord[0] + 0.04 for coord in path_coords]  # Y-coordinates

# Add labels for "Start" and "Goal" 
ax.text(start_y,start_x - 1, 'Start', ha='center', va='center', color='black', fontsize=12, fontweight='bold')
goal_x, goal_y = maze_size - 1, maze_size - 1
ax.text(goal_y,goal_x + 1, 'Goal', ha='center', va='center', color='black', fontsize=12, fontweight='bold')



# Plot the path as a thick pink line
ax.plot(path_x, path_y, color='red', linewidth=5, solid_capstyle='round')  # Thicker line with rounded caps


# Use Streamlit to display the plot
st.pyplot(fig)

# Example use case
#st.write("**Optimal path:**", optimal_path)

formatted_path = " → ".join(optimal_path)
st.markdown(''':red[Optimal Path:]''')
st.write(formatted_path)


