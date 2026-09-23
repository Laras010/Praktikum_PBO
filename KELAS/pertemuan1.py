# class Hero:
#     pass

# hero1 = Hero()

# hero1.name = 'sniper'

# print

class Hero:
    jumlahHero = 0
    
    def __init__(self, nama, health, armor, attack):
        self.nama = nama
        self.health = health
        self.armor = armor
        self.attack = attack
        Hero.jumlahHero += 1

    def serang(self, lawan):
        print(f' {self.nama} menyerang {lawan.nama} ')
        lawan.diserang(self, self.attack)
    
    def diserang(self, lawan, attack_lawan):
        print(self.nama + ' diserang ' + lawan.nama)
        attack_diterima = attack_lawan
        self.health -= attack_diterima
        print(f' darah {self.nama} tersisa {self.health} ')

    def healing(self, amount):
        print(self.health)
        self.healh += amount
        print(self.health)


roger = Hero('roger', 100, 4, 15)
sniper = Hero('sniper', 50, 5, 30)

sniper.serang(roger)
roger.diserang(sniper)
sniper.healing(15)


#     def healthUp(self, up):
#         self.health += up

#     def levelUp(self):
#         self.health += 10
#         self.armor += 2
#         self.attack += 5

    

# roger = Hero('roger', 100, 4, 15)
# print(roger.nama)


# roger = Hero('roger', 100, 4, 15)
# print(roger.nama)
# sniper = Hero('sniper', 50, 5, 30)

