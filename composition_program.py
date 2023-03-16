class test:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
class demo:
    def __init__(self,a,b,c):
        self.obj= test(a,b)
        self.c = c

    def show1(self):
        self.obj.show()
        print(self.c)
d = demo(1,2,3)
d.show1()
