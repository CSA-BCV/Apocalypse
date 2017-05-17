# Bryson Vogel
# Comp. Prog. 1
# 4-19-17
# This version has no errors, as it is the final version
# While the origional idea for the damage was a number that
# was random and changed every attack, due to problems with
# the calling of variables it is now set up as a random number
# from a range every new game, and is the same for that game
# forever. There is also no save/load feature, as I couldn't
# get it to work in time. Spd (player speed) is no longer used,
# so who attacks first and if you get away is completely random.
# Make sure to download and/or save gameover.txt in order for
# this program to work.
import time
import random
import os

espd = 5


class Enemy(object):  ##enemy class
    def __init__(self, espd):
        self.damage = 5
        self.speed = espd


def start_menu():
    try:
        start_options = int(input('''Welcome to Apocalypse Version 5!
your options are:

1) New Game

2) Quit Game

please enter 1, or 2
What do you want to do?\n'''))
        enemies_killed = 0
        espd = 5
        level = 1
        bosses_killed = 0
        x = 0
        y = 0
        ehealth = 10
        health = 20
        ehealth2 = ehealth * 2
        gameinventory = {'health potion': 1}
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if_elif_else(start_options, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory,
                     ehealth2)
    except ValueError:
        print('Incorrect input, please try again')
        start_menu()


def if_elif_else(start_options, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory,
                 ehealth2):
    if start_options == 1:
        global name
        name = input('What is your name?\n')  ##player name
        new_game_race(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)
    elif start_options == 2:
        quit()
    else:
        print('Please enter a correct value.')
        start_menu()


def new_game_race(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2):
    try:
        global race
        race = int(input('''What race do you want to be?

        your choices are:

        1) Elf
        2) Human
        3) Goblin
        4) Orc
        5) Dwarf
        \n'''))  # player race
        new_game_class(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)
    except ValueError:
        print('Incorrect input, please try again.')
        new_game_race(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)


def new_game_class(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2):
    try:
        global class1
        class1 = int(input('''What class do you want?

    your choices are:

    1) Archer (Bow)
    2) Knight (Sword)
    3) Thief (Knives)
    4) Beserker (Club)
    5) Cleaver (War-axe)

\n'''))  ##player weapons class
        print("""Your health will start at 20, and you enemy's health will start
at 10. Both will double each level. Each level, your damage will multiplied
by two and one half so you can beat the boss (or at least have a chance).
Every five levels, you will fight a boss with double your health.
Potions add four times your level to you health (so if your level is 1, you get
4 more health). The directions to go in are north, south, east, and west,
written as n, s, e, or w. You cannot go more than a hundred in any direction.
The inventory will be shown as a dictionary class, so the part in marks (like
these: ' ') will be the item's name (used to search for items to use) and the
number after the colon (colon = :) is how many you have.
This message will close in 30 seconds""")
        time.sleep(30)
        os.system('cls' if os.name == 'nt' else 'clear')
        if_else(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)
    except ValueError:
        print('Incorrect input, please try again.')
        new_game_class(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)


def if_else(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2):
    if race == 1 or race == 2 or race == 3 or race == 4 or race == 5:
        if class1 == 1 or class1 == 2 or class1 == 3 or class1 == 4 or class1 == 5:
            stats1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)
        else:
            print('Please choose a correct class.')
            new_game_class(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)
    else:
        print('Please choose a correct race.')
        new_game_race(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, ehealth2)


