class Enemy:
    def __init__(self,name,hp,maxHp,dmg,loot,isBoss=False,bossLoot=None):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.dmg = dmg
        self.loot = loot

    def __str__(self):
        return self.name


#=== /// ENEMIES \\\ ===#
#Name, HP, MaxHP, DMG, Loot

#Basic enemies
goblin = Enemy("Goblin",45,45,6,21)
skeleton = Enemy("Skeleton",25,25,7,11)
brute = Enemy("Brute",68,68,9,20)
wisman_gang_member = Enemy("Wisman Gang Member", 40,40,9,30)
dusek_cultist = Enemy("Order of Dušek Cultist",64,64,10,24)
gurt = Enemy("Gurt",30,30,4,6)

#Mini-Bosses
matyas_janousek = Enemy("Matyáš Janoušek",100,100,18,121)
moto_moto = Enemy("Moto Moto",135,135,8,4)
dusek_acolyte = Enemy("Order of Dušek Acolyte",114,114,17,130)

#Bosses
meat_wall = Enemy("Meat Wall",187,187,4,217)

#Enemy IDs
enemies = {
    1: goblin,
    2: skeleton,
    3: brute,
    4: brute,
    5: dusek_cultist,
    6: gurt,
    7: matyas_janousek,
    8: moto_moto,
    9: dusek_acolyte,
}