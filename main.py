class Hero():

    def __init__(self, name, Hp, armor):
        self.name = name
        self.Hp = Hp
        self.armor = armor

class Attack(Hero):

    def attack1(self,damage):
        self.Hp=self.Hp-damage


barbarian=Attack('ivan', 10, 2)

barbarian.attack1(4)