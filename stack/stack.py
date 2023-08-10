class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,node):
        #jika elemen hanya 1 maka dia sebagai kepala dan ekor
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            node_saat_ini = self.head
            while(node_saat_ini.next != None):
                node_saat_ini = node_saat_ini.next
            node_saat_ini.next = node
            node.prev = node_saat_ini
            self.tail = node
    
    def add_node_di_belakang(self, node):
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            temp = self.tail
            self.tail = node
            self.tail.prev = temp
            temp.next = self.tail

    def add_node_di_depan(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            temp.prev = self.head

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
            node_sebelum = node_saat_ini.prev
            node_saat_ini.prev = node
            node_sebelum.next =  node
            node.prev = node_sebelum
            node.next = node_saat_ini
            
    def cetak_semua_nilai(self):
        node_saat_ini = self.head
        while(node_saat_ini != None):
            print(node_saat_ini.value,end=" ")
            node_saat_ini = node_saat_ini.next
        print()

    def cetak_semua_nilai_dari_belakang(self):
        node_saat_ini = self.tail
        while(node_saat_ini != None):
            print(node_saat_ini.value,end=" ")
            node_saat_ini = node_saat_ini.prev
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
    
    def cari_index_dari_belakang(self, nilai_dicari):
        index = -1
        index_dicari = index
        node_saat_ini = self.tail
        while(node_saat_ini != None):
            index = index + 1
            if node_saat_ini.value == nilai_dicari:
                index_dicari = index
                break
            node_saat_ini = node_saat_ini.prev
        return index_dicari
    
    def ambil_node(self):
        nilai_paling_belakang = self.tail
        node_kedua_dari_belakang = self.tail.prev
        self.tail.prev = None
        node_kedua_dari_belakang.next = None
        self.tail = node_kedua_dari_belakang
        return nilai_paling_belakang
    
    def tambah_node(self, node):
        self.add_node(node)        
    
list = Stack()
list.add_node(Node(2))
list.add_node_di_depan(Node(99))
list.add_node_di_belakang(Node(33))
list.add_node_di_depan(Node(17))
list.add_node_di_index(Node(18), 1)
list.cetak_semua_nilai()

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

# nilai_dicari = 33
# print("index dari" , nilai_dicari , "adalah" , list.cari_index_dari_belakang(nilai_dicari));
# nilai_dicari = 2
# print("index dari" , nilai_dicari , "adalah" , list.cari_index_dari_belakang(nilai_dicari));