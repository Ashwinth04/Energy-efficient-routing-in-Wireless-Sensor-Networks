import matplotlib.pyplot as plt
import numpy as np

nodes = {
    1:{
        "Node ID": 1,
        "Position": (100, 200),
        "Neighbors": [2,3,4,5],
        "Initial Energy": 100,
        "Residual Energy": 95,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    2:{
        "Node ID": 2,
        "Position": (50,150),
        "Neighbors": [6,7],
        "Initial Energy": 98,
        "Residual Energy": 90,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    3:{
        "Node ID": 3,
        "Position": (100,150),
        "Neighbors": [8,9],
        "Initial Energy": 95,
        "Residual Energy": 95,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    4:{
        "Node ID": 4,
        "Position": (150,150),
        "Neighbors": [9,10],
        "Initial Energy": 90,
        "Residual Energy": 75,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    5:{
        "Node ID": 5,
        "Position": (200,150),
        "Neighbors": [11],
        "Initial Energy": 85,
        "Residual Energy": 83,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    6:{
        "Node ID": 6,
        "Position": (33,100),
        "Neighbors": [12],
        "Initial Energy": 83,
        "Residual Energy": 50,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    7:{
        "Node ID": 7,
        "Position": (66,100),
        "Neighbors": [12],
        "Initial Energy": 87,
        "Residual Energy": 77,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    8:{
        "Node ID": 8,
        "Position": (99,100),
        "Neighbors": [13],
        "Initial Energy": 73,
        "Residual Energy": 70,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    9:{
        "Node ID": 9,
        "Position": (133,100),
        "Neighbors": [13],
        "Initial Energy": 65,
        "Residual Energy": 62,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    10:{
        "Node ID": 10,
        "Position": (166,100),
        "Neighbors": [14],
        "Initial Energy": 60,
        "Residual Energy": 30,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    11:{
        "Node ID": 11,
        "Position": (199,100),
        "Neighbors": [14],
        "Initial Energy": 55,
        "Residual Energy": 55,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    12:{
        "Node ID": 12,
        "Position": (75,50),
        "Neighbors": [15],
        "Initial Energy": 30,
        "Residual Energy": 25,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    13:{
        "Node ID": 13,
        "Position": (140,50),
        "Neighbors": [15],
        "Initial Energy": 45,
        "Residual Energy": 45,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    14:{
        "Node ID": 14,
        "Position": (185,50),
        "Neighbors": [15],
        "Initial Energy": 38,
        "Residual Energy": 33,
        "PRR": np.random.uniform(0.8, 0.91),
        "Buffer Capacity": np.random.randint(8, 11),
        "Free Buffer": np.random.randint(8, 11),
        "Data Packet": {},
        "PTR": 0.88,
    },
    15:{
        "Node ID": 15,
        "Position": (100,10),
        "Neighbors": [],
        "Initial Energy": 35,
        "Residual Energy": 25,
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

def calculate_total_energy():
    energy = 0
    for _, node_dict in nodes.items():
        energy += node_dict["Residual Energy"]

    return energy

def astar(source, sink):
    closed = []
    closed.append(source)
    while(closed[-1] != sink):
        node = closed[-1]
        successor = [0,0]
        # print(node)
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

x_coords = []
y_coords = []
for node,node_dict in nodes.items():
    x_coords.append(node_dict["Position"][0])
    y_coords.append(node_dict["Position"][1])

plt.scatter(x_coords,y_coords)

for node,node_dict in nodes.items():
    first = node_dict["Position"]
    for n in node_dict["Neighbors"]:
        second = nodes[n]["Position"]
        plt.plot([first[0],second[0]],[first[1],second[1]])
plt.show()
print("Initial energy: ",calculate_total_energy())
print(astar(1,15))
print("Final energy: ",calculate_total_energy())
# plt.scatter(x_coords,y_coords)
# plt.show()

# print(calculate_heuristic(3,15))
# print(g_of_n(3))