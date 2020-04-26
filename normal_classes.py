class Animal(object):
    def __init__(self,name,age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
    def description(self):
        print(self.name)
        print(self.age)
zebra = Animal("Morty",16,True) # must have 3 parameters because its specified in init__()
zebra.description()  