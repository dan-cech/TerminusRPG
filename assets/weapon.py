import assets.utilities as utils

class weapon:  
    def __init__(self,name,dmg,cost,info,tag):
        self.name = utils.azure(name)
        self.dmg = dmg
        self.cost = utils.yellow(cost)
        self.info = utils.blue(info)
        self.tag = tag

#=== /// WEAPONS \\\ ===#
#Name, DMG, Cost, Info
rusty_sword = weapon("Rusty Sword",14,50,"Old, rusty sword, Better than nothing.","weapon")
giant_hammer = weapon("Giant Hammer",31,89,"Giant sledgehammer weighing atleast for washing machines.","weapon")
old_pickaxe = weapon("Old Pickaxe",20,30,"An old pickaxe used by slaves in the Educanet corp.","weapon")
greatsword = weapon("Greatsword",28,68,"And old sword once used by the order of Dušek.","weapon")
empty_gun = weapon("Empty Gun",10,95,"An old gun once used by the nefarious Wisman gang.","weapon")
new_magic_wand = weapon("New Magic Wand",21,43,"I saw a photo you looked joyous...","weapon")
long_bow = weapon("Long Bow",20,54,"A wooden long bow handcrafted by unpaid Temu workers.","weapon")
#fencing_sword
#greed_dagger - gives coins after every hit
#vampire_blade - heals after every hit
#iron_fists
#battle_axe
#fish
#crystal_saber
#hell_fork
#shadow_edge - 2x dmg in Atrium
#star_splitter

#Weapon IDs
weapons = {
    1: rusty_sword,
    2: giant_hammer,
    3: old_pickaxe,
    4: greatsword,
    5: empty_gun,
    6: new_magic_wand,
    7: long_bow
}