def stats1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory,
           ehealth2):  # generates the race, class, and speed, then prints what they are for the user.
    import random
    if class1 == 1:
        if race == 1:
            weapon = random.randrange(5, 9)
        else:
            weapon = random.randrange(2, 6)
    if class1 == 2:
        if race == 2:
            weapon = random.randrange(3, 7)
        else:
            weapon = random.randrange(4, 8)
    if class1 == 3:
        if race == 3:
            weapon = random.randrange(4, 8)
        else:
            weapon = random.randrange(3, 7)
    if class1 == 4:
        if race == 4:
            weapon = random.randrange(5, 9)
        else:
            weapon = random.randrange(1, 5)
    if class1 == 5:
        if race == 5:
            weapon = random.randrange(5, 9)
        else:
            weapon = random.randrange(2, 6)
    if race == 1 or race == 3:
        spd = random.randrange(5, 10)
    elif race == 4 or race == 5:
        spd = random.randrange(1, 6)
    else:
        spd = random.randrange(3, 8)
    racedict = {1: 'elf', 2: 'human', 3: 'goblin', 4: 'orc', 5: 'dwarf'}
    classdict = {1: 'archer', 2: 'knight', 3: 'thief', 4: 'beserker', 5: 'cleaver'}
    os.system('cls' if os.name == 'nt' else 'clear')
    print(str(name)+', You are a(n) ' + racedict[race] + ' ' + classdict[class1])
    move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    try:
        global move
        move = int(input('How many spaces do you want to move?\n'))
        movement(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2)
    except ValueError:
        print('Please enter a number for movement.')
        move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def movement(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    direction = input('What direction do you want to travel in?\n').lower()
    if direction == 'n':
        y += move
        if y >= 100:
            y = 100
            print('''You can only go this far(x or y of 100).
You are teleported to the center of the map.''')
            x = 0
            y = 0
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
        else:
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
    elif direction == 's':
        y -= move
        if y <= (-100):
            y = (-100)
            print('''You can only go this far(x or y of 100).
You are teleported to the center of the map.''')
            x = 0
            y = 0
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
        else:
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
    elif direction == 'e':
        x += move
        if x >= 100:
            x = 100
            print('''You can only go this far(x or y of 100).
You are teleported to the center of the map.''')
            x = 0
            y = 0
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
        else:
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
    elif direction == 'w':
        x -= move
        if x <= (-100):
            x = (-100)
            print('''You can only go this far(x or y of 100).
You are teleported to the center of the map.''')
            x = 0
            y = 0
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
        else:
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
    else:
        print('Please choose a correct direction.')
        movement(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2)


def check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                    ehealth2):
    print('x of ' + str(x))
    print('y of ' + str(y))
    print('You have ' + str(gameinventory) + ' in your inventory.')
    use_or_no = input('Do you want to use an item?\n').lower()
    if use_or_no == 'yes':
        which_item = input('What is the full name of the item you want?\n')
        if bool(which_item in gameinventory) == True:
            health += (level * 4)
            print('Your health has been boosted by a ' + which_item + ', and is now ' + str(health))
            gameinventory[which_item] -= 1
            enemy_or_not(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2)
        elif bool(which_item in gameinventory) == False:
            print('There is no item with that name in your inventory!')
            check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
        else:
            print('Error')
    elif use_or_no == 'no':
        enemy_or_not(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)
    else:
        print('Error or you entered a wrong input, please try again.')
        check_inventory(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                        ehealth2)


def enemy_or_not(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):
    import random
    en_or_not = random.randrange(1, 3)
    if en_or_not == 1:
        typeen = random.randrange(1, 3)
        if typeen == 1:
            print('You are confronted by an orc!')
            fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2)
        else:
            print('You are confronted by a gang of goblins!')
            fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2)
    else:
        print('All is quiet.')
        move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    try:
        global choice
        choice = int(input('''What do you want to do?
       your choices are:

       1) attack
       2) run\n'''))
        if_else_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                        ehealth2)
    except ValueError:
        print('Please enter a correct input')
        fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


class Boss(object):
    def __init__(self):
        a = Enemy(espd)
        self.damage = (a.damage * 5)
        self.speed = (a.speed)


