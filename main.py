from random import randint
from os import system, name
import time

class Hero():
    def __init__(self,life,itens):
        self.life = life
        self.itens = itens

    def print_hero(self):
        print("Hero has %s life" %(self.life))
        print("Hero is carrying %s", self.itens)

    def hero_lose_life(self, lose):
        self.life = self.life - lose
        print("Hero lose %s of life and now has %s life" %(lose,self.life))

def read_hero_life(hero):
    if hero.life == 0:
        print("++++++++++++++++++++")
        print("+_+ You are dead +-+")
        print("++++++++++++++++++++")

        exit (1)

def Fight(type, hero):
    life = 0

    if type == "rat":
        life = 5
        while True:
            if life <= 0 or hero.life <= 0:
                break
            print("--> Rat has %s pt of life" %(life))
            print("")

            print("It's your turn")
            dice = Roll_a_Dice()
            if dice > 5:
                print("You hit the rat. He lose 2 pts")
                life = life - 2
            else:
                print("Didn't work")

            print("Keep Fighting. Press ENTER")
            enter = input()

            print("Now it's Rat's turn")
            dice = Roll_a_Dice()
            if dice > 15:
                print("He hit you.")
                hero.hero_lose_life(1)
            else:
                print("Didn't work")

            print("x-x-x-x-x-x-x-x")
            print("Keep Fighting. Press ENTER")
            enter = input()

    elif type == "orc":
        life = 10
        while True:
            if life <= 0 or hero.life <= 0:
                break
            print("--> Orc has %s pt of life" %(life))
            print("")

            print("It's your turn")
            dice = Roll_a_Dice()
            if dice > 8:
                print("You hit the Orc. He lose 2 pts")
                life = life - 2
            else:
                print("Didn't work")

            print("Keep Fighting. Press ENTER")
            enter = input()

            print("Now it's Orc's turn")
            dice = Roll_a_Dice()
            if dice > 15:
                print("He hit you.")
                hero.hero_lose_life(1)
            else:
                print("Didn't work")

            print("Keep Fighting. Press ENTER")
            enter = input()
    elif type == "Dragon":
        life = 50
        while True:
            if life <= 0 or hero.life <= 0:
                break
            print("--> Dragon has %s pt of life" %(life))
            print("")

            print("It's your turn")
            dice = Roll_a_Dice()
            if dice > 15:
                print("You hit the Dragon. He lose 2 pts")
                life = life - 2
            else:
                print("Didn't work")

            print("Keep Fighting. Press ENTER")
            enter = input()

            print("Now it's Dragon's turn")
            dice = Roll_a_Dice()
            if dice > 5:
                print("He hit you.")
                hero.hero_lose_life(1)
            else:
                print("Didn't work")

                print("Keep Fighting. Press ENTER")
                enter = input()

    read_hero_life(hero)
    if life <= 0:
        print("He is dead")
        print("Congrats")

def Roll_a_Dice():
    result = randint(1,20)
    return result

def first_room(hero):
    read_hero_life(hero)

    print("")
    print("Welcome to your first Room, let's see what you see")
    print("At first you are seeing 2 doors. One Metal and another Wood Door")
    print("second you are seeing a little library and a mess table")
    print("And finally you are smelling something bad")

    while True:
        read_hero_life(hero)
        print("")
        print("<<---------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<---------------------------------->>")
        print("Here is your choices")
        print("| 1 - Open the Metal door            |")
        print("| 2 - Open the Wooden door           |")
        print("| 3 - Look at the table              |")
        print("| 4 - Look at the library            |")
        print("<<---------------------------------->>")
        ans = int(input())

        if ans == 1:
            print("Ok, entering in the Metal door")
            going_to_map2(hero)
        elif ans == 2:
            print("Ok, entering in the Wooden door")
            going_to_map3(hero)
        elif ans == 3:
            print("Looking at the table")
            print("Let's try your lucky")
            dice = Roll_a_Dice()
            print(" --> Your dice was: ", dice)
            if dice >= 15:
                print(" *** You find a Potion ***")
            else:
                print(" --- You didn't find anything keep looking ---")
        elif ans == 4:
            print("Looking at the table")
            print("Let's try your lucky")
            dice = Roll_a_Dice()
            print(" --> Your dice was: ", dice)
            if dice >= 18 :
                print(" *** You find a key, looks like a Square *** ")
            else:
                print(" --- You didn't find anything keep looking --- ")

