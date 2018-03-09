class intSet(object):

    def __init__(self):
        self.vals = []
    
    def __str__(self):
        return (' '.join([str(x) for x in self.vals]))
    
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
    
    def member(self,e):
        return e in self.vals
    
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) +' not found in intSet')

def main():
    a = intSet()
    print a
    a.insert(1)
    print a
    a.insert(1)
    print a
    a.insert(2)
    print a
    print a.member(1)
    a.remove(1)
    print a
    a.remove(3)

if __name__ == '__main__':
    main()