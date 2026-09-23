class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack =attack

    @property
    def getName(self):
        return self.name 

    @property
    def health(self):
        return self.__health

    @property
    def heroPower(self):
        return self.__health + (self.armor * 1.5)

    @health.setter 
    def health(self, darahBaru):
        if darahBaru <=0:
            self.__health = 0
        else:
            self.__health = darahBaru

    @armor.deleter
    def armor(self):
        self.armor = 0

sniper = Hero('sniper', 100, 4, 15)
print(sniper.__dict__)
del sniper.health
print(sniper.__dict__)
# print(sniper.armor)
# print(sniper.getName)
# sniper.name = 'roger'
# print(sniper.name)
# print(sniper.heroPower)