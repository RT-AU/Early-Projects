# Name:  Rowan Thomas
# Import the necessary modules.
import random

#Variable Initialisation
numCharacters = None
mainLoop = True
daytime = True
characters = []
actedCharacters = []
characterInputLoop = 0

#########################
#Define Action Functions#
#########################

#Defines the function dayAction which randomly selects from a dictionary
#of actions and returns it
def dayAction():
    d_actions1 = {1:'picks up a knife and fatally wounds ' + characters[1],#death
                 2:'teams up with ' + characters[1] + ' for the day',
                 3:'finds a cave to wait out the day',
                 4:'finds a canteen full of water',
                 5:'and ' + characters[1] + ' team up and steal supplies from ' + characters[2],
                 6:'hunts around the tower for resources',
                 7:'finds a backback full of camping equipment',
                 8:'receives medical supplies from an unknown sponsor',
                 9:'camouflages themself in some bushes',
                 10:'receives an explosive from an unknown sponsor',
                 11:'receives food from an unknown sponsor',
                 12:'travels to higher ground',
                 13:'discovers a river',
                 14:'constructs a shack',
                 15:'sets an explosive off, killing ' + characters[1] + ', ' + characters[2] + ' and ' + characters[3],#death
                 16:'sets ' + characters[1] +"'s shelter on fire while they were out",
                 17:'falls into a pit and dies', #death
                 18:'sees smoke in the distance, but decides not to investigate',
                 19:'and ' + characters[1] + ' team up and ambush ' + characters[2] + ' and ' + characters[3], #death
                  20:"finds an abandoned car, but can't find the keys",
                  21:"finds a crashed helicopter and decides to search for supplies. \nAfter an hour, they find nothing.",
                  22:"finds a crashed helicopter and decides to search for supplies. \nAfter an hour, they find a gun.",
                  23:"pulls a gun on " + characters[1] + ' but misses and shoots ' + characters[2] + ' instead', #death
                  24:'pulls a gun on ' + characters[1] + ' and kills them', #death
                  25:'sees ' + characters[1] + ' but decides to stay hidden',
                  26:'questions their sanity',
                  27:'finds a log cabin, and decides to fortify it for the day',
                  28:'forages for food',
                  29:'finds a river and goes fishing',
                  30:'teams up with ' + characters[1] + ' to hunt for other survivors',
                  31:'steps on a landmine and dies',
                  32:'finds a friendly dog, who accompanies them for the day',
                  33:'runs across a crumbling railway station. \nA haunting whistle scares them off',
                  34:'sees a helicopter drop a supply crate, and heads towards it; \nHowever, ' + characters[1] + ' was waiting in ambush, and kills them', #death
                  35:'sees a helicopter drop a supply crate, and heads towards it; \nThere is no one else around, and the crate contains ample supplies of food \nand warm clothing'
                 }
    
    d_completedAction1 = d_actions1[random.randint(1,len(d_actions1))] #Randomly selects an action from the d_actions1 dictionary

#This section is invoked when a "death" action is called.
    #first it checks if the action called is a "death" action
    #second it checks if the character(s) to die is in the actedCharacters list
    #finally it kills the character(s) by removing it from the characters list
    if d_completedAction1 == d_actions1[1]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])
        
    if d_completedAction1 == d_actions1[15]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        if characters[2] in actedCharacters:
            actedCharacters.remove(characters[2])
        if characters[3] in actedCharacters:
            actedCharacters.remove(characters[3])
        characters.remove(characters[1])
        characters.remove(characters[1])
        characters.remove(characters[1])

    if d_completedAction1 == d_actions1[17]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    if d_completedAction1 == d_actions1[19]:
        if characters[2] in actedCharacters:
            actedCharacters.remove(characters[2])
        if characters[3] in actedCharacters:
            actedCharacters.remove(characters[3])
        characters.remove(characters[2])
        characters.remove(characters[2])

    if d_completedAction1 == d_actions1[23]:
        if characters[2] in actedCharacters:
            actedCharacters.remove(characters[2])
        characters.remove(characters[2])

    if d_completedAction1 == d_actions1[24]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    if d_completedAction1 == d_actions1[31]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    if d_completedAction1 == d_actions1[34]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])


    return d_completedAction1

#See above descriptions on action functions

