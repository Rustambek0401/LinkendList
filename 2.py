class List:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def Print(self):
        a = self.head
        while a:
            print(a.data)
            a = a.next
    def Push(self,data1):
        data2 = List(data1)
        # yangi tugun haosil qildi
        data2.next = self.head
        # bunda qo'shilgan elementni bosh yani boshlanishi deb
        #qabul qiladi
        self.head = data2
    def Insert(self,element,data1):
        if element is None:
            print("xatalik")
        # List degan kilasga yuboradi
        data2 = List(data1)
        # Listdagi element tuguni bilan yangi element tugunini ulaymiz
        data2.next = element.next
        # listdagi elementdan keyin yangi element kelishini aytib qo'ydik
        element.next = data2
    def Append(self,data1):
        data2 = List(data1)
        if self.head is None:
            #elementni boshi bo'lmas yangi qo'shilgan elementni boshi deb qabulqil
            self.head = data2
        return
        ese = self.head
        while ese:
            # ese elementdan keyin yana ese keladi deb aytib qo'yiladi While da
            # oxirgi elementgacha boradida toxtayfi keyin
            ese = ese.next
        # bunda data2 elementni oxirgi deb qabul qiladi
        ese.next = data2
z = List(2)
x = List(1)
c = List(4)
v = List(12)
b = List(42)
n = List(21)
m = List(34)
a = List(44)
s = List(65)
d = List(75)
ele = Linkedlist()
# bunda eng birinchi element qaysiligi aytiladi
ele.head = z
# bunda ese keyingi elemen bilan ulanadi
z.next = x
x.next = c
c.next = v
v.next = b
b.next = n
n.next = m
m.next = a
a.next = s
s.next = d
ele.Print()
print("#"*20,'Push',43,"#"*20)
ele.Push(43)
ele.Print()

# print("#"*20,'Apend',"#"*20)
# q = List(111)
# ele.Append(q)
# ele.Print()


