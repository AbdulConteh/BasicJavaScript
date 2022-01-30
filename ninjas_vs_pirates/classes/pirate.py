class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def haki ( self , ninja ):
        ninja.health -= self.strength
        return self

    def hook_stab ( self , ninja ):
        ninja.health -= self.strength
        return self

    def  potion ( self , ninja ):
        ninja.health += self.health
        return self 