def dayAction3Left():
    d_actions2 = {1:'picks up a knife and fatally wounds ' + characters[1],#death
                 2:'teams up with ' + characters[1] + ' for the day',
                 3:'finds a cave to wait out the day',
                 4:'finds a canteen full of water',
                 5:'and ' + characters[1] + ' team up and steal supplies from ' + characters[2],
                 6:'hunts around the tower for resources',
                 7:'finds a backback full of camping equipment',
                 8:'receives medical supplies from an unknown sponsor',
                 9:'camouflages themself in some bushes',
                 10:'receives an explosive from an unknown sponsor',
                 11:'receives food from an unknown sponsor',
                 12:'travels to higher ground',
                 13:'discovers a river',
                 14:'constructs a shack',
                 15:'sets an explosive off, killing ' + characters[1] + ' and ' + characters[2], #death
                 16:'sets ' + characters[1] +"'s shelter on fire while they were out",
                 17:'falls into a pit and dies', #death
                 18:'sees smoke in the distance, but decides not to investigate',
                 19:'and ' + characters[1] + ' team up and ambush ' + characters[2], #death
                 }
                 
    d_completedAction2 = d_actions2[random.randint(1,len(d_actions2))]

    if d_completedAction2 == d_actions2[1]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

        
    if d_completedAction2 == d_actions2[15]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        if characters[2] in actedCharacters:
            actedCharacters.remove(characters[2])
        characters.remove(characters[1])
        characters.remove(characters[1])

    if d_completedAction2 == d_actions2[17]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    if d_completedAction2 == d_actions2[19]:
        if characters[2] in actedCharacters:
            actedCharacters.remove(characters[2])
        characters.remove(characters[2])



    return d_completedAction2

#See above descriptions on action functions

def dayAction2Left():
    d_actions3 = {1:'picks up a knife and fatally wounds ' + characters[1],#death
                 2:'sees ' + characters[1] + ' from a distance, but runs away',
                 3:'finds a cave to wait out the day',
                 4:'finds a canteen full of water',
                 5:'steals supplies from ' + characters[1],
                 6:'hunts around the tower for resources',
                 7:'finds a backback full of camping equipment',
                 8:'receives medical supplies from an unknown sponsor',
                 9:'camouflages themself in some bushes',
                 10:'receives an explosive from an unknown sponsor',
                 11:'receives food from an unknown sponsor',
                 12:'travels to higher ground',
                 13:'discovers a river',
                 14:'constructs a shack',
                 15:'sets an explosive off which kills ' + characters[1],#death
                 }
                 
    d_completedAction3 = d_actions3[random.randint(1,len(d_actions3))]

    if d_completedAction3 == d_actions3[1]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])
        
    if d_completedAction3 == d_actions3[15]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    return d_completedAction3

#See above descriptions on action functions

def nightAction():
    n_actions1 = {1:'huddles by a fire for warmth',
                 2:'climbs up a tree and sleeps in its branches',
                 3:'finds a cave to wait out the night',
                 4:'cries themself to sleep',
                 5:'stays awake all night',
                 6:'and ' + characters[1] + ' run into each other and decide to truce for the night',
                 7:'and ' + characters[1] + ' sleep in shifts',
                 8:'clubs ' + characters[1] + ' with a tree branch.', #death
                 9:'falls out of a tree and lands on ' + characters[1] + ', killing them both',
                  10:'hears snoring in the night, and follows it to find ' + characters[1] + ' \nbut leaves them alone',
                  11:'hears snoring in the night, and follows it to find ' + characters[1] + ' \nand kills them in their sleep', #death
                  12:'stares at the stars longingly',
                  13:'stumbles across a cave filled with toxic gas and dies', #death
                  14:'sleeps like a log',
                  15:'hears movement behind them, but it turns out to be a wild cat',
                  16:'hears movement behind them, which turns out to be a wild boar that chases them all night',
                  17:'tries to sneak up on ' + characters[1] + ' but is found, and killed instead', #death
                  18:"stumbles about in the dark and falls of a cliff", #death
                  19:'dreams of safety',
                  20:'finds a hot spring',
                  21:'finds night vision goggles, and uses them to steal supplies from ' + characters[1],
                 }
                 
    n_completedAction1 = n_actions1[random.randint(1,len(n_actions1))]

    if n_completedAction1 == n_actions1[8]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    if n_completedAction1 == n_actions1[9]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[0])
        characters.remove(characters[0])

    if n_completedAction1 == n_actions1[11]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    if n_completedAction1 == n_actions1[13]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    if n_completedAction1 == n_actions1[17]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    if n_completedAction1 == n_actions1[18]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        characters.remove(characters[0])

    return n_completedAction1

