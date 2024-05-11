#Fantastic Roles - Created by Rowan Thomas
#Version: 0.3

import random

#Variable Initialisation

numPlayers = None
#characterCreate = 0
main = True
characters = {}
startingStats = 10
totalAllStats = 10
global karthvileExplored
karthvileExplored = False


####### CHARACTER CREATION #######

def characterCreation(characters, numPlayers):
    characterCreate = 0
    while characterCreate < numPlayers:
        character = characterClass()
        character.name = input('\nPlayer ' + (str(characterCreate+1)) + "'s Name: ")
        character.homeland = homelandSelection()
        character.location = randomLocation()
        character.charClass = classSelection(character)
        creationSkills(character)
        item = creationItems(character)
        #character.inventory[item] = item
        #character.skills.append(skill)
        
        statIncrease(character, startingStats)
        characters[characterCreate+1] = character
        characterCreate+=1

def characterRegen(character):

    if character.HP < character.maxHP:
        hpRegen = character.HPR
        character.HP += character.HPR
        if character.HP > character.maxHP:
            character.HP = character.maxHP
            print(" [",hpRegen,"Health Regenerated. Health at Full ]")
        else:
            print(" [",hpRegen,"Health Regenerated ]")

    if character.MP < character.maxMP:
        mpRegen = character.MPR
        character.MP += character.MPR
        if character.MP > character.maxMP:
            character.MP = character.maxMP
            print(" [",mpRegen,"Magic Regenerated. Magic at Full ]")
        else:
            print(" [",mpRegen,"Magic Regenerated ]")

    if character.SP < character.maxSP:
        spRegen = character.SPR
        character.SP += character.SPR
        if character.SP > character.maxSP:
            spRegen = character.SP-character.maxSP
            character.SP = character.maxSP
            print(" [",spRegen,"Stamina Regenerated. Stamina at Full ]")
        else:
            print(" [",spRegen,"Stamina Regenerated ]")
    
    

def creationItems(character):
    if character.charClass == "Knight":
        character.weaponName = "1 Handed Sword and Shield"
        character.weaponType = "melee"
        character.AR = 10*character.vit
        character.weaponDamage = 10+character.meleeDam
    elif character.charClass == "Ranger":
        character.weaponName = "Bow and Arrows"
        character.weaponType = "ranged"
        character.weaponDamage = 10
    elif character.charClass == "Cleric":
        character.weaponName = "Magic Staff"
        character.weaponType = "magic"
        character.weaponDamage = 5
    elif character.charClass == "Crusader":
        character.weaponName = "Greatsword"
        character.weaponType = "melee"
        character.weaponDamage = 20
    elif character.charClass == "Rogue":
        character.weaponName = "Daggers"
        character.weaponType = "melee"
        character.weaponDamage = 5
    elif character.charClass == "Vigilant":
        character.weaponName = "Mace"
        character.weaponType = "melee"
        character.weaponDamage = 10
    elif character.charClass == "Samurai":
        character.weaponName = "Katana"
        character.weaponType = "melee"
        character.weaponDamage = 15
    elif character.charClass == "Ninja":
        character.weaponName = "Shuriken"
        character.weaponType = "ranged"
        character.weaponDamage = 5
    elif character.charClass == "Mystic":
        character.weaponName = "Grimoire"
        character.weaponType = "magic"
        character.weaponDamage = 5
    return

def creationSkills(character):
    if character.charClass == "Knight":
        character.skillOneID = "Riding" #Riding Skill
        character.skillOneCode = "RI"
        character.skillOneSPCost = 100
        character.skillOneLevel = 5
        character.skillOneEffect = 15 #20%chance to escape * level

    elif character.charClass == "Ranger":
        character.skillOneID = "Ranged Shot" #Ranged Shot Skill
        character.skillOneCode = "RS"
        character.skillOneSPCost = 50
        character.skillOneLevel = 5
        character.skillOneEffect = 10
        
    elif character.charClass == "Cleric":
        character.skillOneID = "Heal" #Heal Skill
        character.skillOneCode = "H"
        character.skillOneMPCost = 20
        character.skillOneLevel = 5
        character.skillOneEffect = 10 #10 heal x level
        
    elif character.charClass == "Crusader":
        character.skillOneID = "Self Heal" #Self Heal Skill
        character.skillOneCode = "SH"
        character.skillOneMPCost = 50
        character.skillOneLevel = 5
        character.skillOneEffect = 10
        
    elif character.charClass == "Rogue":
        character.skillOneID = "Steal" #Stealth Skill
        character.skillOneCode = "S"
        character.skillOneMPCost = 100
        character.skillOneLevel = 5
        character.skillOneEffect = 10
        
    elif character.charClass == "Vigilant":
        character.skillOneID = "Strengthen"
        character.skillOneCode = "STR"
        character.skillOneMPCost = 100
        character.skillOneLevel = 5
        character.skillOneEffect = 2 #will do 2*skill level buff on strength for combat
        
    elif character.charClass == "Samurai":
        character.skillOneID = "Flurry Strike"
        character.skillOneCode = "FS"
        character.skillOneSPCost = 25
        character.skillOneLevel = 5
        character.skillOneEffect = 5
        
    elif character.charClass == "Ninja":
        character.skillOneID = "Assassinate"
        character.skillOneCode = "ASN"
        character.skillOneSPCost = 50
        character.skillOneEffect = 20
        character.skillOneLevel = 5
        
    elif character.charClass == "Mystic":
        character.skillOneID = "Summon Elemental"
        character.skillOneCode = "SE"
        character.skillOneMPCost = 50
        character.skillOneEffect = 10
        character.skillOneEffect2 = 5
        character.skillOneLevel = 5
    return

