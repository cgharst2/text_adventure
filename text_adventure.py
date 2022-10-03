#Written by Connor Gharst

import random

stamina = 100
bag = ["candy"]
wealth = 0


#Riddles for the doors in the basement
#The harder the riddle attempted the more stamina it takes to solve it
#takes more stamina for a wrong answer
def riddles(stamina,bag,wealth):
    print("The three doors all have different riddles with varying difficulty. Easy, medium, or hard")
    print("The easy door gives one coin in return, medium two coins, and hard 3 coins")
    print("What do you do... 'door 1', 'door 2', door 3', or 'open bag'")

    #What English word retains the same pronunciation, even after you take away four of its five letters? Queue (hard)
    #What starts with a 't' ends with a 't' and is full of 't' ? teapot (medium)
    #What is so delicate that saying its name breaks it? Silence (easy)

    user_path = input()
    print()
    response = False

    #keeping track of where the user has been and what the user has completed
    door1 = False
    door2 = False
    door3 = False
    apple = False

    #always checks users wealth until they get to 5
    while wealth < 5:
        response = False
        while response == False:

                #Easy riddle
                if user_path == 'door 1':
                    if door1 == False:
                            print("Riddle: What is so delicate that saying its name breaks it?")
                            if apple == True:
                                print("Being healthy and eating the apple seems to have increased your brain power")
                                print("Hint: The answer rhymes with 'violence'")

                            user_riddle = input("Enter your answer: ")
                            print()
                            if user_riddle.lower() == 'silence':
                                print("The doors burts open and behind lays one coin")
                                wealth += 1
                                print("Wealth: ", wealth)
                                stamina -= 5
                                print("Stamina: ", stamina)
                                door1 = True
                                print("What do you do... 'door 1', 'door 2', door 3', or 'open bag'")
                                user_path = input()
                            elif user_riddle.lower() == 'leave':
                                print("What do you do... 'door 1', 'door 2', door 3', or 'open bag'")
                                user_path = input()
                                print()
                            else:
                                print("You answer but nothing happens, must not have been correct")
                                stamina -= 10
                                print("Stamina: ", stamina)
                                print("Enter 'leave' if you would like to leave this door or continue to attempt this riddle")
                                print()
                    else:
                        print("You have already solved this riddle")
                        print("What do you do... 'door 2', door 3', or 'open bag'")
                        user_path = input()
                        print()
                    response = True

                #Medium riddle
                elif user_path == 'door 2':
                    if door2 == False:
                        print("Riddle: What starts with a 't' ends with a 't' and is full of 't'?")
                        if apple == True:
                            print("Being healthy and eating the apple seems to have increased your brain power")
                            print("Hint: You might pour a hot drink out of this...")

                        user_riddle = input("Enter your answer: ")
                        print()
                        if user_riddle.lower() == 'teapot':
                            print("The door bursts open and behind lays two coins")
                            wealth += 2
                            print("Wealth: ", wealth)
                            stamina -= 10
                            print("Stamina: ", stamina)
                            door2 = True
                            print("What do you do... 'door 1', 'door 2', 'door 3', or 'open bag'")
                            user_path = input()
                            print()
                        elif user_riddle.lower() == 'leave':
                            print("What do you do... 'door 1', 'door 2', door 3', or 'open bag'")
                            user_path = input()
                            print()
                        else:
                            print("You answer but nothing happens, must not have been correct")
                            stamina -= 15
                            print("Stamina: ", stamina)
                            print("Enter 'leave' if you would like to leave this door or continue to attempt this riddle")
                            print()
                    else:
                        print("You have already solved this riddle")
                        print("What do you do... 'door 1', 'door 2', 'door 3', or 'open bag'")
                        user_path = input()
                        print()
                    response = True

                #Hard riddle
                elif user_path == 'door 3':
                    if door3 == False:
                        print("Riddle: What English word retains the same pronunciation, even after you take away four of its five letters?")
                        if apple == True:
                            print("Being healthy and eating the apples seems to have increased your brain power")
                            print("Hint: The last four letters of this five letter word are all vowels")

                        user_riddle = input("Enter your answer: ")
                        print()
                        if user_riddle.lower() == 'queue':
                            print("The door bursts open and behind lays three coins")
                            wealth += 3
                            stamina -= 15
                            print("Wealth: ", wealth)
                            print("Stamina: ", stamina)
                            door3 = True
                            print("What do you do... 'door 1', 'door 2', 'door 3', or 'open bag'")
                            user_path = input()
                            print()
                        elif user_riddle.lower() == 'leave':
                            print("What do you do... 'door 1', 'door 2', 'door 3', or 'open bag'")
                            user_path = input()
                            print()
                        else:
                            print("You answer but nothing happens, must not have been correct")
                            stamina -= 20
                            print("Stamina: ", stamina)
                            print("Enter 'leave' if you would like to leave this door or continue to attempt this riddle")
                            print()
                    else:
                        print("You have already solved this riddle")
                        print("What do you do... 'door 1', 'door 2', 'door 3', or 'open bag'")
                        user_path = input()
                        print()
                    response = True

                #gives user oppurtunity to use items in their bag
                elif user_path == 'open bag':
                    print("Bag: ", ', '.join(bag))
                    print("What will you use? Or 'leave bag'")
                    user_bag = input()
                    print()
                    if user_bag in bag:
                        if user_bag.lower() == 'candy':
                            print("Are you sure you want to eat the candy. You've already had a lot of candy tonight. Maybe you should wait a little bit before eating more... y/n")
                            user_candy = input("Enter y/n: ")
                            if user_candy == 'y':
                                print("You eat the candy and immediately start to get dizzy and everything goes black")
                                print("It's Halloween night and you've already eaten too much candy already... you've had a sugar crash")
                                print("You wake up sometime later but you are missing a coin")
                                wealth -= 1
                                print("Wealth: ", wealth)
                                stamina -= 5
                                print("Stamina: ", stamina)
                                bag.remove('candy')
                            elif user_candy == 'n':
                                continue
                            else:
                                print("Enter either 'y' or 'n'")
                        elif user_bag == 'apple':
                            print("You eat the apple and feel rejuvenated and smarter than ever. These riddles seem easier than ever now...")
                            apple = True
                            bag.remove('apple')
                            stamina += 15
                            print("Stamina: ", stamina)
                        else:
                            print("This is not the time or place to be using this...")
                    elif user_bag == 'leave bag':
                        print("What do you do... 'door 1', 'door 2', door 3', or 'open bag'")
                        user_path = input()
                        print()
                    else:
                        print("Not an item in your bag (check for typo or capitalization)")
                    response = True
                else:
                    print("Please enter either 'door 1', 'door 2', 'door 3', or 'open bag'")
                    user_path = input()
                    print()
    return stamina, bag, wealth

