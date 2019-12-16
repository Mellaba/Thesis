import networkx as nx
import matplotlib.pyplot as plt
import random 
import itertools
import collections

def undercon(G, k):
    to_be_removed = []
    for n in G:
        if len(G[n]) < k:
            to_be_removed.append(n)

    for node in to_be_removed:       
        G.remove_node(node) # G.remove_node(n)
    
    return G

def subsumed(G, k):
    to_be_removed = []
    all_nodes = set(G)
    for n in G:
        n_edges = set(G[n])
        for m in all_nodes:
            if n == m:
                continue
            m_edges = set(G[m])

            if n_edges.issubset(m_edges):
                to_be_removed.append(n)
                all_nodes.remove(n)
                break


    #     for m in G:
    #         m_list = []
    #         if m != n:
    #             for j in G[m]:
    #                 m_list.append(j)

    #             if set(m_list).issubset(set(n_list)): #and len(m_list) > k-1:
    #                 if m not in to_be_removed:
    #                     to_be_removed.append(m)

    for node in to_be_removed:
        G.remove_node(node)
    
    return G


def cliques_of_size(G, n):

    cliques = []
    for clique in nx.find_cliques(G):
        if len(clique) == n:
            cliques.append(set(clique))
            # Hier wil ik dus eigenlijk checken of K-1 elementen van lijst 1 overeenkomen met lijst 2. Als dit zo is dan
            # pak de unique elementen uit beide lijsten en merge deze nodes met elkaar.
    return cliques

def get_mergable_nodes(cliques, k):

    mergable_nodes = set()

    for clique_a, clique_b in itertools.combinations(cliques, 2):
        if len(clique_a & clique_b) == k - 1:
            mergable_nodes.add(tuple(clique_a ^ clique_b))
    
    return mergable_nodes

def symmetry(G, k):
    cliques = cliques_of_size(G, k)
    mergable = get_mergable_nodes(cliques, k)

    mergable_nodes = list(map(list, mergable))

    while mergable_nodes:
        node_a, node_b = mergable_nodes.pop()

        if node_a == node_b:
            continue

        G = nx.contracted_nodes(G, node_a, node_b)

        for i in range(len(mergable_nodes)):
            if mergable_nodes[i][0] == node_b:
                mergable_nodes[i][0] = node_a
            if mergable_nodes[i][1] == node_b:
                mergable_nodes[i][1] = node_a
                
    return G

def create_edge(G, K, node_1, node_2):
    if node_1 != node_2:
        G.add_edge(node_1, node_2)
    
    for clique in nx.cliques_containing_node(G, nodes=node_1):
        if node_2 in clique and len(clique) > K:
            G.remove_edge(node_1, node_2)
            break
        
    return G

def average_degree(G):
    return sum(dict(G.degree()).values()) / len(G)

def reduce_graph(G, K):
    n_nodes = len(G)
    while True:
        G = subsumed(G, K)
        G = symmetry(G, K)
        G = undercon(G, K)
        if len(G) == n_nodes:
            break
        n_nodes = len(G)
    return G

def gen_random_graph(N, K, P):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    for node_1 in G:
        for node_2 in G:
            p = P / N
            if random.random() < p:
                G = create_edge(G, K, node_1, node_2)

    G = reduce_graph(G, K)
                
    return G
