def useSkillCombat(character, skillID, enemy):
    
    if character.skillOneCode == skillID or character.skillOneCode.lower() == skillID.lower() or skillID.lower() == character.skillOneID.lower():
        if skillID.lower() == "ri" or skillID.lower() == "riding":
            if character.SP >= character.skillOneSPCost:
                character.SP -= character.skillOneSPCost
                character.escape += character.skillOneEffect*character.skillOneLevel
                if character.escape > 100:
                    character.escape = 100
                print("You used",character.skillOneID,"skill, Escape chance increased to", character.escape)
            else:
                print("You don't have enough SP")
                return

        elif skillID.lower() == "rs" or skillID.lower() == "ranged shot":
            if character.SP >= character.skillOneSPCost:
                character.SP -= character.skillOneSPCost
                damage = (character.skillOneEffect*character.dex)*character.skillOneLevel
                enemy.HP -= damage
                print("You used",character.skillOneID,"skill. Hit", enemy.name,"for",damage,"damage")
            else:
                print("You don't have enough SP")
                return

        elif skillID.lower() == "h" or skillID.lower() == "heal":
            if character.MP >= character.skillOneMPCost:
                character.MP -= character.skillOneMPCost
                heal = (character.skillOneEffect*character.intel)*character.skillOneLevel
                character.HP += heal
                print("You used",character.skillOneID,"skill. Healed yourself for",heal,"health")
            else:
                print("You don't have enough MP")
                return

        elif skillID.lower() == "sh" or skillID.lower() == "self heal":
            if character.MP >= character.skillOneMPCost:
                character.MP -= character.skillOneMPCost
                heal = (character.skillOneEffect*character.intel)*character.skillOneLevel
                character.HP += heal
                if character.HP > character.maxHP:
                    character.HP = character.maxHP
                print("You used",character.skillOneID,"skill. Healed yourself for",heal,"health")
            else:
                print("You don't have enough MP")
                return

        elif skillID.lower() == "str" or skillID.lower() == "strengthen":
            if character.MP >= character.skillOneMPCost:
                character.MP -= character.skillOneMPCost
                buff = 2*character.skillOneLevel
                character.stren += buff
                print("You used",character.skillOneID,"skill. Increased your strengh by",buff,"until combat ends")
            else:
                print("You don't have enough MP")
                return

        elif skillID.lower() == "fs" or skillID.lower() == "flurry strike":
            if character.SP >= character.skillOneSPCost:
                character.SP -= character.skillOneSPCost
                damage = (character.skillOneEffect*character.dex)*character.skillOneLevel
                enemy.HP -= damage
                print("You used",character.skillOneID,"skill. Hit", enemy.name,"for",damage,"damage")
            else:
                print("You don't have enough SP")
                return

        elif skillID.lower() == "asn" or skillID.lower() == "assassinate":
            if character.SP >= character.skillOneSPCost:
                character.SP -= character.skillOneSPCost
                damage = (character.skillOneEffect*character.dex)+(character.luc*character.skillOneLevel)
                enemy.HP -= damage
                print("You used",character.skillOneID,"skill. Hit", enemy.name,"for",damage,"damage")
            else:
                print("You don't have enough MP")
                return

        elif skillID.lower() == "se" or skillID.lower() == "summon elemental":
            if character.MP >= character.skillOneMPCost:
                character.MP -= character.skillOneMPCost
                mode = input("Which Elemental do you wish to Summon? \n1) Fire Elemental - Damage Enemy\n2) Water Elemental - Heal Self")
                if mode == "1":
                    damage = (character.skillOneEffect*character.intel)*character.skillOneLevel
                    enemy.HP -= damage
                    print("You used",character.skillOneID,"(Fire) skill. Hit", enemy.name,"for",damage,"damage")
                elif mode == "2":
                    heal = (character.skillOneEffect2*character.intel)*character.skillOneLevel
                    character.HP += heal
                    if character.HP > character.maxHP:
                        character.HP = character.maxHP
                    print("You used",character.skillOneID,"(Water) skill. Healed yourself for",heal,"health")
            else:
                print("You don't have enough MP")
                playerAttack(character, enemy)
                return
    else:
        print("Not a valid skill")




    #elif character.skillTwoID == skillID:

    #elif character.skillThreeID == skillID:
        
        







