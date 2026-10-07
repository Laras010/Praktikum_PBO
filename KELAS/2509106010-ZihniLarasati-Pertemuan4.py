class Hero():
    def __init__(self, name, health, attack, mana):
        self.name = name
        self.health = health
        self.attack = attack
        self.mana = mana
        self.armor = 0

    def diserang(self, jumlah):
        self._health = max(self._health - jumlah,0)

    def serang(self,target):
        damage = max(self.attack - target.armor,0)
        target.diserang(damage)
        print(f'{self.name} menyerang {target.name}, damage{damage}')

    @property
    def health(self):
        return self._health
        
    def __str__(self):
        return f'nama Hero: {self.name}'

class Archer(Hero):
    def __init__(self, name, health, attack, mana=50, missChange=50):
        super().__init__(name, health, attack, mana=50)
        self.missChange = missChange 

    def serang(self, target):
        super().serang(target)
        print(f'meyerang menggunakan panah')
        # print(f'{self.name} menyerang menggunakan panah ke {target.name}')

class EnergyArcher(Archer):
    def __init__(self, name, health, attack, mana=50, missChange=50, energy=100):
        super().__init__(name, health, attack, mana=50, missChange=50)
        self.energy = energy

    def serang(self, target):
        if self.energy >= 20:
            self.energy -= 20
            damage = max(self.attack * 2 - target.armor,0)
            target.diserang(damage)
            print(f'{self.name} menyerang {target.name}, damage {damage}, sisa energi: {self.energy}')
        else:
            print().serang(target)
            
        class Mage(Hero):
            pass    

        roger = Hero('Roger', 100, 15, 100)
        Windranger = Archer('Windranger', 80, 20, 50, 40)
        kimmy = EnergyArcher('Kimmy', 70, 25, 50, 30, 100)
        

        roger.serang(Windranger)
        Windranger.serang(roger)

