import matplotlib.pyplot as plt
import numpy as np
import copy
from numpy import random
from nodes import nodes

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

def calculate_total_energy(nodes_dict):
    energy = 0
    for _, node_dict in nodes_dict.items():
        energy += node_dict["Residual Energy"]

    return energy

def calculate_distance(first,second):
    return((first[0] - second[0])**2 + (first[1] - second[1])**2)**0.5

def calculate_energy_for_path(path):
    temp_nodes = copy.deepcopy(nodes)
    for i in range(0,len(path)-1):
        t = temp_nodes[path[i]]
        r = temp_nodes[path[i+1]]
        transmission_energy, reception_energy = calculate_trans_rec_energy(path[i],path[i+1],4,temp_nodes)
        t["Residual Energy"] -= transmission_energy
        r["Residual Energy"] -= reception_energy
    return calculate_total_energy(temp_nodes)

def calculate_trans_rec_energy(node1,node2,k,nodes_dict):
    transmitter = nodes_dict[node1]
    # print(node1,node2)
    receiver = nodes_dict[node2]
    E_elec = 5
    epsilon = 10
    d = calculate_distance(transmitter["Position"],receiver["Position"])
    transmission_energy = k*(E_elec + epsilon*d*d/10000000)
    reception_energy = k*E_elec

    return transmission_energy, reception_energy


def astar(source, sink):
    closed = []
    closed.append(source)
    cost_list = [0]
    while(closed[-1] != sink):
        node = closed[-1]
        successor = [0,0]
        neighbors = nodes[node]['Neighbors']
        # print(neighbors)
        for neighbor in neighbors:
            if(neighbor == sink):
                successor[1] = neighbor
                break
            if(neighbor not in closed):
                fn = sum(cost_list) + g_of_n(node) + calculate_heuristic(neighbor,sink)
                cost_list.append(g_of_n(node))
                # if(fn > successor[0]):
                successor[0] = fn
                successor[1] = neighbor
        closed.append(successor[1])
        # print(closed)
        transmission_energy, reception_energy = calculate_trans_rec_energy(node,successor[1],4,nodes)
        nodes[node]["Residual Energy"] -= transmission_energy
        nodes[node]["Residual Energy"] -= reception_energy
    return closed

x_coords = []
y_coords = []



# for node,node_dict in nodes.items():
#     x_coords.append(node_dict["Position"][0])
#     y_coords.append(node_dict["Position"][1])

# plt.scatter(x_coords,y_coords)

# for node,node_dict in nodes.items():
#     first = node_dict["Position"]
#     for n in node_dict["Neighbors"]:
#         second = nodes[n]["Position"]
#         plt.plot([first[0],second[0]],[first[1],second[1]])

# plt.show()

# path = [1,3,8,13,15]
# print(f"Path = {path}, Residual Energy of network if this path is taken: {calculate_energy_for_path(path)}")

# path = [1,2,7,12,15]
# print(f"Path = {path}, Residual Energy of network if this path is taken: {calculate_energy_for_path(path)}")

# print("Initial energy: ",calculate_total_energy(nodes))
# print(astar(1,15))
# print("Final energy: ",calculate_total_energy(nodes))


def generate_random_path(source,sink):
    path = []
    path.append(source)
    node = path[-1]
    while(node != sink):
        neighbours = nodes[node]["Neighbors"]
        successor = random.choice(neighbours)
        path.append(successor)
        node = path[-1]

    return path

def find_different_path(path):
    index = random.randint(1,len(path)-1)
    prev_index = index - 1
    neighbors = nodes[path[prev_index]]["Neighbors"]
    new_bit = random.choice(neighbors)
    path[index] = new_bit
    for i in range(index+1,len(path)):
        if(path[i] not in nodes[path[i-1]]["Neighbors"]):
            path[i] = random.choice(nodes[path[i-1]]["Neighbors"])

    return path

# print(find_different_path([1,3,8,13,15]))


def simulated_annealing(initial_path,temperature, cooling_rate):
    path = initial_path
    while(temperature > 0.01):
        new_path = find_different_path(path)
        new_cost = calculate_energy_for_path(new_path)
        old_cost = calculate_energy_for_path(path)
        if(new_cost > old_cost):
            path = new_path
            continue
        else:
            dele = old_cost - new_cost
            p = np.exp(-1*dele/temperature)
            r = random.randint(0,1)
            if(p > r):
                path = new_path
            temperature= cooling_rate*temperature

    return path

initial_path = [1, 5, 11, 14, 15]
print(f"Initial path: {initial_path}, Energy if this path was taken = {calculate_energy_for_path(initial_path)}")
path = simulated_annealing(initial_path,1000,0.1)
print(f"Path: {path}, Residual Energy = {calculate_energy_for_path(path)}")