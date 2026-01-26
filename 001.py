"""
Charles Gauthier
407
exercice de classe#  1
"""
import math
from dataclasses import dataclass
import random



class StringFoo():
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


sf = StringFoo()

sf.set_string("obligation")
sf.print_string()



class rectangle:

    def __init__(self, longueure, largeur):
        self.longueure = longueure
        self.largeur = largeur

    def calcule_aire(self):
        self.aire = self.largeur * self.longueure
        print(self.aire)


mesure = rectangle(8, 5)
mesure.calcule_aire()




class cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def calcule_aire(self):
        self.aire = self.rayon * self.rayon * math.pi
        print(self.aire)

    def calcule_circ(self):
        self.circ = 2 * self.rayon * math.pi
        print(self.circ)


dimension = cercle(2)
dimension.calcule_aire()
dimension.calcule_circ()


@dataclass
class Hero:
    dexterite: int = random.randint(1, 6)

    def __init__(self, nom):
        self.nom = nom
        self.vie = random.randint(1, 10) + random.randint(1,10)
        self.force_attack = random.randint(1, 6)
        self.force_defence = random.randint(1, 6)

    def attack(self):
        return self.force_attack + random.randint(1, 6)

    def dommage(self, dommage):
        self.vie += self.force_defence - dommage
        print(self.vie)

    def alive(self):
        return self.vie > 0


darren = Hero("darren")
darren.dommage(4)
if darren.alive():
    print("il est vivant")



@dataclass
class DonneesPerso:
    force: int = random.randint(1,6)
    dexterite: int = random.randint(1,6)
    constitution: int = random.randint(1, 6)
    inteligence: int = random.randint(1, 6)
    sagesse: int = random.randint(1, 6)
    charisme: int = random.randint(1, 6)


class NPC:
    def __init__(self):
        self.stats = DonneesPerso()


z = NPC()


print(z.stats)

