from random import randint
from os import system, name

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

def Fight(type, hero):
    life = 10

    while life >> 0 or hero.life == 0 :
        if type == "rat":
            print("Fighting a Rat")

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
                print("Hi hit you and you lose 1 pts")
                hero.hero_lose_life(1)
            else:
                print("Didn't work")
            print("Keep Fighting. Press ENTER")
            enter = input()

def Roll_a_Dice():
    result = randint(1,20)
    return result

def first_room(hero):
    print("")
    print("Welcome to your first Room, let's see what you see")
    print("At first you are seeing 2 doors. One Metal and another Wood Door")
    print("second you are seeing a little library and a mess table")
    print("And finally you are smelling something bad")

    while True:
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

    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing just one door")
    print("second you are seeing a pile of garbage")
    print("You are seeing a little candle burning on the floor")

    while True:
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
    print("")
    print("Welcome to the next Room, let's see what you see")
    print("At first you are seeing one door and listened some annoyng sounds coming from there")
    print("You are seeing a little light at the top of the room")
    print("And finally a very messed table")
    while True:
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
            print("You are dead")
            exit (1)
        if ans == 2:
            print("You can see a little rope close the wall")
            print("Do you wanna try it? (YES - NO)")
            ans2 = input()
            if ans2 == "Yes" or ans2 == "yes":
                print("Let's Try to Climb it")
                dice = Roll_a_Dice()
                print("DICE WAS ", dice)
                if dice > 5:
                    climb+=1
                    print("You are climbing")
                    print("Keep going ...")
                else:
                    print("You felt !! Ouch. Loose 1 pt of life")
                    print("Keep going ...")
                    climb-=1

                if climb >= 5:
                    print("You are seeing a way to go, do you wanna go? (YES - NO)")
                    ans3 = input()
                    if ans3 == "Yes" or ans3 == "yes":
                        going_to_map5()
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
    pass

def going_to_map5(hero):
    pass

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