#where lantern is; creepy noises; queen main villain; get trapped; must pay queen money in order to escape/to get lantern;
#pays money to queen then queen dies and lantern apears; solve random riddles in order to get money
#when solving riddles, brain power/stamina decreases with every wrong answer, must eat a banana in order to recover brain power/stamina and get a hint
#if you eat the candy than you have a sugar crash and lose a coin
def Haunted_house(stamina,bag,wealth):
    print('Stamina: ', stamina)
    print('Bag: ', ', '.join(bag))
    print('Wealth: ', wealth)
    print()
    print("You enter the house and it is eerily quiet so first you explore the living room")
    print("There appears to be nothing in the living room except a golden coin")
    print("Do you take the coin ('take coin') or do you go into the kitchen ('kitchen')")
    print()
    
    #In living room, can either take a coin and increase wealth or leave and explore the kitchen
    user_path = input()
    response = False
    while response == False:    
        if (user_path == 'take coin'):
            wealth += 1
            print("Wealth: ", wealth)
            print("You take the coin and go to the kitchen")
            response = True
        elif (user_path == 'kitchen'):
            print("You decide not to take the coin and instead go to the kitchen")
            response = True
        else:
            print("Please enter either 'take coin' or 'kitchen'")
            user_path = input()
            print()
    
    print("In the kitchen all you can see is closed drawers, a pantry, and a staircase down into the basement")
    print("Do you 'search drawers', 'open pantry', or go down into the 'basement'")
    
    #In kitchen, can either explore pantry, search drawers, or leave and go down to the basement
    #coin and apple booleans are to make sure user can only get each of them once
    user_path = input()
    print()
    response = False 
    coin = False
    apple = False
    while response == False:
        if (user_path == 'search drawers'):
            if (coin == False):
                print("You find a coin!")
                wealth += 1
                print("Wealth: ", wealth)
                stamina -= 5
                print("Stamina: ", stamina)
                coin = True
            else:
                print("You have already checked here")
            print("Now do you 'open pantry' or go into the 'basement'?")
            user_path = input()
            print()
        elif (user_path == 'open pantry'):
            if (apple == False):
                print("You open the pantry and find an apple")
                print()                     
                print("                                      _/`.-'`.")
                print("                            _      _/` .  _.'")
                print("                   ..:::::.(_)   /` _.'_./")
                print("                 .oooooooooo\ \o/.-'__.'o.")
                print("                .ooooooooo`._\_|_.'`oooooob.")
                print("              .ooooooooooooooooooooo&&oooooob.")
                print("             .oooooooooooooooooooo&@@@@@@oooob.")
                print("            .ooooooooooooooooooooooo&&@@@@@ooob.")
                print("            doooooooooooooooooooooooooo&@@@@ooob")
                print("            doooooooooooooooooooooooooo&@@@oooob")
                print("            dooooooooooooooooooooooooo&@@@ooooob")
                print("            dooooooooooooooooooooooooo&@@oooooob")
                print("            `dooooooooooooooooooooooooo&@ooooob'")
                print("             `doooooooooooooooooooooooooooooob'")
                print("              `doooooooooooooooooooooooooooob'")
                print("               `doooooooooooooooooooooooooob'")
                print("                `doooooooooooooooooooooooob'")
                print("                 `doooooooooooooooooooooob'")
                print("                  `dooooooooobodoooooooob'")
                print("                   `doooooooob dooooooob'")
                print("                     `'''''' `'''''''''")
                print()
                print("You put the apple in your bag for later")
                bag.append('apple')
                print("Bag: ", ', '.join(bag))
                stamina -= 5
                print("Stamina: ", stamina)
                apple = True
            else:
                print("You have already looked through the pantry")
            print("Now do you 'search drawers' or go into the 'basement'?")
            user_path = input()
            print()
        elif (user_path == 'basement'):
            print("You decide to go down into the basement")
            response = True
        else:
            print("Please enter 'search drawers', 'open pantry', or 'basement'")
            user_path = input()
            print()

    #goes down to basement where riddles and more coins are, as well as introduced to queen
    print("Walking down the stairs you hear some rummaging through the basement")
    print("The basement door slams and locks behind you, you are now at the bottom of the stairs")
    print("All of the sudden the Queen jumps out at you asking for money")
    print("She says that you need 5 coins and she will give you something useful in return, otherwise you are stuck down here forever")
    print("She slowly fades away and disappears")

    print("Being in the basement you can rummage around ('rummage'), or explore the layout ('explore')")
    print()
    user_path = input()
    response = False
    lighter = False
    while response == False:
        if user_path == 'rummage':
            print('You rummage around a find a lighter! Maybe this can be used later...')
            bag.append('lighter')
            print("Bag: ", ', '.join(bag))
            stamina -= 5
            print("Stamina: ", stamina)
            print("Now you start to explore the basement more")
            user_path = 'explore'
        elif user_path == 'explore':
            print("While exploring the basement you come across three doors right next to each other")
            stamina, bag, wealth = riddles(stamina,bag,wealth)
            print()
            print("Wait..... you see something happening in the corner")
            response = True
        else:
            print("Please enter 'rummage' or 'explore'")
            user_path = input()
            print()

    #Queen comes now that the user has at least 5 coins, disappears and gives lantern
    print("IT'S THE QUEEN")
    print("She rushes over to you and forces you to give you all your coins")
    print('"Perfect" she says, "Just enough"')
    print()
    wealth = 0
    print("Wealth: ", wealth)
    print("Once she takes all of your coins she falls to the floor and slowly disappears with light coming down onto her from the sky")
    print("After she's gone, a lantern appears in her place")
    bag.append('lantern')
    print()
    print("Bag: ", ', '.join(bag))
    print()
    print("You leave the house to try and escape through the forest")
    return 'completed', stamina, bag, wealth


