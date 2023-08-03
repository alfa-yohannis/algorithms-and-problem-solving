class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    def __init__(self, value):
        self.value = value
        self.from_node = None
        self.to_node = None

    def set_from_node(self, node):
        self.from_node = node
        node.edges.append(self)

    def set_to_node(self, node):
        self.to_node = node
        node.edges.append(self)

class Graph:
     
    def __init__(self):
        pass

    def cetak_graph_dalam(self, start_node):
        edge_memory = []
        self.rekursif_cetak_graph_dalam(start_node, edge_memory)
        edge_memory.clear()
        print()

    def rekursif_cetak_graph_dalam(self,node, edge_memory):
        print(node.value, end=" ")
        for edge in node.edges:
            # print(edge.value, end=" ")
            if edge in edge_memory:
                continue
            edge_memory.append(edge)
            prev_node = node
            if node == edge.from_node:
                node = edge.to_node
            elif node == edge.to_node:
                node = edge.from_node
            self.rekursif_cetak_graph_dalam(node, edge_memory)
            node = prev_node

nodeA, nodeB, nodeC = Node("A"), Node("B"), Node("C")
nodeD, nodeE, nodeF = Node("D"), Node("E"), Node("F")
edge1, edge2, edge3, edge4 = Edge("1"), Edge("2"), Edge("3"), Edge("4")
edge5, edge6, edge7 = Edge("5"), Edge("6"), Edge("7")
edge1.set_from_node(nodeA), edge1.set_to_node(nodeB)
edge2.set_from_node(nodeA), edge2.set_to_node(nodeC)
edge3.set_from_node(nodeB), edge3.set_to_node(nodeE)
edge4.set_from_node(nodeB), edge4.set_to_node(nodeF)
edge5.set_from_node(nodeC), edge5.set_to_node(nodeD)
edge6.set_from_node(nodeD), edge6.set_to_node(nodeF)
edge7.set_from_node(nodeD), edge7.set_to_node(nodeE)

graph = Graph()
graph.cetak_graph_dalam(nodeA)
graph.cetak_graph_dalam(nodeB)
graph.cetak_graph_dalam(nodeC)



    


    