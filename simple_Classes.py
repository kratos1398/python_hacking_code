class Animal(object):
    def __init__(self,name,age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey",12,True)
lion = Animal("Alex",16,False)
girraffe = Animal("Glen",45,True)
print("{} : {} : {}".format(zebra.name,zebra.age,zebra.is_hungry))
print("{} : {} : {}".format(lion.name,lion.age,lion.is_hungry))
print("{} : {} : {}".format(girraffe.name,girraffe.age,girraffe.is_hungry))