# need a lantern to get through the forest, pitch black without; running water that you need to get across
#for running water have two different ways to get across...
#1) use sticks and build a raft across (must forage around and find sticks) 2) try and swim across (float away and end up in new area)
def Forest(stamina,bag,wealth):
    print('Stamina: ', stamina)
    print('Bag: ', ', '.join(bag))
    print('Wealth: ', wealth)

    print()
    print("You try to leave through the forest but it's pitch black and impossible to see, you need some sort of light source to get through")
    
    #Checking for latern and lighter
    if ("lantern" in bag) == True and ("lighter" in bag) == True:
        print("Lucky enough there's a lantern and a lighter in the bag... \nPulls out lantern and lights")
        print("As you walk through the forest you come across a stream of running water")
        print("It doesn't look too dangerous to cross... do you attempt to craft a raft with sticks lying around ('raft') or do you try and swim across ('swim')")
        user_path = input()
        print()

        response = False
        while response == False:
            
            #If user choses to build raft they have to correctly multiply 2 random numbers
            #This is how they can get across the river and possible get to an ending where the user survives
            if user_path == 'raft':
                number1 = random.randint(5,12)
                number2 = random.randint(5,12)
                print("In order to cross this river on a raft, you need a " + str(number1) + " by " + str(number2) + " stick raft")
                print("How many sticks in total do you need and find")
                stick_amount = number1 * number2
                user_guess = int(input())
                if user_guess == stick_amount:
                    print("You grab the correct amount of sticks and build a sufficient raft")
                    print("You cross the stream with no problem")
                    print()
                    stamina -= 15
                    print("Stamina: ", stamina)
                    print("After getting across the stream you can see city lights.")

                    #User must have a certain amount of stamina left in order to get to survival, they have chance to restore stamina with food items in bag
                    if stamina > 30:
                        print("Stamina: ", stamina)
                        print("You just have enough stamina in you to follow these lights and make it back home safely, congratulations you have survived Halloween night!")
                        print("Until next year...")
                        print("~~~~~~~")
                        print("THE END")
                        return 'win', stamina, bag, wealth
                    else:
                        print("Stamina: ", stamina)
                        print("You're running low on stamina and won't be able to make it to the lights at your present state...")
                        print("Maybe there's something you can eat in your bag")
                        print()
                        print("Bag: ", ', '.join(bag))
                        print("You are in your bag, what will you use. If you don't have anything than 'leave bag'")
                        user_bag = input()
                        response = False
                        while response == False:
                                if user_bag in bag:
                                    if user_bag.lower() == 'candy':
                                        print("Its been awhile since you have had candy tonight, this shouldn't hurt")
                                        print("You eat the candy")
                                        stamina += 30
                                        print("Stamina: ", stamina)
                                        bag.remove('candy')
                                        print("Bag: ", ', '.join(bag))
                                    elif user_bag.lower() == 'apple':
                                        print("You eat the apple")
                                        stamina += 50
                                        print("Stamina: ", stamina)
                                        bag.remove('apple')
                                        print("Bag: ", ', '.join(bag))
                                        print()
                                    else:
                                        print("This is not the time or place to being using this")
                                        user_bag = input()
                                        print()
                                elif user_bag.lower() == 'leave bag':
                                    print("You put your bag away")
                                    response = True
                                else:
                                    print("That is not in your bag (check for typo or capitalization)")
                                    print("Enter 'leave bag' if you want to leave your bag")
                                    user_bag = input()
                                    print()
                        if stamina > 30:
                            print("Stamina: ", stamina)
                            print("You just have enough stamina in you to follow these lights and make it back home safely, congratulations you have survived Halloween night!")
                            print("Until next year...")
                            print("~~~~~~~")
                            print("THE END")
                            return 'win', stamina, bag, wealth
                        else:
                            print("You try your best to make it to the lights but your body fails on you and you pass out")
                            print("When you regain consciousness you realize your are in the stream getting carried all the way down")
                            return 'lake', stamina, bag, wealth
                elif user_guess != stick_amount:
                    print("You did not grab the correct amount of sticks and ended up building an insufficient raft")
                    print("Half way across the river, the raft breaks and the river carries you downstream")
                    stamina -= 10
                    print("Stamina: ", stamina)
                    return 'lake', stamina, bag, wealth
                response = True

            #User tries to swim but goes to lake ending
            elif user_path == 'swim':
                print("You try and swim across the river but the current is too strong and it carries you all the way downstream")
                return 'lake', stamina, bag, wealth
                response = True
            else:
                print("Please enter 'raft' or 'swim'")
                user_path = input()
                print()
    elif ("lantern" in bag) == True:
        print("You have a lantern but no way to light it")
        print("There must be something I can use in the house...")
        return 'not completable', stamina, bag, wealth
    elif ("lighter" in bag) == True:
        print("You have a lighter but it is not big enough to light the way")
        print("Maybe there is something bigger in the house that I could light...")
        return 'not completable', stamina, bag, wealth
    else:
        print("There is no light source found in the bag")
        print("There must be something I can use in the house...")
        print()
        return 'not completable', stamina, bag, wealth

