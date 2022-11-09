import networkx as nx 
# import pylab as plt 
import matplotlib.pylab as plt
D = nx.DiGraph() 
n = int(input("\nEnter number of nodes: ")) 
for i in range(n): 
    print(f"\nEnter node {i}:") 
    D.add_weighted_edges_from([(input("Enter Parent: "), input("Enter Child: "), int(input("Enter Weight: ")))]) 
print("\nPageRank: ", nx.pagerank(D)) 
nx.draw(D, with_labels=True) 
plt.show() 
