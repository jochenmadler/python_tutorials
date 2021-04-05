# defining class Dog and then playing around with it

class Dog:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getInfo(self):
        print(self.name + " is " + str(self.age) + " years old.")

    def setBuddy(self,buddy):
        self.buddy = buddy      # added new attribute on the get go
        buddy.buddy = buddy

    def getBuddy(self):
        print(self.name + "'s buddy is " + self.buddy.getName())


doggo1 = Dog("Sina", 3)
doggo2 = Dog("Kimba", 4)

doggo1.setBuddy(doggo2)
doggo1.getBuddy()

