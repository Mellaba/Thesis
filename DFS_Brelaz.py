import networkx as nx
import matplotlib.pyplot as plt
import random
import time  
import copy
import os
import json

def options(F, distinct_colors, colors):

    for i in range(len(F)):
        # Compute the maximum saturation and the set of nodes that
        # achieve that saturation.
        saturation = {v: len(c) for v, c in distinct_colors.items() # om te kijken hoe hoog de saturation is
                       if v not in colors} # want als hij in colors zit is die ingekleurd
        # Yield the node with the highest saturation, and break ties by
        # degree.
        
        # Dit deel stelt vast welke nodes de hoogste saturation hebben en stopt ze in een lijst
        max_sat = 0
        for key in saturation:
            if saturation[key] > max_sat:
                max_sat = saturation[key]
        max_sat_items = []
        for key in saturation:
            if saturation[key] == max_sat:
                max_sat_items.append(key)
        max_deg = 0

        # Dit deel stelt vast welke nodes van de hoogste saturation de meeste connecties hebben en stopt
        # deze dan ook weer in een lijst
        if len(max_sat_items) > 1:
            max_sat_max_deg = []
            for item in max_sat_items:
                if max_deg < len(F[item]):
                    max_deg = len(F[item])

            for item in max_sat_items:
                if len(F[item]) == max_deg:
                    max_sat_max_deg.append(item)
            return max_sat_max_deg
        
        return max_sat_items


def DFS_color_Brelaz(G, k):
    start = time.time()
    colors = {}

    distinct_colors = {v: set() for v in G}

    stack = []
    d_stack = []
    visited = []
    steps = 0
    brelaz_steps = 0
    
    nodes = options(G, distinct_colors, colors)
    for node in nodes:
        brelaz_steps += 1
        for color in range(k):
            colors_2 = copy.deepcopy(colors)
            if color not in distinct_colors[node]:
                distinct_colors_2 = copy.deepcopy(distinct_colors)
                colors_2[node] = color
                for neighbour in G[node]:
                    distinct_colors_2[neighbour].add(color)
                stack.append(colors_2)
                d_stack.append(distinct_colors_2)
                    
    while stack:
        colors_1 = stack.pop()
        steps += 1

        if colors_1 in visited:
            continue
        if brelaz_steps > 144000 and len(colors_1) != len(G):
            end = time.time()
            runtime = (end - start)
            return {}, brelaz_steps, steps, runtime 
        visited.append(colors_1)
        if len(colors_1) == len(G):
            end = time.time()
            runtime = (end - start)
            return colors_1, brelaz_steps, steps, runtime
        distinct_colors = d_stack.pop()
        nodes = options(G, distinct_colors, colors_1)
        for node in nodes:
            brelaz_steps += 1
            for color in range(k): 
                colors_2 = copy.deepcopy(colors_1)
                if color not in distinct_colors[node]:
                    distinct_colors_2 = copy.deepcopy(distinct_colors)
                    colors_2[node] = color
                    for neighbour in G[node]:
                        distinct_colors_2[neighbour].add(color)

                    stack.append(colors_2)
                    d_stack.append(distinct_colors_2)
    
    
    if len(colors_1) == len(G):
        end = time.time()
        runtime = (end - start)
        return colors_1, brelaz_steps, steps, runtime
    
    if stack == [] and len(colors_1) != len(G):
        end = time.time()
        runtime = (end - start)
        return {}, brelaz_steps, steps, runtime

def DFS_color_Random(G, k):
    start = time.time()
    colors = {}

    distinct_colors = {v: set() for v in G}

    stack = []
    d_stack = []
    visited = []
    steps = 0
    still_to_be_colored = []

    for node1 in G:
        still_to_be_colored.append(node1)

    i = random.randrange(len(still_to_be_colored))
    node = F[i]
    
    for color in range(k):
        colors_2 = copy.deepcopy(colors)
        if color not in distinct_colors[node]:
            distinct_colors_2 = copy.deepcopy(distinct_colors)
            colors_2[node] = color
            for neighbour in G[node]:
                distinct_colors_2[neighbour].add(color)
            stack.append(colors_2)
            d_stack.append(distinct_colors_2)
                    
    while stack:
        colors_1 = stack.pop()
        steps += 1

        if colors_1 in visited:
            continue
        if steps > 100000 and len(colors_1) != len(G):
            end = time.time()
            runtime = (end - start)
            return {}, steps, runtime 
        visited.append(colors_1)
        if len(colors_1) == len(G):
            end = time.time()
            runtime = (end - start)
            return colors_1, steps, runtime
        distinct_colors = d_stack.pop()
        nodes = options(G, distinct_colors, colors_1)


        for color in range(k): 
            colors_2 = copy.deepcopy(colors_1)
            if color not in distinct_colors[node]:
                distinct_colors_2 = copy.deepcopy(distinct_colors)
                colors_2[node] = color
                for neighbour in G[node]:
                    distinct_colors_2[neighbour].add(color)

                stack.append(colors_2)
                d_stack.append(distinct_colors_2)
    
    
    if len(colors_1) == len(G):
        end = time.time()
        runtime = (end - start)
        return colors_1, steps, runtime
    
    if stack == [] and len(colors_1) != len(G):
        end = time.time()
        runtime = (end - start)
        return {}, steps, runtime

def split_filename(filename):
    parts = filename.split('_')
    degree = parts[0]
    nodes = parts[2] 
    p = parts[3][1]
    
    return degree, nodes, p

output = []
for filename in os.listdir("4K_graphs_all_cliques"):
    if filename.startswith('.'):
        continue
    flag = 0
    degree, nodes, p = split_filename(filename)

    name = "/Users/melanie/Documents/Thesis/Programming/4K_graphs_all_cliques/" + str(filename)
    G=nx.read_edgelist(name)
    colorlist, brelaz_steps, steps, runtime = DFS_color_Brelaz(G, 4)
    
    data = {
        "degree": degree,
        "nodes": nodes,
        "p": p,
        "colorlist": colorlist,
        "brelazsteps" : brelaz_steps,
        "steps": steps,
        "runtime":runtime
    }

    
    with open('Brelazsteps_all_cliques_coloured_4K_graphs_DFS_Brelaz.json', 'a') as outfile:
        json.dump(data, outfile, indent=2)
        outfile.write(',')