def going_to_map2(hero):
    candle = 0
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing just one door")
    print("second you are seeing a pile of garbage")
    print("You are seeing a little candle burning on the floor")

    while True:
        read_hero_life(hero)
        print("")
        print("<<---------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<---------------------------------->>")
        print("Here is your choices")
        print("| 1 - Open the door                  |")
        print("| 2 - Look at the Garbage            |")
        print("| 3 - Look at the Little Candle      |")
        print("<<---------------------------------->>")
        ans = int(input())

        if ans == 1:
            if candle == 0:
                print("Oh Now, the Door is looked.")
            else:
                print("The door is opened")
                going_to_map4(hero)
        elif ans == 2:
            print("You are looking at the garbage when ... ")
            dice = Roll_a_Dice()
            if dice < 5:
                print("You find a Big Rat coming at to you")
                print("Let's Fight")
                Fight("rat", hero)
            else:
                print("You didn't see nothing usefull")
        elif ans == 3:
            print("Looking at the Candle")
            print("What you wan't to do?")
            print("1 - Burn your hand")
            print("2 - Blow the candle")
            print("3 - Nothing")
            ans2 = int(input())
            if ans2 == 1:
                print("You burn your hand and loose 2 pt of life")
                hero.hero_lose_life(2)
            elif ans2 == 2:
                print("You listened a door unlocking")
                candle = 1
            elif ans2 == 3:
                print("Ok, Go ahead")

def going_to_map3(hero):
    climb = 0
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing one door and listened some annoyng sounds coming from there")
    print("You are seeing a little light at the top of the room")
    print("And finally a very messed table")
    while True:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        print("Here is your choices")
        print("| 1 - Open the door                                     |")
        print("| 2 - Look better for the top to try to find something  |")
        print("| 3 - Look at the table                                 |")
        print("<<----------------------------------------------------->>")
        ans = int(input())

        if ans == 1:
            print("A lot of bats flying at to you killing you little by little ...")
            print("+-+ You are dead +-+")
            exit (1)
        if ans == 2:
            print("You can see a little rope close the wall")
            print("Do you wanna try it? (YES - NO)")
            ans2 = input()
            if ans2 == "Yes" or ans2 == "yes":
                print("Let's Try to Climb it")
                dice = Roll_a_Dice()
                print("DICE WAS ", dice)

                if dice >= 20:
                    print("You climbed so good that ... ")
                    print("You are seeing a way to go, do you wanna go? (YES - NO)")
                    ans3 = input()
                    if ans3 == "Yes" or ans3 == "yes":
                        going_to_map5(hero)
                elif dice > 5:
                    climb+=1
                    print("You are climbing")
                    print("Keep going ...")
                else:
                    print("You felt !! Ouch. Loose 1 pt of life")
                    hero.hero_lose_life(1)
                    print("Keep going ...")
                    climb-=1
                if climb >= 3:
                    print("You are seeing a way to go, do you wanna go? (YES - NO)")
                    ans3 = input()
                    if ans3 == "Yes" or ans3 == "yes":
                        going_to_map5(hero)
            else:
                print("Ok, Go Ahead")
        if ans == 3:
            print("You are looking at the table when..")
            dice = Roll_a_Dice()
            print("DICE WAS ", dice)
            if dice > 15:
                print("You find a Sword")
            else:
                print("Didn't find anything")