def randomLocation():
    locationList = {1:"Lystral Village",
                    2:"Fort Hammerhold",
                    3:"Castle Seaview",
                    4:"Grimfield Village",
                    5:"Karthvile Cove",
                    6:"Wittleshin Cavern",
                    7:"Meadowbreeze Village",
                    8:"Shadowmist Mansion",
                    9:"Clearspring Village",
                    10:"Carabell Mining Town"
                    }
    selectedLocation = locationList[random.randint(1,10)]
    return selectedLocation

def classSelection(character):
    if character.homeland == 'Wryvenfell Kingdom':
        classList = {1:'Knight',
                    2:'Ranger',
                    3:'Cleric'
                    }
    elif character.homeland == 'Roswall Empire':
        classList = {1:'Crusader',
                    2:'Rogue',
                    3:'Vigilant'
                    }
    elif character.homeland == 'Sakura Dynasty':
        classList = {1:'Samurai',
                    2:'Ninja',
                    3:'Mystic'
                    }
    print("\nPlease select a class\n")
    for k in classList:
        print(str(k) + ") " + str(classList[k]))
    while True:
        charClass = int(input())
        try:
            return classList[charClass]
        except KeyError:
            print("Please enter a value from 1 - 3")

def homelandSelection():
    homelandList = {1:'Wryvenfell Kingdom',
                    2:'Roswall Empire',
                    3:'Sakura Dynasty'
                    }
    print("\nPlease select a homeland\n")
    for k in homelandList:
        print(str(k) + ") " + str(homelandList[k]))
    while True:
        try:
            homeland = int(input())
            try:
                return homelandList[homeland]
            except KeyError:
                print("Please enter a value from 1 - 3")
        except ValueError:
            print('\nPlease enter a valid number\n')
        

def statIncrease(character, statPoints):
    totalStatPoints = statPoints
    while totalStatPoints != 0:
        print("\nYou have",totalStatPoints,"stat points left")
        statIncreaseVar = input("\nWhich stat would you like to increase? \n1. Strength \n2. Dexterity \n3. Vitality \n4. Intelligence \n5. Wisdom \n6. Luck\n")
        if statIncreaseVar == "1":
            print("\nSTRENGTH")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Strength by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.stren = character.stren + increase
            totalStatPoints = totalStatPoints - increase
        elif statIncreaseVar == "2":
            print("DEXTERITY")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Dexterity by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.dex = character.dex + increase
            totalStatPoints = totalStatPoints - increase
        elif statIncreaseVar == "3":
            print("\nVITALITY")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Vitality by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.vit = character.vit + increase
            totalStatPoints = totalStatPoints - increase
        elif statIncreaseVar == "4":
            print("\nINTELLIGENCE")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Intelligence by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.intel = character.intel + increase
            totalStatPoints = totalStatPoints - increase
        elif statIncreaseVar == "5":
            print("\nWISDOM")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Wisdom by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.wis = character.wis + increase
            totalStatPoints = totalStatPoints - increase
        elif statIncreaseVar == "6":
            print("\nLUCK")
            print("\nYou have",totalStatPoints,"stat points left")
            increase = int(input("\nHow many points would you like to increase Luck by?: "))
            if increase > totalStatPoints:
                while increase > totalStatPoints:
                    print("Please enter a value equal to or less than",totalStatPoints)
                    increase = int(input("\n"))
            character.luc = character.luc + increase
            totalStatPoints = totalStatPoints - increase
        else:
            print("Please enter a value from 1 to 6")
    character.statPoints = 0

    character.HP = 90+10*character.vit
    character.maxHP = 90+10*character.vit
    character.HPR = 5*character.vit
    
    character.SP = 90+10*character.stren
    character.maxSP = 90+10*character.stren
    character.SPR = 5*character.dex
    
    character.MP = 90+10*character.intel
    character.maxMP = 90+10*character.intel
    character.MPR = 5*character.wis
    
    character.meleeDam = 10*character.stren
    character.magicDam = 10*character.intel
    character.rangedDam = 10*character.dex
    if character.dex >= 5:
        character.attackSpeed = 2
    if character.dex >= 10:
        character.attackSpeed = 3
    if character.dex >= 15:
        character.attackSpeed = 4
    if character.dex >= 25:
        character.attackSpeed = 5
    if character.dex >= 35:
        character.attackSpeed = 6
    character.stealthAction = 5*character.dex
    character.evasion = 5*character.dex
    character.negEffectRecovery = 5*character.vit
    character.problemSolving = 5*character.intel
    character.wiseChoice = 5*character.wis
    character.escape = 5*character.dex
    character.defaultEscape = 5*character.dex
    character.defaultStren = character.stren