#See above descriptions on action functions

def nightAction3Left():
    n_actions2 = {1:'huddles by a fire for warmth',
                 2:'climbs up a tree and sleeps in its branches',
                 3:'finds a cave to wait out the night',
                 4:'cries themself to sleep',
                 5:'stays awake all night',
                 6:'and ' + characters[1] + ' run into each other and decide to truce for the night',
                 7:'and ' + characters[1] + ' sleep in shifts',
                 8:'clubs ' + characters[1] + ' with a tree branch.', #death
                 9:'falls out of a tree and lands on ' + characters[1] + ', killing them both',
                 }
                 
    n_completedAction2 = n_actions2[random.randint(1,8)]

    if n_completedAction2 == n_actions2[8]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    return n_completedAction2

def nightAction2Left():
    n_actions3 = {1:'huddles by a fire for warmth',
                 2:'climbs up a tree and sleeps in its branches',
                 3:'finds a cave to wait out the night',
                 4:'cries themself to sleep',
                 5:'stays awake all night',
                 6:'and ' + characters[1] + ' run into each other and decide to truce for the night',
                 7:'and ' + characters[1] + ' sleep in shifts',
                 8:'clubs ' + characters[1] + ' with a tree branch.' #death
                 }
                 
    n_completedAction3 = n_actions[random.randint(1,8)]

    if n_completedAction == n_actions3[8]:
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[1])

    if n_completedAction2 == n_actions2[9]:
        if characters[0] in actedCharacters:
            actedCharacters.remove(characters[0])
        if characters[1] in actedCharacters:
            actedCharacters.remove(characters[1])
        characters.remove(characters[0])
        characters.remove(characters[0])


    return n_completedAction3

#########################
#BEGIN MAIN GAME PROCESS#
#########################

while numCharacters == None:
    try:
        numCharacters = int(input('How many survivors?: '))
    except ValueError:
        print('\nPlease enter a valid number\n')
        numCharacters = None


print('Enter the names of the survivors: ')

while characterInputLoop < numCharacters:
    characterInput = input('Name of character ' + (str(characterInputLoop+1)) + ': ')
    characters.append(characterInput)
    characterInputLoop += 1

print('The game begins in a dark Forest \n There is a tall building in the centre, covered in creepvines. \n With a loud gunshot, the game begins...\n')



while mainLoop == True:
    #daytime section
    if daytime == True:
        random.shuffle(characters) # Shuffles the characters to change Order of Play
        if len(characters) == 1:
            print('-'*20)
            print('| CONGRATULATIONS! |')
            print('-'*20)
            input()
            print(characters[0], 'is the winner!')
            input()
            print('-'*13)
            print('| GAME OVER |')
            print('-'*13)
            input()
            break
            
        if len(actedCharacters) != len(characters): #checks to ensure that the day only loops once through each character
            if not characters[0] in actedCharacters:#checks to make sure that character has not already been used
                actedCharacters.append(characters[0])
                try:
                    print(characters[0], dayAction())
                    input()
                except IndexError:
                    try:
                        print(characters[0], dayAction3Left())
                        input()
                    except IndexError:
                        print(characters[0], dayAction2Left())
                        input()

            else:
                random.shuffle(characters)
        else:
            print('-'*15)
            print('| Night falls |')
            print('-'*15)
            input()
            actedCharacters = []
            daytime = False
    #night time section
    else:
        random.shuffle(characters) # Shuffles the characters to change Order of Play
        if len(characters) == 1:
            print('-'*20)
            print('| CONGRATULATIONS! |')
            print('-'*20)
            input()
            print(characters[0], 'is the winner!')
            input()
            print('-'*13)
            print('| GAME OVER |')
            print('-'*13)
            input()
            break
            
        if len(actedCharacters) != len(characters): #checks to ensure that the night only loops once through each character
            if not characters[0] in actedCharacters:#checks to make sure that character has not already been used
                actedCharacters.append(characters[0])
                try:
                    print(characters[0], nightAction())
                    input()
                except IndexError:
                    try:
                        print(characters[0], nightAction3Left())
                        input()
                    except IndexError:
                        print(characters[0], nightAction2Left())
                        input()
            else:
                random.shuffle(characters)         
        else:
            print('-'*17)
            print('| The sun rises |')
            print('-'*17)
            input()
            actedCharacters = []
            daytime = True