def going_to_map4(hero):
    clue = 0
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing a very dark stairs at your front")
    print("and finally You are seeing a little Statue")
    while True:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        print("Here is your choices")
        print("| 1 - Go to the Stairs                                  |")
        print("| 2 - Look better for little Statue  |")
        print("<<----------------------------------------------------->>")
        ans = int(input())

        if ans == 1:
            if clue == 0:
                print("You tried to go but you lost 10 minutos and you see a looked door.")
                print("Now you are back to the room again")
            elif clue == 2:
                going_to_map6(hero)
            else:
                print("It's so dark that you can't see the steps ")
        if ans == 2:
            print("Looking at the Little Statue you can:")
            print("1- Touch to feel the statue")
            print("2- Try hard to find something looking the details")
            print("3- Do Nothing and forget it")
            ans2 = int(input())
            if ans2 == 1:
                print("You feel something hot in the statue")
            elif ans2 == 2:
                dice = Roll_a_Dice()
                print("Your dice WAS ", dice)
                if dice == 20:
                    print("You LUCKY")
                    print("You can see some lights over the stairs")
                    print("AND")
                    print("You can see some weird sounds over the stairs")
                    clue = 2
                elif dice >= 15 and dice <<20 :
                    print("You can see something strange in the statue")
                    print("Try it? (YES - NO)")
                    ans3 = input()
                    if ans3 == "Yes" or ans3 == "yes" and clue == 0:
                        print("You can see some lights over the stairs")
                        clue = clue + 1
                    elif ans3 == "Yes" or ans3 == "yes" and clue == 1:
                        print("You can see some weird sounds over the stairs")
                        print("Go Ahed to see what's it is")
                        clue = clue + 1
                else:
                    print("There are nothing important here")
            elif ans3 == 3:
                print("Ok, Go Ahead")

def going_to_map5(hero):
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing two doors with colors. One White and Second one Dark Gray")
    print("Some Scriptures one the wall ")
    while True:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        print("Here is your choices")
        print("| 1 - Go to the White Door                              |")
        print("| 2 - Go to the Dark Grey Door                          |")
        print("| 3 - Look at the wall                                  |")
        print("<<----------------------------------------------------->>")
        ans = int(input())
        if ans == 1:
            print("You are ready to fall down in the big role on the floor")
            print("Try to scape. Press ENTER do roll your Dice... Muahahaha")
            enter = input()
            dice = Roll_a_Dice()
            print("DICE WAS ", dice)
            if dice >> 15:
                print("You are alive and go back to the room")
            else:
                print("+-+ You are dead +-+")
                print("Muahahahahahahahhaha")
        elif ans == 2:
            print("You opened the door and you are going to the next room")
            going_to_map7(hero)
        elif ans == 3:
            print("You are looking to the scriptures")
            print("Those scriptures are so strange, and so dark but you can see")
            print("... White colors are showing dark gray people dying")
            print("... and Dark Gray colors are showing white people dying")

def going_to_map6(hero):
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("Oh No... You are seeing a very big Orc, ready to fight!!!")
    print("And a very big Door behind him")
    while True:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        Fight("orc", hero)
        print("You are going to the next room")

    going_to_map8(hero)

def going_to_map7(hero):
    read_hero_life(hero)

    print("")
    print("Welcome to the next Room, No. Wait. It's not a room")
    print("It's a very large Hall")
    print("at the walls you can see some Torches and Paintings")
    print(" while Walking around the Hall you listening waterfalls around you")
    print("Sometimes you can't see your foot, sometimes you can't see nothing")
    while True:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        print("Here is your choices")
        print("| 1 - Keep Walking until find something                 |")
        print("| 2 - Go and take a torch                               |")
        print("<<----------------------------------------------------->>")
        ans = int(input())
        if ans == 1:
            print("You see one door and are you ready to go in?")
            print("(YES - NO)")
            ans3 = input()
            if ans3 == "Yes" or ans3 == "yes":
                going_to_map9(hero)
        elif ans == 2:
            print("Do you wanna take one?")
            print("(YES - NO)")
            ans3 = input()
            if ans3 == "Yes" or ans3 == "yes":
                print("You Got a Torch")

