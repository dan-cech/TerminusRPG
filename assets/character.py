class InventorySlot:
    def __init__(self, item, amount=1):
        self.item = item
        self.amount = amount

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
            slot = self.inventory[i]
            if slot == "Empty":
                print(f"Slot {i+1}:", utils.white("Empty"))
            else:
                # pokud stackovatelný, ukaž počet
                if slot.item.stackable:
                    print(f"Slot {i+1}:", f"{slot.item.name} x{slot.amount}")
                else:
                    print(f"Slot {i+1}:", slot.item.name)
    
    def add_item(self, item, amount=1):
        if item.stackable:
            for slot in self.inventory:
                if slot != "Empty" and slot.item == item:
                    slot.amount += amount
                    return True

        
        for i in range(self.invSize):
            if self.inventory[i] == "Empty":
                self.inventory[i] = InventorySlot(item, amount)
                return True

        return False

    
    def maxStatCheck(self):
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        if self.mana > self.maxMana:
            self.mana = self.maxMana

