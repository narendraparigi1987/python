import random

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname = ""):
        self.name = newname
    def __str__(self):
        return 'Animal: '+str(self.name)+' with age '+str(self.age)

# a = Animal(4)
# print(a)
# print(a.get_age())
# a.set_name('fluffy')
# print(a.get_name())
# a.set_name()
# print a

class Cat(Animal):
    def speak(self):
        print 'Meow'
    def __str__(self):
        return 'Cat: '+str(self.name)+' with age '+str(self.age)

# c = Cat(4)
# print c
# print (c.get_age())
# c.set_name('My cat')
# print c
# c.speak()

class Person(Animal):
    def __init__(self,age,name):
        Animal.__init__(self,age)
        self.name = name
        self.friends = []
    def get_friends(self):
        return self.friends
    def speak(self):
        print 'Hellow'
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self,other):
        return self.age - other.age
    def __str__(self):
        return 'Person: '+str(self.name)+' with age '+str(self.age)

# p = Person(4,'Naren')
# q = Person(10,'Aruna')
# print p
# print q
# p.set_name('Narendra')
# print p
# p.add_friends('Hari')
# print p.get_friends()
# p.speak()
# print p.age_diff(q)

class Student(Person):
    def __init__(self, age, name, major=None):
        Person.__init__(self,age,name)
        self.major = major
    def __str__(self):
        return 'Student: '+str(self.name)+' with age '+str(self.age)
    def change_major(self,nmajor):
        self.major = nmajor
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

# s = Student(10,'Naren','CS')
# print s
# s.speak()
# print s.get_name()

class Rabbit(Animal):
    tag = 1 # class variable and it is shared by all instances of a class
    def __init__(self,age,parent1=None, parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __str__(self):
        return "rabbit:"+ self.get_rid()
    def __add__(self,other):
        return Rabbit(0,self,other)
    def __eq__(self,other):
        parent_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parent_opposites = self.parent2.rid == other.parent1.rid and self.parent1.rid  == other.parent2.rid
        return parent_same or parent_opposites



r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
r4 = r1+r2

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print r3
print r4
print r5
print r6
print r5.get_parent1()
print r5.get_parent2()
print r6.get_parent1()
print r6.get_parent2()
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)