def next_level(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    if level % 5 == 0:
        openit = open('completeboss.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        quit_or = input('Do you want to quit?\n').lower()
        if quit_or == 'yes':
            quit()
        else:
            stats_update(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                         ehealth2)
    else:
        openit = open('complete.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        quit_or = input('Do you want to quit?\n').lower()
        if quit_or == 'yes':
            quit()
        else:
            stats_update(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                         ehealth2)


def stats_update(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):
    for i in range(6):
        print('Updating stats')
        time.sleep(1)
        print('Updating stats.')
        time.sleep(1)
        print('Updating stats..')
        time.sleep(1)
        print('Updating stats...')
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    y = 0
    x = 0
    enstat = Enemy(espd)
    boss = Boss()
    weapon += (weapon * 2) + (weapon / 2)
    spd = spd * 2
    health = health * 2
    enstat.damage = enstat.damage * 2
    espd = espd * 2
    level += 1
    move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def boss_fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    boss = Boss()
    import random
    global bosses
    global ran
    ran = random.randrange(1, 11)
    bosses = {1: 'Freddy the Evil!', 2: 'Marco the Deadly!', 3: 'Paul the Disastrous!', 4: 'Bryson the Overlord!',
              5: 'The Black One!', 6: 'The Man-eating Venus Fly Trap!', 7: 'The Megalodon!',
              8: 'A Swarm of Tribbles (they may look cute, but their numbers will overwhelm you)!', 9: 'Freddy Kruger!',
              10: 'A rather large slime. What an uninteresting boss...'}
    print('You are confronted by the boss: ' + str(bosses[ran]))
    boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2)


def boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):
    try:
        global what_do
        what_do = int(input('''What do you want to do?
your choices are:

1) attack
2) run
3) flail around like a chicken

please enter 1, 2, or 3
\n'''))
        battle(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)
    except ValueError:
        print('Please enter a number.')
        boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)


def battle(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2):
    boss = Boss()
    already = 0
    ren = random.randrange(1, 3)
    if what_do == 1:
        if ren==1:
            print("You're faster and attack first!")
            player_boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y,
                               gameinventory, spd, weapon, ehealth2)
        else:
            print('The boss is faster attacks first!')
            boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                        weapon, ehealth2)
    elif what_do == 2:
        ren=random.randrange(1,3)
        if ren==1:
            print('You escape!')
            move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2)
        else:
            print('The boss was faster and caught you!')
            boss_damage(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                        ehealth2)
    elif what_do == 3:
        print('Really? You choose to flail? <facepalm>')
        boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)
    else:
        print('Please enter 1, 2 or 3.')
        boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)


def player_boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                       weapon, ehealth2):
    if already == 0:
        print("The boss's health is " + str(ehealth2))
        print('You attack, dealing ' + str(weapon) + ' damage!')
        ehealth2 -= weapon
        print("The boss's health is now " + str(ehealth2))
        already = 1
        boss_death1(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                    weapon, ehealth2)
    else:
        print("The boss's health is " + str(ehealth2))
        print('You attack, dealing ' + str(weapon) + ' damage!')
        ehealth2 -= weapon
        print("The boss's health is now " + str(ehealth2))
        boss_death(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                   ehealth2)


def boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                ehealth2):
    boss = Boss()
    if already == 0:
        print('Your health is ' + str(health))
        print('The boss attacks, dealing ' + str(boss.damage) + ' damage!')
        health -= boss.damage
        print('Your health is now ' + str(health))
        player_death2(already, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)
    else:
        print('Your health is ' + str(health))
        print('The boss attacks, dealing ' + str(boss.damage) + ' damage!')
        health -= boss.damage
        print('Your health is now ' + str(health))
        player_death3(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                      ehealth2)


def if_else_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                    ehealth2):
    global ememies_killed
    import random
    already = 0  # a variable that will determine what functions to run.
    ren = random.randrange(1, 3)
    if choice == 1:
        if ren==1:
            print("Your speed is greater than the enemy's! You attack first!")
            player_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory,
                          spd, weapon, ehealth2)
        else:
            print('Oh no! The enemy is faster and attacks first instead!')
            enemy_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                         weapon, ehealth2)
    elif choice == 2:
        if ren==1:
            print('Your speed is greater, you got away!')
            move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2)
        else:
            print('The enemy caught you!')
            already = 1
            enemy_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                         weapon, ehealth2)
    else:
        print('Please enter a correct input (1 or 2)')
        fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def enemy_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):
    en = Enemy(espd)
    if already == 0:
        print('Your health is ' + str(health))
        health -= en.damage
        print('The enemy did ' + str(en.damage) + ' damage to you!')
        print('Your health is now ' + str(health))
        player_death(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                     weapon, ehealth2)
    else:
        print('Your health is ' + str(health))
        health -= en.damage
        print('the enemy did ' + str(en.damage) + ' damage to you!')
        print('Your health is now ' + str(health))
        player_death1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                      ehealth2)


