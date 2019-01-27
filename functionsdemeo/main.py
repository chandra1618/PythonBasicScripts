
class a:
    def __init__(self,m,n):
        self.m = m
        self.n = n
    #b = 10
    #c = "hello world"
    def printstring(self):
        print(self.m)
        return
    def doubleval(self):
        return self.n*2

m = a("hello world",2)
print(m.m)
print(m.n)
m.printstring()
o = m.doubleval()
print(o)