####### END CHARACTER CREATION #######

####### MAP CONTROL #######

def commandTravel(character):
    if character.location == "Lystral Village":
        travelOptions = {1: "Shadowmist Mansion", 2: "Carabell Mining Town"}
    elif character.location == "Shadowmist Mansion":
        travelOptions = {1: "Lystral Village", 2: "Fort Hammerhold"}
    elif character.location == "Carabell Mining Town":
        travelOptions = {1: "Lystral Village", 2: "Karthvile Cove"}
    elif character.location == "Karthvile Cove":
        travelOptions = {1: "Carabell Mining Town", 2: "Wittleshin Cavern"}
    elif character.location == "Wittleshin Cavern":
        travelOptions = {1: "Karthvile Cove", 2: "Fort Hammerhold", 3: "Grimfield Village"}
    elif character.location == "Fort Hammerhold":
        travelOptions = {1: "Shadowmist Mansion", 2: "Meadowbreeze Village", 3: "Clearspring Village", 4: "Wittleshin Cavern"}
    elif character.location == "Clearspring Village":
        travelOptions = {1: "Fort Hammerhold", 2: "Castle Seaview"}
    elif character.location == "Meadowbreeze Village":
        travelOptions = {1: "Fort Hammerhold"}
    elif character.location == "Castle Seaview":
        travelOptions = {1: "Clearspring Village"}
    elif character.location == "Grimfield Village":
        travelOptions = {1: "Wittleshin Cavern"}          
    print("You are in",character.location)
    print("Please select a destination\n")
    for k in travelOptions:
        print(str(k) + ") " + str(travelOptions[k]))
    while True:
        try:
            travelTo = int(input())
            try:
                return travelOptions[travelTo]
            except KeyError:
                print("\nPlease enter a number corresponding to a destination")
        except ValueError:
            print('\nPlease enter a valid number\n')        


def commandLocation(character):
    print("\nYou are in",character.location)
    if character.location == "Lystral Village":
        print("The people of this village will reward you if you work as a farmhand\n[Reward: 50g, 25EXP]")
        yn = input("Do you wish to work in " + character.location + "?: ")
        if yn == "y" or yn == "yes":
            if character.worked == True:
                print("You have already worked all day")
                return
            else:
                print("\nYou work as a farmhand for the day, and earn 50 gold in wages")
                character.wealth += 50
                character.EXP += 25
                character.worked = True

    elif character.location == "Shadowmist Mansion":
        print("This mansion is for sale, and owning it and the surrounding grounds would set you up for life (Victory Condition)\n[Cost: 20'000 gold]")
        yn = input("Do you wish to purchase " + character.location + "?: ")
        if yn == "y" or yn == "yes":
            if character.wealth >= 20000:
                print("You purchase Shadowmist Mansion and its surrounding grounds")
                print("\n//////////////////////////////////////////////////////////////")
                print("\nCongratulations!", character.name,"is the winner!")
                print("\n//////////////////////////////////////////////////////////////")
                return
            else:
                print("\nYou don't have enough wealth to buy Shadowmist Mansion")

    elif character.location == "Carabell Mining Town":
        print("The people of this town will reward you if you work as a miner\n[Reward: 100g, 50EXP]")
        yn = input("Do you wish to work in " + character.location + "?: ")
        if yn == "y" or yn == "yes":
            if character.worked == True:
                print("You have already worked all day")
                return
            else:
                print("\nYou work as a miner for the day, and earn 100 gold in wages")
                character.wealth += 100
                character.EXP += 50
                character.worked = True
       

    elif character.location == "Karthvile Cove":
        print("You decide to venture further into the cove that the town is named after")
        if karthvileExplored == False:
            karthvileExplored = True
            print("As you explore the cove, you lose track of time and darkness starts to set in. As you try to stumble your way back to town\
                    you come across a fallen tree. Deciding to rest for a moment, you are surprised to find a treasure chest\
                    inside the hollowed out stump. Upon opening it, you find 1000 gold.")
            character.wealth+=1000
        else:
            print("You find nothing of value")

    #elif character.location == "Wittleshin Cavern":
        

    elif character.location == "Fort Hammerhold":
        print("Fort Hammerhold's inn is open for business. You can stay there to restore Health, Stamina and Magic")
        yn = input("Stay at the Hammerhold Inn? [Cost: 25 gold] (y/n): ")
        if character.worked == False:
            if yn.lower() == "y" or yn.lower() == "yes":
                if character.wealth >= 25:
                    print("You feel refreshed")
                    character.wealth -= 25
                    character.HP = character.maxHP
                    character.SP = character.maxSP
                    character.MP = character.maxMP
                else:
                    print("You don't have enough gold")
        else:
            print("You have already stayed at the inn")
             

    #elif character.location == "Clearspring Village":
        

    #elif character.location == "Meadowbreeze Village":
        

    #elif character.location == "Castle Seaview":
        

    #elif character.location == "Grimfield Village":
             

