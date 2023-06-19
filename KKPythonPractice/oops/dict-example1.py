class Flower:
    stem = 'green'
    def __init__(self, petals=True, thorns=False) -> None:
        self.petals = petals
        self.thorns = thorns

flower = Flower()
print(type(flower.__dict__))        