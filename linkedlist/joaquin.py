
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            node_saat_ini = self.head
            while node_saat_ini.next is not None:
                node_saat_ini = node_saat_ini.next
            node_saat_ini.next = node
    
    def add_node_di_depan(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def add_node_di_index(self, node, index_dicari):
        index = 0
        node_saat_ini = self.head
        node_sebelum = None
        while node_saat_ini is not None:
            index = index + 1
            node_sebelum = node_saat_ini
            node_saat_ini = node_saat_ini.next
            if index == index_dicari:
                break
        if index_dicari == 0:
            self.add_node_di_depan(node)
        else:
            temp = node_saat_ini
            node_sebelum.next = node
            node.next = node_saat_ini
            
    def cetak_semua_nilai(self):
        node_saat_ini = self.head
        while node_saat_ini is not None:
            print(node_saat_ini.value, end=" ")
            node_saat_ini = node_saat_ini.next
        print()

    def cari_index(self, node, nilai_dicari):
        index = -1
        index_dicari = index
        node_saat_ini = self.head
        while node_saat_ini is not None:
            index = index + 1
            if node_saat_ini.value == nilai_dicari:
                index_dicari = index
                break
            node_saat_ini = node_saat_ini.next
        return index_dicari

    def hapus_node_di_index(self, index_dicari):
        if index_dicari == 0:
            if self.head is not None:
                self.head = self.head.next
        else:
            index = 0
            node_saat_ini = self.head
            node_sebelum = None
            while node_saat_ini is not None:
                if index == index_dicari:
                    if node_sebelum is not None:
                        node_sebelum.next = node_saat_ini.next
                    break
                index += 1
                node_sebelum = node_saat_ini
                node_saat_ini = node_saat_ini.next

    def update_nilai_node_di_index(self, index_dicari, nilai_baru):
        index = 0
        node_saat_ini = self.head
        while node_saat_ini is not None:
            if index == index_dicari:
                node_saat_ini.value = nilai_baru
                break
            index += 1
            node_saat_ini = node_saat_ini.next

    def update_nilai_node_tertentu(self, nilai_dicari, nilai_baru):
        node_saat_ini = self.head
        while node_saat_ini is not None:
            if node_saat_ini.value == nilai_dicari:
                node_saat_ini.value = nilai_baru
            node_saat_ini = node_saat_ini.next


list = SingleLinkedList()
list.add_node(Node(2))
list.add_node_di_depan(Node(99))
list.add_node(Node(33))
list.add_node_di_depan(Node(17))
list.add_node_di_index(Node(18), 0)

list.cetak_semua_nilai()  

# list.hapus_node_di_index(5)
# list.cetak_semua_nilai()  

list.update_nilai_node_di_index(2, 100)
list.cetak_semua_nilai()  

list.update_nilai_node_di_index(4, 0)
list.cetak_semua_nilai()  

list.update_nilai_node_tertentu(18, 50)
list.cetak_semua_nilai() 