####### END MAP CONTROL #######

####### ENEMY FUNCTIONS #######

def generateEnemy():
    
    enemyList = {1: "Orc", 2: "Goblin", 3: "Dragon", 4: "Skeleton",
                 5: "Slime", 6: "Giant Spider", 7: "Wolf", 8:"Tree Ent",
                 9: "Troll", 10: "Giant Rat", 11: "Giant Toad", 12: "Bandit"}
    
    encounter = random.randint(1,2)
    if encounter == 2:
        enemy = enemyClass()
        randomEnemy = enemyList[random.randint(1,len(enemyList))]
        if randomEnemy == "Orc":
            enemy.name = randomEnemy
            enemy.HP = 200
            enemy.ATT = 20
            enemy.EXP = 100
            enemy.loot = 50
        elif randomEnemy == "Goblin":
            enemy.name = randomEnemy
            enemy.HP = 100
            enemy.ATT = 10
            enemy.EXP = 50
            enemy.loot = 25
        elif randomEnemy == "Dragon":
            enemy.name = randomEnemy
            enemy.HP = 2000
            enemy.ATT = 200
            enemy.EXP = 1000
            enemy.loot = 1500
        elif randomEnemy == "Skeleton":
            enemy.name = randomEnemy
            enemy.HP = 150
            enemy.ATT = 15
            enemy.EXP = 50
            enemy.loot = 75
        elif randomEnemy == "Slime":
            enemy.name = randomEnemy
            enemy.HP = 10
            enemy.ATT = 5
            enemy.EXP = 25
            enemy.loot = 20
        elif randomEnemy == "Giant Spider":
            enemy.name = randomEnemy
            enemy.HP = 200
            enemy.ATT = 50
            enemy.EXP = 100
            enemy.loot = 80
        elif randomEnemy == "Wolf":
            enemy.name = randomEnemy
            enemy.HP = 40
            enemy.ATT = 60
            enemy.EXP = 75
            enemy.loot = 50
        elif randomEnemy == "Tree Ent":
            enemy.name = randomEnemy
            enemy.HP = 500
            enemy.ATT = 20
            enemy.EXP = 200
            enemy.loot = 250
        elif randomEnemy == "Troll":
            enemy.name = randomEnemy
            enemy.HP = 250
            enemy.ATT = 80
            enemy.EXP = 200
            enemy.loot = 250
        elif randomEnemy == "Giant Rat":
            enemy.name = randomEnemy
            enemy.HP = 15
            enemy.ATT = 10
            enemy.EXP = 25
            enemy.loot = 30
        elif randomEnemy == "Giant Toad":
            enemy.name = randomEnemy
            enemy.HP = 35
            enemy.ATT = 20
            enemy.EXP = 50
            enemy.loot = 35
        elif randomEnemy == "Bandit":
            enemy.name = randomEnemy
            enemy.HP = 200
            enemy.ATT = 45
            enemy.EXP = 200
            enemy.loot = 100
        return enemy
    else:
        return "safe"