def going_to_map8(hero):
    read_hero_life(hero)
    swim = 0

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("Oh no, you are tired after the fight and")
    print("Now you are seeing a very large river")
    print("The otherside of the river you are seeing your next door")
    print("Ok, you don't have a choice again")
    print("So, let's Swim")
    while True and swim < 5:
        read_hero_life(hero)
        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        dice = Roll_a_Dice()
        print("DICE WAS ", dice)
        if dice > 5:
            print("you are swimming good")
            swim = swim + 1
        elif dice >= 3 and dice <= 4:
            print("You are stuck")
        else:
            print("you are drowning yourself")
            hero.hero_lose_life(1)
        print("Press ENTER to keep Going")
        enter = input()
    going_to_map9(hero)

def going_to_map9(hero):
    read_hero_life(hero)
    pieces = {'King':0,'Queen':0,'Tower':0,"Horse":0}

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("WHen you entered in this room you listened some voice saying")
    print("--------------------------------")
    print("- Do you think you will pass?  -")
    print("- You will never find the exit -")
    print("- I will kill you first        -")
    print("- This is you final test       -")
    print("- Try to scape it              -")
    print("-       OR DIE                 -")
    print("--------------------------------")
    print("After it you see 3 Doors and Puzzle Games")
    print("You can see 4 Statues - 1 King - 1 Queen - 1 Tower - 1 Horse")
    print("And you see for squares on the ground")

    while True:
        read_hero_life(hero)
        if pieces['King'] == 2 and pieces['Queen'] == 1 and pieces['Horse'] == 3 and pieces['Tower'] == 4:
            print("You listened a door opening")
            break

        print("")
        print("<<----------------------------------------------------->>")
        print("| Personagem com %s pontos de vida   |" %(hero.life))
        print("| Lista de itens na mochila: %s      |" %(hero.itens))
        print("<<----------------------------------------------------->>")
        print("Here is your choices")
        print("| 1 - Try to open 1 door                                |")
        print("| 2 - Try to change some piece position                 |")
        print("<<----------------------------------------------------->>")
        ans = int(input())
        if ans == 1:
            print("Which door you will Try")
            print("1 - Gray Door\n2- Black Door\n3- White Door")
            ans2 = int(input())
            if ans2 == 1:
                print("Welcome to the Hell - You are Dead")
                exit(1)
            elif ans2 == 2:
                print("You find a Dragon, Let's Fight")
                Fight("Dragon", hero)
            elif ans2 == 3:
                print("This door is locked")
        elif ans == 2:
            print("Actual positions is: ", pieces)
            print("Which piece do you wanna change?")
            print("King\nQueen\nTower\nHorse")
            ans2 = input()
            if ans2 in pieces.keys():
                print("You have 4 spaces with numbers 1 to 4")
                print("Where do you wanna put it")
                ans3 = int(input())
                if ans3 <= 4:
                    pieces[ans2]=ans3
                else:
                    print("You choose an wrong place")
            else:
                print("You choose an wrong piece.")

    print("You are seeing the light coming from this door")
    print("You are listening birds singing")
    print("And sounds like waterfalls")
    print("You WIN")
    time.sleep(2)
    print("OR NOT")
    print("Your destiny still be mine")
    print("Are you ready?")

def start():
    hero = Hero(30,[])
    print("\n")
    print("You are in your first room.")
    print("Pay atenttion for this rule")
    print("YOU NEVER COME BACK")
    print("Find the EXIT")
    print("Or DYE trying")
    first_room(hero)

def init_game():
    print ("Welcome to RPGMaze")
    print("Are you ready to enter in Dangeon?")
    ans=input("Yes or No to exit:\n")

    if ans == "Yes" or ans == "yes":
        print("Welcome to your new destiny!")
        start()
    elif ans == "No" or ans == "no":
        print("Bye Bye LOSER")
        print("And never come back again Muahahaha")

init_game()
