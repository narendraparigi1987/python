class Fraction(object):

    def __init__(self,num,denom):
        assert type(num) == int and type(denom) == int, 'Expected int but unexpected format for args'
        self.num = num
        self.denom = denom
    
    def __str__(self):
        return str(self.num)+'/'+str(self.denom)
    
    def __add__(self,other):
        top = self.num*other.denom + self.denom*other.num
        bottem = self.denom*other.denom
        return Fraction(top, bottem)
    
    def __sub__(self,other):
        top = self.num*other.denom - self.denom*other.num
        bottem = self.denom*other.denom
        return Fraction(top, bottem)
    
    def __float__(self):
        return float(self.num)/float(self.denom)
    
    def inverse(self):
        return self.denom/self.num

def main():
    a = Fraction(2,3)
    b = Fraction(3,4)
    print a
    print b
    c = a+b
    print c
    d = a-b
    print d
    print float(a)
    print Fraction.__float__(a)
    print float(a.inverse())

if __name__ == '__main__':
    main()