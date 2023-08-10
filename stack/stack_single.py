class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackSingle:
    def __init__(self):
        self.head = None

    def add_node(self,node):
        if self.head == None:
            self.head = node
        else:
            node_saat_ini = self.head
            while(node_saat_ini.next != None):
                node_saat_ini = node_saat_ini.next
            node_saat_ini.next = node
    
    def add_node_di_depan(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def add_node_di_index(self, node, index_dicari):
        index = 0
        node_saat_ini = self.head
        node_sebelum = None
        while(node_saat_ini != None):
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
        while(node_saat_ini != None):
            print(node_saat_ini.value,end=" ")
            node_saat_ini = node_saat_ini.next
        print()

    def cari_index(self, node, nilai_dicari):
        index = -1
        index_dicari = index
        node_saat_ini = self.head
        while(node_saat_ini != None):
            index = index + 1
            if node_saat_ini.value == nilai_dicari:
                index_dicari = index
                break
            node_saat_ini = node_saat_ini.next
        return index_dicari
    
    def dapatkan_node_terakhir(self):
        if self.head == None:
            return None
        node_saat_ini = self.head
        while(node_saat_ini.next != None):
            node_saat_ini = node_saat_ini.next
        return node_saat_ini
    
    def tambah_node(self, node):
        self.add_node(node)    

    def ambil_node(self):
        if self.head == None:
            return None
        node_saat_ini = self.head
        node_sebelum_node_saat_ini = None
        while(node_saat_ini.next != None):
            node_sebelum_node_saat_ini = node_saat_ini
            node_saat_ini = node_saat_ini.next
        node_sebelum_node_saat_ini.next = None
        node_paling_belakang = node_saat_ini
        return node_paling_belakang
   
list = StackSingle()
list.add_node(Node(2))
list.add_node_di_depan(Node(99))
list.add_node(Node(33))
list.add_node_di_depan(Node(17))
list.add_node_di_index(Node(18), 0)
list.cetak_semua_nilai()

node_terakhir = list.dapatkan_node_terakhir()
print("Node terakhir:",node_terakhir.value)

nilai_paling_depan = list.ambil_node()
print("Nilai diambil =", nilai_paling_depan.value)
list.cetak_semua_nilai()

nilai_paling_depan = list.ambil_node()
print("Nilai diambil =", nilai_paling_depan.value)
list.cetak_semua_nilai()

nilai_paling_depan = list.ambil_node()
print("Nilai diambil =", nilai_paling_depan.value)
list.cetak_semua_nilai()

node_baru = Node(45)
list.add_node(node_baru)
print("Nilai ditambahkan =", node_baru.value)
list.cetak_semua_nilai()

nilai_paling_depan = list.ambil_node()
print("Nilai diambil =", nilai_paling_depan.value)
list.cetak_semua_nilai()

node_baru = Node(32)
list.add_node(node_baru)
print("Nilai ditambahkan =", node_baru.value)
list.cetak_semua_nilai()