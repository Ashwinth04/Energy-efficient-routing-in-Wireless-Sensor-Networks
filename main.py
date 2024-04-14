import matplotlib.pyplot as plt
import numpy as np

nodes = {
    1:{
        "Node ID": 1,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [2,3,4,5],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    2:{
        "Node ID": 2,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [6,7],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    3:{
        "Node ID": 3,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [8,9],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    4:{
        "Node ID": 4,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [9,10],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    5:{
        "Node ID": 5,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [11],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    6:{
        "Node ID": 6,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [12],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    7:{
        "Node ID": 7,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [12],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    8:{
        "Node ID": 8,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [13],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    9:{
        "Node ID": 9,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [13],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    10:{
        "Node ID": 10,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [14],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    11:{
        "Node ID": 11,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [14],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    12:{
        "Node ID": 12,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [15],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    13:{
        "Node ID": 13,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [15],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    14:{
        "Node ID": 14,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [15],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    15:{
        "Node ID": 15,
        "Position": (np.random.uniform(0, 200), np.random.uniform(0, 200)),
        "Neighbors": [],
        "Initial Energy": np.random.randint(100, 201),
        "Residual Energy": np.random.randint(100, 201),
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    }
}

def calculate_heuristic(node,sink):
    node_pos = nodes[node]["Position"]
    sink_pos = nodes[sink]["Position"]
    dns = ((node_pos[0] - sink_pos[0])**2 + (node_pos[1] - sink_pos[1])**2)**0.5
    avg_dnj = 0
    for j in nodes[node]["Neighbors"]:
        j_pos = nodes[j]["Position"] 
        dnj = ((node_pos[0] - j_pos[0])**2 + (node_pos[1] - j_pos[1])**2)**0.5
        avg_dnj  += dnj
    avg_dnj /= len(nodes[node]["Neighbors"])

    return avg_dnj/dns

def g_of_n(node):
    alpha = 0.6
    beta = 0.2
    gamma = 0.2

    return alpha*(nodes[node]["Residual Energy"]/nodes[node]["Initial Energy"]) + beta*nodes[node]["PTR"] + gamma*(nodes[node]["Free Buffer"]/nodes[node]["Buffer Capacity"])

x_coords = [info["Position"][0] for node,info in nodes.items()]
y_coords = [info["Position"][1] for node,info in nodes.items()]

def astar(source, sink):
    closed = []
    closed.append(source)
    while(closed[-1] != sink):
        node = closed[-1]
        successor = [0,0]
        print(node)
        neighbors = nodes[node]['Neighbors']
        for neighbor in neighbors:
            if(neighbor == sink):
                successor[1] = neighbor
                break
            if(neighbor not in closed):
                fn = g_of_n(source) + calculate_heuristic(neighbor,sink)
                if(fn > successor[0]):
                    successor[0] = fn
                    successor[1] = neighbor
        closed.append(successor[1])

    return closed

    

print(astar(1,15))
# plt.scatter(x_coords,y_coords)
# plt.show()

# print(calculate_heuristic(3,15))
# print(g_of_n(3))