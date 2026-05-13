from Entities import *
#===================================================================================
# Locations and Location-Quests
class Location:
    def __init__(self, name = "Location", desc = "Lorem ipsum"):
        self._name = name
        self._random_value = random()
        self._desc = desc
    def get_desc(self):
        print(self._desc)
        return self._desc
    def set_desc(self, desc):
        self._desc = desc
    def print_desc(self):
        print(self._desc)
    def __repr__(self):
        return f'Location[Name: {self._name}, luck to complete: {self._random_value}]'

mob_names = ["Zombie", "Skeleton", "Ogr", "Giant"]

def quest1(desc):
    pass

@dlog("getting player's option to the quest")
def quest_get_option():
    try:
        while not (option := int(input("Which option would you like to pick? (Enter an integer) "))):
            logger.debug(f"def quest_get_option - null option")
            continue
        if not (1 <= option <= 3):
            logger.debug(f"def quest_get_option - improper option")
            raise ValueError("Wrong option. Usage: 1 <= player_class <= 3")
        return option
    except ValueError:
        return quest_get_option()

def gen_desc_main_location():
    dsc = [("My dear friend, you have appeared to be brave enough to get here.\n"
            "Our journey starts from here, my lovely guest - from a cold campfire.\n"
            "You are going towards to new adventures and you have already discovered \n"
            "the first one. There is the cave, but you are not really sure what is \n"
            "in there. You feel interested about discovering it, but also strangely \n"
            "confused of the cave. You are trying to approach it carefully...\n")]
    index = 0
    while index < len(dsc):
        res = dsc[index]
        index += 1
        yield res

def gen_desc_quests():
    dsc = [("\n\"It is dark here and I here somebody there, deep in the cave\", \n"
        "you say. You think of a few ways of coping with it:\n"
        "\t1. You can ignore the cave and go ahead the road near the cave.\n"
        "\t2. Nevertheless you are not aware of what is inside the cave, but \n"
        "\tif you sneak inside, take all the valuable and get out of there?\n"
        "\t3. Because there might be something that is very dangerous and you\n"
        "\tmight start the fight with the mobs\n")]
    index = 0
    while index < len(dsc):
        res = dsc[index]
        index += 1
        yield res

@dlog
def quest_complete(luck, predicate):
    return predicate(luck)

@dlog
def is_successful(option):
    if option == 1:
        return quest_complete(random(), lambda x: x > 0)
    elif option == 2:
        return quest_complete(random(), lambda x: x > 60)
    else:
        return quest_complete(random(), lambda x: x > 40)




@dlog()
def quest_complete(luck, predicate):
    return predicate(luck)