#This is one of the endings to the text adventure
def Lake(stamina,bag,wealth):
    print()
    print("You get carried all the way into a lake. Quickly you realise that this lake in right behind the house you explored")
    print("The water starts to suck you in, your feel something pull down on your legs")
    print("You hear whispers all around you as you slowly get pulled down under water")
    print("You start to drown and everything goes black")
    print("You have become the next house ghost, just as the Queen was before...")
    print("You were never seen or heard from again... until the next house victim...")
    print("~~~~~~")
    print("THE END")

# Introduction
print("It's Halloween night and you are out alone looking for your next adventure. All of a sudden you get a text from an unknown number with just an address...")
print("23835 Carve Avenue")
print("'Why not' you say to yourself. You go to the address and quickly notice that it is an abandoned house all sorrounded by forest, with no one in sight")
print("By now it is completely dark outside and you forget which way you came from. Now you are left with two options...")
print("Do you go explore the house ('house') or do you try and leave through the forest ('forest')")

print()

user_path = input()

print()

#Repeat until get valid response
#main outline of the program
response = False
while response == False:
    if (user_path == 'house'):
        completion, stamina, bag, wealth = Haunted_house(stamina,bag,wealth)
        print(completion)
        if completion == 'completed':
           # result_of_forest, stamina, bag, wealth = Forest(stamina,bag,wealth)
            user_path = 'forest'   
    elif (user_path == 'forest'):
        result_of_forest, stamina, bag, wealth = Forest(stamina,bag,wealth)
        if result_of_forest == 'not completable':
            completion, stamina, bag, wealth = Haunted_house(stamina,bag,wealth)
           # response = True
        elif result_of_forest == 'lake':
            Lake(stamina,bag,wealth)
            response = True
        elif result_of_forest == 'win':
            response = True
        else:
            response = True
    else:
        print("Please enter either 'house' or 'forest'")
        print()
        user_path = input()
        print()






