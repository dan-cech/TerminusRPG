import assets.utilities as utils
import assets.character as character

class consumable:
    def __init__(self,name,effect,cost,info,trigger,tag, stackable=True):
        self.name = utils.azure(name)
        self.effect = utils.green(effect)
        self.cost = utils.yellow(cost)
        self.info = utils.red(info)
        self.trigger = trigger
        self.tag = tag
        self.stackable = stackable

#=== /// CONSUMABLES \\\ ===#
#Name, Effect, Cost, Info, Trigger (the assigned function)
lesser_heal_pot = consumable("Lesser Healing Potion","Heals the player for +20 HP.",35,"Consists mostly of Red40.", lambda player: player.healSelf(20),"consum")
great_heal_pot = consumable("Great Healing Potion","Heals the player for +42 HP",50,"Tastes like skittles and oil... and Red40.", lambda player: player.healSelf(42),"consum")
lesser_mana_pot = consumable("Lesser Mana Potion","Gives the player +2 Mana",42,"Smells like mouthwash.", lambda player: player.manaUp(2),"consum")
great_mana_pot = consumable("Great Mana Potion","Gives the player +5 Mana",73,"Tastes like toothpaste with orange juice.", lambda player: player.manaUp(5),"consum")
#lesser_crit_pot
#great_crit_pot
#lesser_regen_pot
#great_regen_pot
small_pocket = consumable("Small Pocket","Adds +1 inventory slot",84,"The knitting is pretty sloppy", lambda player: player.invUp(1),"consum")
big_pocket = consumable("Big Pocket","Adds +2 inventory slot",84,"You could fit a chair in that", lambda player: player.invUp(2),"consum")

#Consumable IDs
consumables = {
    1: lesser_heal_pot,
    2: great_heal_pot,
    3: lesser_mana_pot,
    4: great_mana_pot
}