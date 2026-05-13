from functools import wraps
from re import match, sub
from Logger import dlog, logger
from time import sleep
from random import randint

# Logo
@dlog("printing the logo's separator")
def logo():
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
    sleep(delay_time)
    print("=================================================")

# Separator
@dlog()
def separator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("====================================")
        return func(*args, **kwargs)
    return wrapper

# Global variables:
delay_time = 10

# Randomising value for the quest to be completed,
# if the value of the player's 'luck' is higher than
# the value it means that the quest has to be completed
def random():
    return randint(randint(10, 20), randint(50, 70))

# Functions:
@dlog("verifying whether the answer is positive")
def verify_answer(string):
    return match("Yes|yes|aha|Sure|OK|yeah|Yeah|y|Y|yep|Yep", sub(" ", "", string))

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