def combat(character, enemy):
    character
    print("You encounter an enemy! A", enemy.name,"appears!")
    while enemy.HP > 0:
        if character.isDead == True:
            print("You fell in battle against a",enemy.name)
            return
        #USE SKILL IN COMBAT
        decision = input("\nDo you wish to attack, flee, use a skill, or use an item?\n")
        if decision.lower() == "skill" or decision.lower() == "skills":
            print("you have the following skills:\n")
            if character.skillOneID != None:
                  print(character.skillOneID, "(",character.skillOneCode, ")")
            if character.skillTwoID != None:
                  print(character.skillTwoID, "(",character.skillTwoCode, ")")
            if character.skillThreeID != None:
                  print(character.skillThreeID, "(",character.skillThreeCode, ")")
            skillID = input("\nWhat skill would you like to use?\n")
            useSkillCombat(character, skillID, enemy)

        #USE ITEM IN COMBAT  
        elif decision.lower() == "item":
            print("What item would you like to use?")
            if character.healthPotions > 0:
                print("Health Potion (HPOT)")
            if character.magicPotions > 0:
                print("Magic Potion (MPOT)")
            if character.staminaPotions > 0:
                print("Stamina Potion (SPOT)")
            if character.invisPotions > 0:
                print("Invisibility Potion (IPOT)\n")
            item = input()
            if item.lower() == "hpot":
                if character.healthPotions > 0:
                    print("Health Potion used. 100 health restored.")
                    character.healthPotions -= 1
                    character.HP += 100
                    if character.HP+100 > character.maxHP:
                        character.HP = character.maxHP
                else:
                    print("You don't have any health potions")
            elif item.lower() == "mpot":
                if character.magicPotions > 0:
                    character.magicPotions -= 1
                    print("Magic Potion used. 100 magic restored.")
                    character.MP += 100
                    if character.MP+100 > character.maxMP:
                        character.MP = character.maxMP
                else:
                    print("You don't have any magic potions")
            elif item.lower() == "spot":
                if character.staminaPotions > 0:
                    character.staminaPotions -= 1
                    print("Stamina Potion used. 100 stamina restored.")
                    character.SP += 100
                    if character.SP > character.maxSP:
                        character.SP = character.maxSP
                else:
                    print("You don't have any stamina potions")
            elif item.lower() == "ipot":
                if  character.invisPotions > 0:
                    print(character.escape)
                    print("Invisibility Potion used. Escape chance increased by 50%.")
                    character.invisPotions -= 1
                    character.escape += 50
                    if character.escape > 90:
                        character.escape = 90
                else:
                    print("You don't have any invisibility potions")


        #FLEE FROM COMBAT
        elif decision.lower() == "flee":
            attempt = random.randint(1,100)
            if character.escape >= attempt:
                print("You successfully escaped to previous location")
                character.escape = character.defaultEscape
                return
            else:
                print("\nFailed to escape")
                enemyAttack(character, enemy)
                playerAttack(character, enemy)
        #NORMAL COMBAT
        elif decision.lower() =="attack" or decision.lower() == "1":
            playerAttack(character, enemy)
            enemyAttack(character, enemy)


    modifier = random.randint(-10,20)
    loot = enemy.loot + modifier
    XP = enemy.EXP
    print("###########################")
    print()
    print(enemy.name, "was defeated!")
    print("You found", loot, "Gold!")
    print("You gained",XP,"Experience!")
    print()
    print("###########################")
    character.wealth += loot
    character.EXP += XP
    character.escape = character.defaultEscape
    character.stren = character.defaultStren
    
    return

def playerAttack(character, enemy):
    melee = character.meleeDam
    magic = character.magicDam
    speed = character.attackSpeed
    #attackType = input("1) Normal attack \n2) Use Skill\n")
    #if attackType.lower() == "1" or attackType.lower() == "normal":
    if character.weaponType == "melee":
        damage = character.weaponDamage+character.meleeDam
        print("You hit", enemy.name, speed, "times for", damage*(speed), "damage")
    if character.weaponType == "ranged":
        damage = character.weaponDamage+character.rangedDam
        print("You hit", enemy.name, speed, "times for", damage*(speed), "damage")
    if character.weaponType == "magic":
        damage = character.weaponDamage+character.magicDam
        print("You hit", enemy.name, speed, "times for", damage*(speed), "damage")
    enemy.HP -= damage*speed
    return
    
   # elif attackType.lower() == "2" or attackType.lower() == "skill":
        
            
    
def enemyAttack(character, enemy):
    if enemy.HP > 0:
        enemyDamage = enemy.ATT
        evadeAttempt = random.randint(1,100)
        if character.evasion > 80:
            evasion = 80
            if evasion >= evadeAttempt:
                print()
                print(enemy.name, "attacks, but you evade the hit")
            elif evasion+5 >= evadeAttempt:
                print()
                print(enemy.name, "attacks. It's a glancing blow. Damage is halved.")
                enemyDamage = enemyDamage/2
        print()
        print(enemy.name, "hits you for", enemyDamage, "damage\n")
        if character.AR > 0:
            damage = enemyDamage - character.AR*character.vit
            if damage < 0:
                print("All damage was negated by your armour")
                damage = 0
            else:
                print(character.AR*character.vit,"was negated by your armour")
                print("Hit for", damage, "damage")
            character.HP -= damage
        else:
            character.HP -= enemyDamage
        if character.HP <= 0:
            character.isDead = True
            return
        print("You have",character.HP,"HP left")
        

def listener(event, character):
    if event.lower() == "status":
        commandStatus(character)
    elif event.lower() == "skills":
        commandSkills(character)
    elif event.lower() == "inventory":
        commandInventory(character)
    elif event.lower() == "level up":
        commandLevel(character)
    elif event.lower() == "shop":
        commandShop(character)
    elif event.lower() == "travel":
        destination = commandTravel(character)
        interruption = generateEnemy()
        if interruption != "safe":
            if interruption.name != "Dragon":
                combat(character, interruption)
            elif interruption.name == "Dragon" and character.level >= 10:
                combat(character, interruption)
            else:
                character.location = destination
                print("You arrived at",destination,"safely")
                character.locationStolen = False
                listener("end turn", character)
            character.location = destination
            character.locationStolen = False
        else:
            character.location = destination
            print("You arrived at",destination,"safely")
            character.locationStolen = False
            listener("end turn", character)
    elif event.lower() == "item":
        commandUseItem(character)
    elif event.lower() == "steal":
        commandSteal(character)
    elif event.lower() == "location":
        commandLocation(character)

