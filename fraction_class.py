class fraction(object):
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
    def __str__(self):
        return str(self.num)+'/'+str(self.denom)
    def get_num(self):
        return self.num
    def get_denom(self):
        return self.denom
    def __add__(self,other):
        num_add=(self.num*other.denom)+(self.denom*other.num)
        denom_add=(self.denom*other.denom)
        return fraction(num_add,denom_add)
    def __sub__(self,other):
        num_sub=(self.num*other.denom)-(self.denom*other.num)
        denom_sub=(self.denom*other.denom)
        return fraction(num_sub,denom_sub)
    def convert(self):
        return self.num/self.denom
