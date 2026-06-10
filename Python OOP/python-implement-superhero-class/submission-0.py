class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health

# TODO: Create Superhero instances
hero1 = SuperHero("Batman","Intelligence",100)
hero2 = SuperHero("Superman","Strength",150)

# TODO: Print out the attributes of each superhero
print(hero1.name)
print(hero1.power)
print(hero1.health)
print(hero2.name)
print(hero2.power)
print(hero2.health)
