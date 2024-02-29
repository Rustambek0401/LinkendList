class Data:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkdlist:
    def __init__(self):
        self.hade = None
    def print(self):
        temp = self.hade
        while temp:
            print(temp.data)
            temp = temp.next
    def Push(self,new_data):
        data1 = Data(new_data)
        data1.next = self.hade
        self.hade = data1
    def insert ( self, prev_node, new_data ):
        if prev_node is None:
            print("Xatolik bor ??? ")
        data1 = Data(new_data)
        data1.next = prev_node
        prev_node.next = new_data
    def append(self,new_data):
        data1 = Data(new_data)
        if self.hade is None:
            self.hade = new_data
            return
        last = self.hade
        while last.next:
            last = last.next
        last.next = data1
a = Data(3)
b = Data(4)
c = Data(6)
d = Data(1)
f = Data(9)
aa = Linkdlist()
aa.hade = a
a.next = b
b.next = c
c.next = d
d.next = f
aa.print()