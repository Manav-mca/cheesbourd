class character:
    def __init__(self,name, health ,attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack_enemy(self):
        print("f {self.name} attack with power {self.health}")

worrir = character("thor", 100,50)
mage = character("gandle", 80, 70)

worrir.attack_enemy()
mage.attack_enemy()

    
