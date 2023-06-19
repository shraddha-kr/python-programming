class Flower:
    stem = 'green'
    def __init__(self, petals=True, thorns=False):
        self.petals = petals
        self.thorns = thorns

flower = Flower()
print(type(flower.__dict__))
print(flower.__dict__)

flower = Flower(False) # The first possible argument value match is picked and used
flower.__leaves = True
print(flower.__dict__) 