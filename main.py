import os, logging, Entities, re
from datetime import datetime
from glob import glob
from functools import wraps
from time import sleep
from random import shuffle

# Logo


# Logger

def log():
    path = "logs/*.log"
    files = glob(path)
    if len(files) >= 5:
        os.remove(files[0])

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
    log_path = os.path.join(log_dir, date_now)
    logging.basicConfig(level = logging.DEBUG, filename = log_path, filemode = "w", format = "%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger("Logger")
    logger.debug("Initializing logger")
    return logger

logger = log()

# Decorators:

def dlog(message = ""):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            logger.debug(f"def {name} - invocation")
            try:
                if message != "":
                    logger.debug(f"def {name} - {message}")
                res = func(*args, **kwargs)
                return res
            except:
                logger.exception(f"At {name} occurred some unexpected error")
        return wrapper
    return dec

@dlog()
def separator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("====================================")
        return func(*args, **kwargs)
    return wrapper

# Functions:

@dlog("printing the logo's separator")
def logo():
    print("=================================================", end = "")
    logger.debug("def logo - printing the logo")
    print(r""" 
     _                                        
    | |                                       
  __| |_   _ _ __   __ _  ___  ___  _ __  ___ 
 / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|
| (_| | |_| | | | | (_| |  __/ (_) | | | \__ \
 \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_|___/
                    __/ |                     
                   |___/ """, end = "")
    print(r""" 
                             _  
                            | |           
              __ _ _ __   __| |
             / _` | '_ \ / _` |
            | (_| | | | | (_| |
             \__,_|_| |_|\__,_| """)
    print(r"""
         _                             
        | |                            
      __| |_ __ __ _  __ _  ___  _ __  ___ 
     / _` | '__/ _` |/ _` |/ _ \| '_ \/ __|
    | (_| | | | (_| | (_| | (_) | | | |__ \
     \__,_|_|  \__,_|\__, |\___/|_| |_|___/
                      __/ |            
                     |___/""", end = "\n")
    logger.debug("def logo - printing the logo's separator")
    print("=================================================")

@dlog("verifying whether the answer is positive")
def verify_answer(string):
    return re.match("Yes|yes|aha|Sure|OK|yeah|Yeah|y|Y|yep|Yep", re.sub(" ", "", string))

@separator
@dlog("printing classes")
def print_player_classes():
    print("Here are the classes that you can play in this game: ")
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")
    sleep(delay_time)

@separator
@dlog("printing classes description")
def print_player_classes_description():
    print("Each class has its own speciality")
    print("1. Archer")
    print(f"\tYou posses a bow with which you can hit enemies from long distance. Health: {Entities.Archer.get_health(Entities.Archer(None))}.")
    print("2. Wizard")
    print(f"\tYou posses a magic wand with which you can hit enemies from long distance. Health: {Entities.Wizard.get_health(Entities.Wizard(None))}.")
    print("3. Gnome")
    print(f"\tYou posses a golden pickaxe with which you can hit enemies from short distance. Health: {Entities.Gnome.get_health(Entities.Gnome(None))}.")
    print("4. Ogr")
    print(f"\tYou posses a mace with which you can hit enemies from medium distance. Health: {Entities.Ogr.get_health(Entities.Ogr(None))}.")
    print("5. Knight")
    print(f"\tYou posses a silver sword  with which you can hit enemies from short distance. Health: {Entities.Knight.get_health(Entities.Knight(None))}.")
    sleep(delay_time)

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
def next_thing():
    @dlog("are we going forward?")
    def internal():
        if verify_answer(input("Are you ready to go further?: ")):
            logger.debug(f"def next_thing - we are going forward")
            return True
        else:
            logger.debug("def next_thing - additional time to make decision")
            print("Alright, take your time, dear guest of mine")
            sleep(2)
            return internal()
    return internal()

@dlog("choosing class")
def class_choice():
    player_name = read_player_name()
    player_class = read_player_class()
    logger.debug("def class_choice - initializing player")
    player = Entities.initialize_entity(player_class, player_name)
    print("Here is your character -> ", end="")
    print(player)
    if verify_answer(input("Is that what you wanted? ")):
        logger.debug("def class_choice - going to the game itself")
        print("Alright, then let's start our journey into the world of D&D Light!")
        return player
    else:
        logger.debug("def class_choice - rechoosing the class or the name")
        return class_choice()

@separator
@dlog()
def quest_complete(q, player):
    luck = Entities.random()
    res = q.complete(luck)
    print("OK") if res else print("NOK")

# Global variables:
delay_time = 1


@dlog()
def main():
    # logo()
    # greeting()
    # next_thing()
    #
    # print_player_classes()
    # print_player_classes_description()
    # next_thing()

    player = class_choice()
    mobs = [Entities.Mob("Zombie" if i % 2 == 0 else "Piglin" if i % 3 == 0 else "Human") for i in range(10)]
    shuffle(mobs)
    quests = [Entities.Quest(f"Quest {i}") for i in range(10)]
    print(quests)
    while len(quests) > 0:
        quest = quests[0]
        quest_complete(quest, player)
        quests.pop(0)
    print("end")

    # next_thing()

main()