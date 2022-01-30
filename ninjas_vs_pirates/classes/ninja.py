class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nHealth:")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    def ninja_star(self, pirate):
        pirate.health -= self.strength
        return self

    def chidori(self, pirate):
        pirate.health -= self.strength
        return self

    def potion(self, ninja):
        ninja.health += self.health
        return self

@classmethod 
def change_ninja(cls, name):
    cls.ninja = name
    name = "Madara"

    def planetary_devistation():
        pass: