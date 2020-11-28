class Toy():
    def __init__(self, name, age):
        self.name = name
        self.age = age


toy1 = Toy(name="Hummer", age=8)
# print (dict(toy1))
print (toy1.__dict__)

toy2 = Toy(**toy1.__dict__)

print (toy2)
print(toy2.name)
print(toy2.age)


