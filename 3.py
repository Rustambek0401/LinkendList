class List:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkendLIST:
    def __init__(self):
        self.head = None
    def Print(self):
        ded = self.head
        while ded:
            print(ded.data)
            ded = ded.next
    def Push(self,dat):
        dat1 = List(dat)
        dat1.next = self.head
        self.head = dat1
    def Insert(self,elem,dat):
        if elem is None:
            print("???? XATO ????")
        dat1 = List(dat)
        #elementga ulanadi keyin eski elementni
        # qoli uziladi va yangi orqali bir biriga ulanadi
        dat1.next = elem.next
        # yaxgi element oqali ulandi bir biriga
        elem.next = dat1
    def Append(self,dat):
        dat1 = List(dat)
        if self.head is None:
            self.head = dat1
            return
        last = self.head
        while last:
            last = last.next
        last.next = dat1
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
ele = LinkendLIST()
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
print("#"*20,'Insert',44,"dan keyin ",39 ,'ni qoshadi',"#"*20)
ele.Insert(a,39)
ele.Print()
print("#+_+#" * 20)
ele.Insert(s,333)
ele.Insert(x,222)
ele.Insert(c,111)
ele.Print()

