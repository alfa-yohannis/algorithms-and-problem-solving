class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None

    def cetak_tree_dalam(self):
        self.rekursif_cetak_tree_dalam(self.root)
        print()

    def rekursif_cetak_tree_dalam(self,node):
        print(node.value, end=" ")
        for child in node.children:
            self.rekursif_cetak_tree_dalam(child)
    
    def cetak_tree_lebar(self):
        print(self.root.value, end=" ")
        self.rekursif_cetak_tree_lebar(self.root)
        print()

    def rekursif_cetak_tree_lebar(self,node):
        for child in node.children:
            print(child.value, end=" ")

        for child in node.children:
            self.rekursif_cetak_tree_lebar(child)

    def cari_node_lebar(self, value):
        if self.root.value == value:
            return self.root
        
        node = self.rekursif_cari_node_lebar(self.root, value)
        return node

    def rekursif_cari_node_lebar(self, node, nilai_dicari):

        for child in node.children:
            if child.value == nilai_dicari:
                return child

        for child in node.children:
            node_dicari = self.rekursif_cari_node_lebar(child, nilai_dicari)
            if node_dicari != None:
                return node_dicari
        
        return None
    
    def cari_node_dalam(self, value):
        node = self.rekursif_cari_node_dalam(self.root, value)
        return node

    def rekursif_cari_node_dalam(self, node, nilai_dicari):
        if node.value == nilai_dicari:
            return node
        
        for child in node.children:
            node_dicari = self.rekursif_cari_node_dalam(child, nilai_dicari)
            if node_dicari != None:
                return node_dicari
        return None


    
tree = Tree()
nodeA, nodeB, nodeC, nodeD = Node("A"), Node("B"), Node("C"), Node("D")
nodeE, nodeF =  Node("E"), Node("F")
tree.root = nodeA
nodeA.children.append(nodeB)
nodeB.parent = nodeA
nodeA.children.append(nodeC)
nodeC.parent = nodeA
nodeB.children.append(nodeD)
nodeD.parent = nodeB
nodeB.children.append(nodeE)
nodeE.parent = nodeB
nodeC.children.append(nodeF)
nodeF.parent = nodeC
# tree.root = nodeA
# print("Cara Dalam Dulu: ", end="")
# tree.cetak_tree_dalam()
# print("Cara Lebar Dulu: ", end="")
# tree.cetak_tree_lebar()
nilai_dicari = "B"
node = tree.cari_node_lebar(nilai_dicari)
# node = tree.cari_node_dalam(nilai_dicari)
if (node != None):
    print("Cari", nilai_dicari, ": ketemu node", node.value)
    print("parent dari", node.value, " = ", node.parent.value)
    for child in node.children:
        print(child.value," anak dari",node.value)
else:
    print("Cari", nilai_dicari, ": tidak ketemu")
