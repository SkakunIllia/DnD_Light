from Entities import *
from Auxiliary import *

@dlog("choosing class")
def class_choice():
    player_name = read_player_name()
    player_class = read_player_class()
    logger.debug("def class_choice - initializing player")
    player = initialize_entity(player_class, player_name)
    print("Here is your character -> ", end="")
    print(player)
    if verify_answer(input("Is that what you wanted? ")):
        logger.debug("def class_choice - going to the game itself")
        print("Alright, then let's start our journey into the world of D&D Light!")
        return player
    else:
        logger.debug("def class_choice - rechoosing the class or the name")
        return class_choice()

@dlog("greeting the player")
def greeting():
    print("Welcome to the game of D&D Light")
    print("The concept of the game is the same as in the D&D")
    print("The game consists of some random amount of quest that you have to complete")
    print("Then you enter the boss stage and that's all")
    print("Pretty simple, isn't it?")
    print("So let's try this game out!")
    sleep(delay_time)

@separator
@dlog("printing classes")
def print_player_classes():
    print("Here are the classes that you can play in this game: ")
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")
    sleep(delay_time - 5 if delay_time - 5 > 0 else delay_time)

@separator
@dlog("printing classes description")
def print_player_classes_description():
    print("Each class has its own speciality")
    print("1. Archer")
    print(f"\tYou posses a bow with which you can hit enemies from long distance. Health: {Archer.get_health(Archer(None))}.")
    print("2. Wizard")
    print(f"\tYou posses a magic wand with which you can hit enemies from long distance. Health: {Wizard.get_health(Wizard(None))}.")
    print("3. Gnome")
    print(f"\tYou posses a golden pickaxe with which you can hit enemies from short distance. Health: {Gnome.get_health(Gnome(None))}.")
    print("4. Ogr")
    print(f"\tYou posses a mace with which you can hit enemies from medium distance. Health: {Ogr.get_health(Ogr(None))}.")
    print("5. Knight")
    print(f"\tYou posses a silver sword  with which you can hit enemies from short distance. Health: {Knight.get_health(Knight(None))}.")
    sleep(delay_time - 7 if delay_time - 7 > 0 else delay_time)

@separator
@dlog("reading player's name")
def read_player_name():
    while (player_name := input("What is your name? ")) == "":
        logger.debug(f"def read_player_name - null name")
        continue
    return player_name

@dlog("reading player's class")
def read_player_class():
    try:
        while not (player_class := int(input("What class do you want to play? (Enter a number) "))):
            logger.debug(f"def read_player_class - null class")
            continue
        if not ( 1 <= player_class <= 5):
            logger.debug(f"def read_player_class - improper class")
            raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

