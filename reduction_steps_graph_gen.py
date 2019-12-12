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
    for n in G:
        n_list = [] 
        for i in G[n]:
            n_list.append(i)

        for m in G:
            m_list = []
            if m != n:
                for j in G[m]:
                    m_list.append(j)

                if set(m_list).issubset(set(n_list)) and len(m_list) > k-1:
                    if m not in to_be_removed:
                        to_be_removed.append(m)

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
        G = nx.contracted_nodes(G, node_a, node_b)

        for i in range(len(mergable_nodes)):
            if mergable_nodes[i][0] == node_b:
                mergable_nodes[i][0] = node_a
            elif mergable_nodes[i][1] == node_b:
                mergable_nodes[i][1] = node_a
                
    return G

def gen_random_graph(N, K):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    Somenodes = random.randrange(N)
    flag = 0
    
    for i in G:
        flag = 0
        for j in nx.cliques_containing_node(G, nodes=i): 
            if len(j) > K-1:  # JELLE: KLOPT DIT WEL? 
                flag = 1 
                break
        if flag == 1:
            continue
        rnum = random.randrange(10*K) # VRAAG AAN JELLE: IK HEB DEZE KEUZE GEMAAKT
        for count in range(rnum):
            flag = 0
            randomnode = random.randrange(N)
            if randomnode!= i:
                for a in nx.cliques_containing_node(G, nodes=randomnode):
                    if len(a) > K-1:
                        flag = 1
                        break
                if flag == 1:
                    continue
                
                ran = random.random()
                if ran > 0.5:
                    G.add_edge(i,randomnode)
    return G