def commandSteal(character):
    if character.skillOneID == "Steal" or character.skillTwoID == "Steal" or character.skillThreeID == "Steal":
        print("Are you sure you want to steal from", character.location, "(y/n)")
        yn = input()
        if yn == "n":
            print("You don't steal anything")
            return
        elif yn == "y":
            if character.locationStolen == True:
                print("You have already robbed this location, better not risk it again for a while.")
            else:
                stolenWealth = (10*character.dex)
                stolenWealth += random.randint(-25, 75)
                character.wealth += stolenWealth
                print("You stole", stolenWealth,"gold")
                character.locationStolen = True
    else:
        print("You do not have the steal skill")
        
def commandUseItem(character):
    print("What item would you like to use?")
    if character.healthPotions > 0:
        print("Health Potion (HPOT)")
    if character.magicPotions > 0:
        print("Magic Potion (MPOT)")
    if character.staminaPotions > 0:
        print("Stamina Potion (SPOT)")
    item = input()
    if item.lower() == "hpot":
        if character.healthPotions > 0:
            print("Health Potion used. 100 health restored.")
            character.healthPotions -= 1
            character.HP += 100
            if character.HP > character.maxHP:
                character.HP = character.maxHP
        else:
            print("You don't have any health potions")
    elif item.lower() == "mpot":
        if character.magicPotions > 0:
            character.magicPotions -= 1
            print("Magic Potion used. 100 magic restored.")
            character.MP += 100
            if character.MP > character.maxMP:
                character.MP = character.maxMP
        else:
            print("You don't have any magic potions")

    elif item.lower() == "spot":
        if character.staminaPotions > 0:
            character.staminaPotions -= 1
            print("Stamina Potion used. 100 stamina restored.")
            character.SP += 100
            if character.SP > character.maxSP:
                character.SP = character.maxSP
        else:
            print("You don't have any stamina potions")

def commandLevel(character):
    if character.EXP >= 200:
        confirm = input("Would you like to spend 200EXP to level up? (y/n): ")
        if confirm.lower() == "y":
            character.EXP = character.EXP - 200
            character.statPoints = character.statPoints + 3
            character.level += 1
            character.HP = character.maxHP
            character.MP = character.maxMP
            print("Leveled up! You are now Level", characters[char].level)
    else:
        print("You don't have enough EXP")
    return

def commandStatus(character):
    print(character.name,"of the",character.homeland,"( Level",character.level, character.charClass,")")
    print("   Health Points: ", character.HP)
    print("   Magic Points:  ", character.MP)
    print("   Stamina Points:", character.SP)
    print()
    print("   Armour Rating:", character.AR)
    print("   Defence Rating:",character.AR*character.vit)
    print()
    print("   Current EXP:",character.EXP)
    print("   Unspent Stat Points: ", character.statPoints)
    print("   Str:",character.stren)
    print("   Dex:",character.dex)
    print("   Vit:",character.vit)
    print("   Int:",character.intel)
    print("   Wis:",character.wis)
    print("   Luc:",character.luc)
    print()
    print("   Location:", character.location)
    print("escape:",character.escape)

    if character.statPoints != 0:
        print()
        if input("You have unspent stat points, would you like to allocate them now? (y/n)").lower() == "y":
            statIncrease(character, character.statPoints)

def commandInventory(character):
    print("---- Wealth ----")
    print("",character.wealth,"gold")
    print()
    print("---- Potions ----")
    if character.healthPotions > 0:
        print(" Health Potions:",character.healthPotions)
    if character.magicPotions > 0:
        print(" Magic Potions:",character.magicPotions)
    if character.staminaPotions > 0:
        print(" Stamina Potions:",character.staminaPotions)
    if character.staminaPotions > 0:
        print(" Invisibility Potions:",character.invisPotions)
    print()
    print("---- Weapon ----")
    print("",character.weaponName)
    if character.weaponType == "melee":
        print(" Damage: ",character.weaponDamage+character.meleeDam)
    if character.weaponType == "ranged":
        print(" Damage: ",character.weaponDamage+character.rangedDam)
    if character.weaponType == "magic":
        print(" Damage: ",character.weaponDamage+character.magicDam)
            

def commandSkills(character):
    print(character.skillOneID)
    #for skill in character.skills:
        #print("Skill name:",skill.name)
        #print("Skill level:",skill.level)

