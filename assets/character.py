class Player:
    def __init__(self, hp, maxHp, coins, dmgMult, mana, maxMana, invSize):
        self.hp = hp
        self.maxHp = maxHp
        self.coins = coins
        self.dmgMult = dmgMult
        self.mana = mana
        self.maxMana = maxMana
        self.invSize = invSize

        self.inventory = []
        for _ in range(self.invSize):
            self.inventory.append("Empty")
    
    def healSelf(self, value):
        self.hp += value
    
    def manaUp(self, value):
        self.mana += value

    def invUp(self, value):
        self.invSize += value
        for _ in range(value):
            self.inventory.append("Empty")
    
    def inventoryOpen(self):
        import assets.utilities as utils
        print(utils.white(r"\n#*=== /// INVENTORY \\\\\ ===*#"))
        for i in range(self.invSize):
            item = self.inventory[i]
            if item == "Empty":
                print(f"Slot {i+1}:", utils.white("Empty"))
            else:
                print(f"Slot {i+1}:", item.name)
    
    def maxStatCheck(self):
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        if self.mana > self.maxMana:
            self.mana = self.maxMana

