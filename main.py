#Made by Daniel Čech

import random, os, sys, time, pygame

import assets.utilities as utils
import assets.weapon as weapon
import assets.consumable as consumable
import assets.floor as floor
import assets.character as character
import assets.enemy as enemy
import assets.loottables as loottables

pygame.init()


utils.clear()
print("#=== /// TERMINUS RPG \\\\\ ===#")
input("> ")
utils.clear()
nameSet = False

# Setting your name
while nameSet == False:
    utils.clear()
    print(utils.azure("Who are you..."))
    username = input("> ")

    utils.clear()
    if username == "":
        username = "Unknown"
    print(utils.azure(f"Are you sure? -"),utils.green(username))
    print("0 = No")
    print("1 = Yes")
    choice = str(input("> "))

    if choice == "1":
        nameSet = True
    elif choice == "0":
        continue
    else:
        print(utils.red("Invalid input!"))
        input()

player = character.Player(100, 100, 0, 1, 0, 5, 5)

equippedWeapon = weapon.weapons[1]
equippedConsum = consumable.consumables[2]
roomsCleared = 0
currentFloor = floor.floors[1]
utils.clear()

#=== /// MAIN GAMEPLAY LOOP \\\ ===#
while player.hp > 0:
    print(f"Floor: {currentFloor}\n")
    print(f"HP: {utils.green(player.hp)}/{utils.green(player.maxHp)}")
    print(f"Mana: {utils.blue(player.mana)}/{utils.blue(player.maxMana)}")
    print(f"Rooms cleared:",utils.azure(roomsCleared))
    print(f"Gold:",utils.yellow(player.coins))
    print(f"Equipped weapon: {equippedWeapon.name} - {utils.red(f"{equippedWeapon.dmg} DMG")}")
    print("＿＿＿＿＿＿＿＿＿＿\n")
    print(utils.azure("What will you do?"))
    print("1 = Go to next room | 2 = Inventory")
    choice = str(input("> "))

    if choice == "exit":
        exit()

    #Entering the next room
    if choice == "1":
        utils.clear()
        utils.wait(1)
        utils.clear()

        #Chooses the room type
        
        roomType = random.randint(1,3)
        print("You entered the next room.")
        if roomType == 1:
            coinRoom = random.randint(1,5)
            if coinRoom in (1,2,3,4):
                print(utils.azure(f"Just an empty room."))
                roomsCleared += 1
            else:
                print(utils.azure(f"Empty room with a handful of coins on the floor."))
                receivedCoins = random.randint(5,16)
                player.coins += receivedCoins
                print(utils.yellow(f"+{receivedCoins} coins."))
                roomsCleared += 1
            input()
        elif roomType == 2:
            print(utils.red("There's an enemy blocking the way!"))
            input()
            

            #Battle Loop
            opponent = enemy.enemies[random.randint(1,2)]
            opponent.hp = opponent.maxHp
            utils.clear()
        
            while player.hp > 0 and opponent.hp > 0:
                print(f"{username}'s HP: {player.hp}/{player.maxHp}")
                print(f"{opponent.name}'s HP: {opponent.hp}/{opponent.maxHp}\n")

                #Player Turn
                print("#=== /// PLAYER TURN \\\\\ ===#\n")
                print(utils.azure("What will you do?"))
                print("1 = Attack | 2 = Inventory")
                choice = str(input("> "))
                

                if choice == "1":

                    dealtDMG = equippedWeapon.dmg * player.dmgMult
                    opponent.hp -= dealtDMG
                    print(f"\nYou've dealt {utils.red(dealtDMG)} DMG.")
                    

                    #Enemy Turn
                    
                    if opponent.hp > 0:
                        print("\n#=== /// ENEMY TURN \\\\\ ===#\n")
                        player.hp -= opponent.dmg
                        print(f"The enemy dealt {opponent.dmg} DMG.")
                        
                    else:
                        print("The enemy died before it could attack back.")
                else:
                    print(utils.red("Invalid input!"))
                input()

                utils.clear()
            if player.hp > 0:
                
                print(utils.yellow("You won!"))
                player.coins += opponent.loot
                roomsCleared += 1
            elif player.hp < 0:
                print(utils.red("You lost!"))
            
            player.mana += 1
            if player.mana > player.maxMana:
                player.mana = player.maxMana
            input()
            
        elif roomType == 3:
            print(utils.yellow("You found a treasure a chest!"))
            input()
            utils.clear()

            #chest frame1
            print(r"""
    -Enter to open-
                  

      ..-------..
     //         \\
    ||====.-.====||
    ||   <=O=>   ||
    ||____'-'____||
    '-------------'
            """)
            
            loot = random.choices(list(loottables.chestLootTable.keys()), weights=list(loottables.chestLootTable.values()), k=1)[0]
            input()
            utils.wait(0.5)
            utils.clear()
            
            #chest frame2
            print(r"""
      .=='''''==.
      ||       || 
      ||       ||
      ||_______||  
     .'|       |'.
    ||====.-.====||
    ||   <=O=>   ||
    ||____'-'____||
    '-------------'           
            """)
            print(f"You found: {loot.name}")
            for i in range(len(player.inventory)):
                        if player.inventory[i] == "Empty":
                            player.inventory[i] = loot
                            break

            roomsCleared += 1
            input()

    #Opening inventory
    elif choice == "2":
        invOpen = True
        while invOpen == True:
            utils.clear()
            player.inventoryOpen()
            print(utils.azure("\nWhat will you do?"))
            print("1 = Back | 2 = Manage Inventory")
            choice = str(input("> "))

            #Go back
            if choice == "1":
                invOpen = False

            #Manage Inv
            elif choice == "2":
                utils.clear()
                player.inventoryOpen()

                slotSelected = False
                invSlotAmount = len(player.inventory)
                print(utils.azure("\nSelect slot number:"))
                choice = str(input("> "))
                if choice == "":
                    print(utils.red("Invalid input!"))
                    input()
                    continue

                chosenIndex = (int(choice)-1)
                if player.inventory[chosenIndex]=="Empty":
                    print("Selected slot is empty.")
                    input()
                else:

                    selectedItem = player.inventory[chosenIndex]
                    print("\nSelected item:",selectedItem.name)


                    #WEAPON
                    if selectedItem.tag == "weapon":
                        print(utils.red(f"{selectedItem.dmg} DMG"))
                        print(f"{utils.red(selectedItem.info)}")
                        print(utils.azure("\nWhat will you do?"))
                        print("1 = Back | 2 = Equip | 3 = Toss")

                        choice = str(input("> "))
                        if choice == "1":
                            continue
                        elif choice == "2":
                            player.inventory[chosenIndex] = equippedWeapon

                            currentWeapon = equippedWeapon
                            equippedWeapon = selectedItem
                        elif choice == "3":
                            print(f"\nAre you sure you want to throw {player.inventory[chosenIndex].name} away?")
                            print(f"1 = Yes | 2 = No")
                            choice = str(input("> "))
                            if choice == "1":
                                player.inventory[chosenIndex] = "Empty"
                            elif choice == "2":
                                continue
                            else:
                                print(utils.red("Invalid Input!"))
                                input()
                            

                    
                    #CONSUM
                    elif selectedItem.tag == "consum":
                        print(f"{selectedItem.effect}")
                        print(f"{selectedItem.info}")
                        print(utils.azure("\nWhat will you do?"))
                        print("1 = Back | 2 = Use | 3 = Toss")
                        choice = str(input("> "))

                        if choice == "1":
                            continue
                        elif choice == "2":
                            selectedItem.trigger(player)
                            player.maxStatCheck()
                            player.inventory[chosenIndex] = "Empty"
                        elif choice == "3":
                            print(f"\nAre you sure you want to throw {player.inventory[chosenIndex].name} away?")
                            print(f"1 = Yes | 2 = No")
                            choice = str(input("> "))
                            if choice == "1":
                                player.inventory[chosenIndex] = "Empty"
                            elif choice == "2":
                                continue
                            else:
                                print(utils.red("Invalid Input!"))
                                input()

            else:
                print(utils.red("Invalid Input!"))
                input()
    else:
        print(utils.red("Invalid input!"))
        input()
    utils.clear()

#-- TO-DO LIST --
#   Add new floors
#   Add sound effects / Music if possible

#SHOPKEEPER
#   -Every 15 rooms, there's a guaranteed encounter with the shopkeeper. He lets you buy from 5 randomly selected items
#   (based on the floor you're at)
#   (the shopkeeper's appearance will be determined by the floor you're on.)

#Different floors, which will get harder as the player progresses further. New enemies, new weapons, new items.
#   -Basement, Labyrinth, Catacombs, Atrium
#   -SPECIAL FLOORS
#       -Arena - A special floor which only consists of battles every turn.

#ROOM TYPES
#   -Empty room (Chance to find free gold)
#   -Battle room (Random enemy based on the floor)
#   -Treasure room (Gives you one random item based on the floor)
#   -Shop (Lets you spend your gold on randomly selected items)
#   -Archive (Let's you choose from three random spell scrolls)