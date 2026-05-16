import os, json

# Save Creater
def save(player):
    save_title = input("How would you like to name the save file? ")
    save_dir = "saves"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    path = save_title + ".json"
    save_file = os.path.join(save_dir, path)
    # to be continued

# Save Loader
def load(save_file):
    pass
    # to be continued