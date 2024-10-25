# SINGLE INHERITANCE

class Parent:                                                       # Base Class
    def func1(self):
        print("\nThis function is in parent class.")
 
class Child(Parent):                                                # Derived Class         # a -> b
    def func2(self):
        print("This function is in child class.")
 
object = Child()                                                    # Object
object.func1()
object.func2()


# MULTIPLE INHERITANCCE

class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername) 
 
class Son(Mother, Father):                                             # a ->  c  <- b 
    def parents(self):
        print("\nFather's name is : ", self.fathername)
        print("Mother's name is : ", self.mothername)

s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()


# MULTILEVEL INHERITANCE

class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):                                                        # a ->  b  -> c
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('\nGrandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

s1 = Son('Sun-Jae', 'Tae-Moo', 'Min-Hyuk')
#print(s1.grandfathername)
s1.print_name()


# HIERARCHICAL INHERITANCE

class Parent:
    def func1(self):
        print("\nThis function is in parent class.")

class Child1(Parent):                                          # a -> b
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):                                          # a -> c
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# HYBRID INHERITANCE

class School:
    def func1(self):
        print("\nThis function is in school.")
 
class Student1(School):                                          # a -> b
    def func2(self):
        print("This function is in student 1. ")
 
class Student2(School):                                          # a -> c
    def func3(self):
        print("This function is in student 2.") 
 
class Student3(Student1, School):                                # a , b -> d
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()
object.func4()
obj = Student2()
obj.func3()
