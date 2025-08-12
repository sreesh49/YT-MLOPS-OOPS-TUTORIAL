

#single or Basic Inheritance

#Base class

class parent:

    def __init__(self, name):
        self.name=name
    
    def greet(self):
        print(f'Hello,my name is {self.name}.')


#Derived Class

class Child(parent):

    def play(self):
        print(f"{self.name} is playing")

#Create an instance of Child.

child=Child("Alice")
child.greet() #Output:Hello,my name is Alice

child.play()   #Output:Alice is playing


#...............................


#Multi level inheritance

#Base class

class Grandparent:

    def __init__(self,name):
        self.name=name
    def tell_story(self):
        print(f'{self.name} tells a story')

#Intermediate class

class Parent(Grandparent):

    def work(self):
        print(f'{self.name} is working')


#Derived class

class Child(Parent):


    def play(self):
        print(f'{self.name} is playing')



#create an instance of child.

child = Child("Charlie")
child.tell_story()  #output:charlie tells a story
child.work()        #output:charlie is working
child.play()        #output:charlie is playing 


#--------------------------------------------

#Hierchical Inheritance

#Base class

class Parent:

    def __init__(self,name):
        self.name= name

    def greet(self):

        print(f'hello,my name is {self.name}')

#Derived class

class Child1(Parent):

    def play(self):

        print(f'{self.name} is playing')

#Derived class 2

class Child2(Parent):

    def study(self):
        print(f"{self.name} is studying")

#create instance of child 1 and child 2

child1=Child1("Dave")
child2=Child2("Eve")

child1.greet()   #output:Hello,my name is Dave
child1.play()    #output:Dave is playing


child2.greet()   #output:Hello,my name is Eve
child2.play()    #output:Eve is studying.

#----------------------------------------------------------------


#Multiple Inheritance (Diamond Problem)


#Common base class


class A:
    def __init__(self,name):

        self.name=name

    def greet(self):
        print(f"Hello from A,{self.name}")

#intermediate class 1

class B(A):

    def greet(self):

        print(f"Hello from B,{self.name}.")
        super().greet()

#Intermediate class 2

class C(A):

    def greet(self):

        print(f"Hello from C,{self.name}.")

#Derived class

class D(B,C):

    def greet(self):
        print(f'Hello from D,{self.name}.')
        super().greet()

#Create an instance of D

d=D("Frank")
d.greet()

#Output

#Hello from D,Frank.
#Hello from B,Frank.
#Hello from C,Frank.
#Hello from A,Frank.

#----------------------------

#Hybrid Inheritance

#Base class

class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f'{self.name} makes a sound')

#Intermediate class1(Hierarchical)

class Mammel(Animal):

    def feed(self):
        print(f"{self.name} is feeding milk")

#Intermediate class 2(Multiple)

class Bird(Animal):
    def fly(self):
        print(f'{self.name} is flying')


#derived class (multiple inheritance)


class Bat(Mammel,Bird):
    def __init__(self,name):

        Mammel.__init__(self,name)  #Explicitly calling the constructor

    def nocturnal(self):

        print(f"{self.name} is nocturnal")


#Create an instance of BAt

bat=Bat("Bruce")

bat.sound() #output:Bruce makes a sound.

bat.feed()  #output:Bruce is feeding milk

bat.fly()   #output:Bruce is flying
bat.nocturnal()  #Output:Bruce is nocturnal.