def commandShop(character):
    item = None
    while item != "exit":
        print("\nWhat would you like to buy?")
        shopInventory = {1:"Health Potion {50g}", 2:"Magic Potion {50g}", 3: "Stamina Potion {50g}", 4:"Invisibility Potion {100g}"}
        for i in shopInventory:
            print(str(i) + ") " + str(shopInventory[i]))
        print("type 'exit' to exit shop")
        item = input()
        if item != "exit":
            try:
                item = int(item)
                if item == 1:
                    quantity = int(input("\nHow many Health Potions do you wish to purchase?: "))
                    cost = quantity*50
                    if character.wealth >= cost:
                        print("You purchased",quantity,"health potions for",cost,"gold")
                        character.wealth -= cost
                        character.healthPotions += quantity
                    else:
                        print("You don't have enough gold")
                elif item == 2:
                    quantity = int(input("\nHow many Magic Potions do you wish to purchase?: "))
                    cost = quantity*50
                    if character.wealth >= cost:
                        print("You purchased",quantity,"magic potions for",cost,"gold")
                        character.wealth -= cost
                        character.magicPotions += quantity
                    else:
                        print("You don't have enough gold")
                elif item == 3:
                    quantity = int(input("\nHow many Stamina Potions do you wish to purchase?: "))
                    cost = quantity*50
                    if character.wealth >= cost:
                        print("You purchased",quantity,"stamina potions for",cost,"gold")
                        character.wealth -= cost
                        character.staminaPotions += quantity
                    else:
                        print("You don't have enough gold")
                elif item == 4:
                    quantity = int(input("\nHow many Invisibility Potions do you wish to purchase?: "))
                    cost = quantity*100
                    if character.wealth >= cost:
                        print("You purchased",quantity,"invisibility potions for",cost,"gold")
                        character.wealth -= cost
                        character.invisPotions += quantity
                    else:
                        print("You don't have enough gold")
            except ValueError:
                print("\nPlease enter a valid number")
    return



class characterClass:
    EXP = 0
    level = 1
    
    name = None
    homeland = None
    charClass = None
    statPoints = 0
    stren = 1
    dex = 1
    vit = 1
    intel = 1
    wis = 1
    luc = 1

    HP = 10*vit
    maxHP = 10*vit
    SP = 10*stren
    SPR = 5*dex
    MP = 10*intel
    maxMP = 10*intel
    MPR = 5*wis
    AR = 0
    
    meleeDam = 10*stren
    magicDam = 10*intel
    rangedDam = 10*dex
    attackSpeed = 1
    
    stealthAction = 5*dex
    evasion = 5*dex
    
    negEffectRecovery = 5*vit
    problemSolving = 5*intel
    wiseChoice = 5*wis
    escape = 5*dex
    defaultEscape = 5*dex
    defaultStren = stren

    location = None
    locationStolen = False
    inParty = False
    worked = False
    
    wealth = 100

    # INVENTORY SECTION 
    healthPotions = 0
    magicPotions = 0
    staminaPotions = 0
    invisPotions = 0
    

    weaponName = None
    weaponType = None
    weaponDamage = None
    weaponArmour = None

    #SKILL ONE
    skillOneID = None
    skillOneCode = None
    skillOneEffect = None
    skillOneEffect2 = None
    skillOneMPCost = None
    skillOneSPCost = None
    skillOneLevel = None

    #SKILL TWO
    skillTwoID = None
    skillTwoCode = None
    skillTwoEffect = None
    skillTwoEffect2 = None
    skillTwoMPCost = None
    skillTwoSPCost = None
    skillTwoLevel = None

    #SKILL THREE
    skillThreeID = None
    skillThreeCode = None
    skillThreeEffect = None
    skillThreeEffect2 = None
    skillThreeMPCost = None
    skillThreeSPCost = None
    skillThreeLevel = None
                            
    isDead = False
    


    
class enemyClass():
    name = None
    HP = None
    ATT = None
    EXP = None
    loot = None
    
#########################
#BEGIN MAIN GAME PROCESS#
#########################

while numPlayers == None:
    try:
        numPlayers = int(input('How many players?: '))
    except ValueError:
        print('\nPlease enter a valid number\n')
        numPlayers = None

characterCreation(characters, numPlayers)

print("\n---- THE ADVENTURE BEGINS ----")

while main:

    for char in characters:
        character = characters[char]
        if character.isDead == False:
            print()
            print("<<<<", character.name.upper(),">>>>")
            print(character.name, "it is your turn, you are in", character.location,"\n")
            command = input("Command >>> " )
            print()
            while command != "end turn":
                listener(command, character)
                if command == "travel":
                    print()
                    print(character.name,"arrives in",character.location,"and ends their turn")
                    break
                command = input("Command >>> " )
            characterRegen(character)
            character.worked = False

                




              
              
