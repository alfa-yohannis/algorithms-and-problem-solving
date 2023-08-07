class Node:
    def __init__(self, label):
        self.label = label
        self.value = None
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
        self.nodes = []
        self.edges = []

    def cetak_graph_dalam(self, start_node):
        node_memory = []
        self.rekursif_cetak_graph_dalam(start_node, node_memory)
        node_memory.clear()
        print()

    def rekursif_cetak_graph_dalam(self,node, node_memory):
        print(node.label, end=" ")
        node_memory.append(node)

        for edge in node.edges:
            other_node = None
            if edge.from_node == node:
                other_node = edge.to_node
            else:
                other_node = edge.from_node
            
            if other_node in node_memory:
                continue

            self.rekursif_cetak_graph_dalam(other_node, node_memory)


    def cetak_graph_lebar(self, start_node):
        node_memory = []
        print(start_node.label, end=" ")
        node_memory.append(start_node)
        self.rekursif_cetak_graph_lebar(start_node, node_memory)
        node_memory.clear()
        print()

    def rekursif_cetak_graph_lebar(self,node, node_memory):

        other_nodes = []
        for edge in node.edges:
            other_node = None
            if edge.from_node == node:
                other_node = edge.to_node
            else:
                other_node = edge.from_node
        
            if other_node in node_memory:
                continue
            
            print(other_node.label, end=" ")
            node_memory.append(other_node)
            other_nodes.append(other_node)

        for n in other_nodes:
            self.rekursif_cetak_graph_lebar(n, node_memory)


    def cari_path(self, start_node, end_node):
        path_memory = []
        stack = []
        possible_paths = []
        self.rekursif_cari_path_dalam(start_node, end_node, start_node, path_memory, stack, possible_paths)
        return possible_paths

    def rekursif_cari_path_dalam(self, start_node, end_node, current_node, path_memory, stack, possible_paths):
        # print(current_node.label, end=" ")

        if current_node.label in stack:
            return 

        if current_node == end_node:
            path = stack.copy()
            path.append(current_node.label)
            possible_paths.append(path)
            return

        path_memory.append(current_node)
        stack.append(current_node.label)
        # for e in stack:
        #     print(e, end=" ")
        # print()

        for edge in current_node.edges:
            next_node = None
            if edge.from_node == current_node:
                next_node = edge.to_node
            else:
                next_node = edge.from_node
            
            self.rekursif_cari_path_dalam(start_node, end_node, next_node, path_memory, stack, possible_paths)
        
        stack.pop(len(stack) - 1)
        # for e in stack:
        #     print(e, end=" ")
        # print()

    def hitung_biaya_path(self, path):
        
        path_cost = 0

        for index in range(0, len(path) - 1):
            node1_value = path[index]
            node2_value = path[index + 1]
            node1 = None
            for node in self.nodes:
                if node.label == node1_value:
                    node1 = node
                    break
            
            for edge in node1.edges:
                if edge.from_node.label == node2_value or \
                    edge.to_node.label == node2_value:
                    path_cost = path_cost + edge.value
        
        return path_cost

    def hitung_biaya_nodes(self, path):
        path_cost = 0
        
        for label in path:
            node_dicari = None
            for node in self.nodes:
                if node.label == label:
                    node_dicari = node
                    break
            
            path_cost = path_cost + node_dicari.value

        return path_cost
    

    '''
        Menghitung jumlah biaya untuk semua nodes dan 
        edges yang dikunjungi dalam satu path.
        Modifikasi method berikut untuk menjawab pertanyaan
        soal UAS.
    '''
    def hitung_biaya_nodes_edges(self, path):
        pass


graph = Graph()

nodeA, nodeB = Node("A"), Node("B")


nodeA.value, nodeB.value = 1, 2

graph.nodes.append(nodeA), graph.nodes.append(nodeB)

edge1 = Edge("1")

graph.edges.append(edge1)

edge1.set_from_node(nodeA), edge1.set_to_node(nodeB)

edge1.value


print("\nSemua path dari", nodeA.label, "ke", nodeB.label,":")
for path in graph.cari_path(nodeA, nodeB):
    for element in path:
        print(element, end=" ")
    print("=", end=" ")
    print(graph.hitung_biaya_path(path), end=", ")
    print(graph.hitung_biaya_nodes(path), end="")
    print()
