class MathDojo(object):
    def __init__(self):
        self.var = 0
    def add(self, *arg):
        for i in arg:
            print i,
        if type(i) == list or type(i) == tuple:
            for j in i:
                self.var += j
                print self.var
        elif type(i) == int:
            for k in arg:
                self.var += i
                print self.var
        return self
    def subtract(self, *arg):
        temp = 0 
        for i in arg:
            print i,
        if type(i) == list or type(i) == tuple:
            for j in i:
                self.var -= j
                print self.var
        elif type(i) == int:
            for k in arg:
                self.var -= i
                print self.var
        return self
    def p(self):
        print self.var,'<00000000000000000000'
        return self


md = MathDojo()
md.add([1,2,3,4],10,10).subtract([10,5],5,(10)).p()