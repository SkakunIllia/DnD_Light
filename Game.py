from Entities import *
import DeathException

#===================================================================================
# Generators
def gen_desc_main_locations():
    dsc = [("My dear friend, you have appeared to be brave enough to get here.\n"
            "Our journey starts from here, my lovely guest - from a cold campfire.\n"
            "You are going towards to new adventures and you have already discovered \n"
            "the first one. There is the cave, but you are not really sure what is \n"
            "in there. You feel interested about discovering it, but also strangely \n"
            "confused of the cave. You are trying to approach it carefully...")]
    index = 0
    while index < len(dsc):
        res = dsc[index]
        index += 1
        yield res

def gen_desc_quests():
    dsc = [("\"It is dark here and I here somebody there, deep in the cave\", \n"
        "you say. You think of a few ways of coping with it:\n"
        "\t1. You can ignore the cave and go ahead the road near the cave.\n"
        "\t2. Nevertheless you are not aware of what is inside the cave, but \n"
        "\tif you sneak inside, take all the valuable and get out of there?\n"
        "\t3. Because there might be something that is very dangerous and you\n"
        "\tmight start the fight with the mobs")]
    index = 0
    while index < len(dsc):
        res = dsc[index]
        index += 1
        yield res

#===================================================================================
# Global variables
mob_names = ["Zombie", "Skeleton", "Ogr", "Giant"]
quest_desc = gen_desc_quests()
main_locations_desc = gen_desc_main_locations()

#===================================================================================
# Functions
@separator
@dlog("getting player's option to the quest")
def quest_get_option():
    try:
        while not (option := int(input("Which option would you like to pick? (Enter a number from a list above) "))):
            logger.debug(f"def quest_get_option - null option")
            continue
        if not (1 <= option <= 3):
            logger.debug(f"def quest_get_option - improper option")
            raise ValueError("Wrong option. Usage: 1 <= player_class <= 3")
        return option
    except ValueError:
        return quest_get_option()

@dlog()
def quest_complete(luck, predicate):
    return predicate(luck)

@dlog()
def quest_is_successful(option):
    if option == 1:
        logger.info("def quest_is_successful - option 1")
        return quest_complete(random(), lambda x: x > 0)
    elif option == 2:
        logger.info("def quest_is_successful - option 2")
        return quest_complete(random(), lambda x: x > 50)
    else:
        logger.info("def quest_is_successful - option 3")
        return quest_complete(random(), lambda x: x > 20)

@dlog()
@separator
def quest1(player):
    print("QUEST 1")
    desc = next(quest_desc)
    print(desc)
    sleep(delay_time - 1)
    option = quest_get_option()
    is_successful = quest_is_successful(option)
    sep()
    logger.info(f"def quest1 - is option successful? {is_successful}")

    def fight():
        sleep(delay_time_quest)
        logger.info("def ques1.fight - the player has started the fight")
        mobs = [
            Mob(
                mob_names[randint(0, len(mob_names) - 1)]
                for _ in range(4)
            )
        ]
        for i, mob in enumerate(mobs):
            sleep(delay_time_quest)
            logger.info(f"def quest1 - player attack the mob {i}")
            player.attack(mob)
            if player.get_health() < 0:
                logger.info("def quest1 - player has died")
                print("Unfortunately you have been killed")
                raise DeathException
        sleep(delay_time_quest)
        logger.info("def quest1 - player has won the fight")
        print("It was tough, but you have perfectly fought and won the battle of the Cave")
        player.add_item(Item("Diamond"))
        end_of_quest()

    def end_of_quest():
        sleep(delay_time_quest)
        logger.info("def quest1 - the player is outside the cave")
        print("\nNow you are outside the cave and going further the road."
              "\nIt is dark outside so you decided to rest for a little bit")
        sleep(delay_time_quest)
        print("\nYou look at yourself in a river as in the mirror and wonder about this magical effect...")
        print(player)
        sleep(delay_time)

    if option == 1:
        logger.info("def quest1 - the player leaves the quest")
        print("Well, sometimes it is better to omit possible problem.\nNevertheless you don't get the prize")
    elif option == 2:
        logger.info("def quest1 - the player tries to sneak into the cave")
        if is_successful:
            sleep(delay_time_quest)
            logger.info("def quest1 - the player sneaked into the cave successfully")
            print(
                "Heeeah! You got inside sneakily and found "
                "there something really interesting")
            player.add(Item("Diamond"))
        else:
            logger.info("def quest1 - the player has been noticed while sneaking into the cave")
            print("You have been noticed while sneaking into the cave.\nThe fight has started")
            fight()
    elif option == 3:
        if is_successful:
            print("You have started really cruel fight with the monsters")
            fight()
        else:
            logger.info("def quest1 - the player has died in a fight")
            print("There were two giant zombies that, unfortunately, killed you...")
            raise DeathException

@separator
@dlog()
def quest2():
    pass

@separator
@dlog()
def main_location1():
    desc = next(main_locations_desc)
    print(desc)
    sleep(delay_time)

@dlog()
def game(player):
    try:
        main_location1()
        quest1(player)
        next_thing()
        end_of_game()
        input()
    except DeathException:
        death()

@separator
@dlog()
def end_of_game():
    print(r"""
  _____ _    _ ______   ______ _   _ _____  
 |_   _| |  | |  ____| |  ____| \ | |  __ \ 
   | | | |__| | |__    | |__  |  \| | |  | |
   | | |  __  |  __|   |  __| | . ` | |  | |
  _| |_| |  | | |____  | |____| |\  | |__| |
 |_____|_|  |_|______| |______|_| \_|_____/
 """)

@separator
@dlog()
def death():
    print("Unfortunately you have been killed")
    end_of_game()