class Hero():

    def __init__(self, name, Hp, armor):
        self.name = name
        self.Hp = Hp
        self.armor = armor

    def Atakca(self):
        if self.armor > 0:
            self.armor -= 10
            if self.armor < 0:
                self.armor = 0
        else:
            self.Hp -= 10
            if self.Hp < 0:
                self.Hp = 0

class Knight(Hero):

    def __init__(self, name, Hp, armor, ):
        super().__init__(name, Hp, armor)


class Knight2(Hero):

    def __init__(self, name, Hp, armor):
        super().__init__(name, Hp, armor)

Knight1 = Knight('Ivan ', 99, 99)
Knight21 =Knight2('A4 ', 50, 50)

while True:
    if Knight21.Hp <= 0:
        print(Knight1.name + 'победил')
        break
    elif Knight1.Hp <= 0:
        print(Knight21.name + 'победил')
        break

    Knight1.Atakca()
    print(f"у {Knight1.name} осталось {Knight1.Hp} здаровья и {Knight1.armor} брони")

    Knight21.Atakca()
    print(f'у {Knight21.name} осталось {Knight21.Hp} здаровья и {Knight21.armor} брони')