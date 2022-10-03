class NodeTabungan:
    class NodeTabungan:
        no_rekening = None
        nama = None
        saldo = None
        next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
         self._head=None
         self._tail=None
         self._size = 0

    def __len__(self):
        return self._size

    def insert_head(self, no_rekening, nama,saldo):
        bru = NodeTabungan(no_rekening, nama,saldo)
        if self.isEmpty()==True:
            self.head = bru
            self.tail = bru
            self.tail.next = None
        else:
            bru.next = self.head
            self.head = baru
        self.size += 1
    


            
