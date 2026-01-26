import random

class hero:

    def __init__(self, nom):
        self.nom = nom
        self.vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_attack = random.randint(1,6)
        self.force_defense = random.randint(1,6)



    def attack(self):
        return self.attack + random.randint(1,6)


    def dommage(self, dommage):
        self.vie += self.defence - dommage
        print(self.vie)


    def alive(self):
        -