class abc:
    def getdata(self, a, b):
        self.a=a
        self.b=b
    def setdata(self):
        print(self.a)
        print(self.b)
obj1=abc()
obj2=abc()
obj1.getdata(5,9)
obj1.setdata()
obj2.getdata(8,10)
obj2.setdata()
