class MathDojo(object):
    def __init__(self):
        self.var = 0
    def add(self, *arg):
        for i in arg:
            self.var += i
        return self
    def subtract(self, *arg):
        temp = 0
        for i in arg:
            temp += i
        self.var -= temp
        return self
    def p(self):
        print self.var
        return self


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).p()