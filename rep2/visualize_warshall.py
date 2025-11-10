import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

# 1. initialize relation matrix
R = np.array([
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
], dtype=int)

n = len(R)
steps = []  # save each step for visualization

# 2. warshall algorithm
M = R.copy()
for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = M[i][j] | (M[i][k] & M[k][j])
    steps.append(M.copy())  # k단계 후 행렬 저장

# 3. visualize
fig, ax = plt.subplots(figsize=(6, 6))
pos = nx.circular_layout(range(1, n + 1))

def draw_graph(matrix, k):
    ax.clear()
    ax.set_title(f"Warshall Algorithm: step k={k+1}")
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                G.add_edge(i + 1, j + 1)
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightblue",
        arrowsize=15,
        edge_color="tab:blue"
    )
    ax.axis("off")

# animation function
prev = np.zeros_like(R)
def update(frame):
    ax.clear()
    current = steps[frame]
    new_edges = np.argwhere((current - prev) > 0)
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if current[i][j]:
                color = "red" if [i, j] in new_edges.tolist() else "tab:blue"
                G.add_edge(i + 1, j + 1, color=color)
    colors = [d["color"] for (_,_,d) in G.edges(data=True)]
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color=colors, arrowsize=15)
    ax.set_title(f"Step {frame+1}")
    ax.axis("off")
    prev[:] = current

ani = FuncAnimation(fig, update, frames=len(steps), interval=2000, repeat=False)
ani.save("warshall.gif", writer=PillowWriter(fps=1))
plt.show()
