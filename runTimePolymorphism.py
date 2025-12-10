class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("BARK BARK")

class Cat(Animal):
    def sound(self):
        print("MEOW MEOW")

a= Animal()
d= Dog()
c= Cat()

a.sound()
d.sound()
c.sound()