def player_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                  weapon, ehealth2):
    if already == 0:
        print("The enemy's health is " + str(ehealth))
        ehealth -= weapon
        print('You did ' + str(weapon) + ' damage to the enemy!')
        print("The enemy's health is now " + str(ehealth))
        enemy_death(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                    weapon, ehealth2)
    else:
        print("The enemy's health is " + str(ehealth))
        ehealth -= weapon
        print('You did ' + str(weapon) + ' damage to the enemy!')
        print("The enemy's health is now " + str(ehealth))
        enemy_death1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)


def enemy_death(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                ehealth2):  # runs if player attacked and enemy did not
    if ehealth <= 0:
        ehealth=10*level
        print('You win!')
        enemies_killed += 1
        if 25 - enemies_killed <= 0:
            if level % 5 == 0:
                boss_fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
            else:
                next_level(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                           weapon, ehealth2)
        else:
            print('You have ' + str(25 - enemies_killed) + ' enemies left to kill before you move to the next level.')
            item(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2)
    else:
        already = 1
        enemy_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                     weapon, ehealth2)


def enemy_death1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):  # runs if both player and enemy have attacked
    if ehealth <= 0:
        ehealth=10*level
        print('You win!')
        enemies_killed += 1
        if 25 - enemies_killed <= 0:
            if level % 5 == 0:
                print('You are suddenly, magically wisked away before you can even see if the enemy dropped anything!')
                boss_fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                            weapon, ehealth2)
            else:
                print('You are suddenly, magicallywisked away before you can even see if the enemy dropped anything!')
                next_level(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                           weapon, ehealth2)
        else:
            print('You have ' + str(25 - enemies_killed) + ' enemies left to kill before you move to the next level.')
            item(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2)
    else:
        fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def item(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
         ehealth2):  # determines if the enemy drops a potion or not
    it = random.randrange(1, 3)
    if it == 1:
        print('The enemy dropped a health potion! =)')
        gameinventory['health potion'] += 1
        move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)
    else:
        print('Aww... the enemy dropped nothing... =(')
        move1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def boss_death(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
               ehealth2):  # runs if boss attacked and player just attacked
    if ehealth2 <= 0:
        ehealth2=ehealth*2
        print('You win!')
        bosses_killed += 1
        next_level(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                   ehealth2)
    else:
        boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)


def boss_death1(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                ehealth2):  # runs if player atacked and boss has not yet
    if ehealth2 <= 0:
        ehealth2=ehealth*2
        print('You win!')
        bosses_killed += 1
        next_level(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                   ehealth2)
    else:
        already = 1
        boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                    weapon, ehealth2)


def player_death(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                 ehealth2):  # runs if enemy attacked first and player has not.
    if health <= 0:
        openit = open('gameover.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_menu()
    else:
        already = 1
        player_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                      weapon, ehealth2)


def player_death1(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2):  # runs if both enemy and player atacked.
    if health <= 0:
        openit = open('gameover.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_menu()
    else:
        fight(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon, ehealth2)


def player_death2(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                  weapon, ehealth2):  # runs if boss attacked and player has not.
    if health <= 0:
        openit = open('gameover.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_menu()
    else:
        already = 1
        boss_damage(already, health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd,
                    weapon, ehealth2)


def player_death3(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                  ehealth2):  # runs if both boss and player have attacked.
    if health <= 0:
        openit = open('gameover.txt', 'r')
        readit = openit.read()
        print(str(readit))
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_menu()
    else:
        boss_choices(health, ehealth, enemies_killed, espd, level, bosses_killed, x, y, gameinventory, spd, weapon,
                     ehealth2)


start_menu()