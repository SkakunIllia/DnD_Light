from Game import *
from GameStart import *

@dlog()
def main():
    logo()
    greeting()
    next_thing()
    #
    print_player_classes()
    print_player_classes_description()
    next_thing()

    player = class_choice()

    next_thing()

    game = gen_desc_main_location()
    quests_desc = gen_desc_quests()

main()