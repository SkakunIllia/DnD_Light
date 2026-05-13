from Auxiliary import *

#===================================================================================
# Functions
@dlog()
def initialize_entity(player_class, player_name):
    match player_class:
        case 1: return Archer(player_name)
        case 2: return Wizard(player_name)
        case 3: return Gnome(player_name)
        case 4: return Ogr(player_name)
        case 5: return Knight(player_name)
        case _: return Player(player_name, "Entity")

#===================================================================================
# Base classes
class Entity:
    def __init__(self, name):
        self._name = name
    def __repr__(self):
        return f'Entity[Name: {self._name}]'
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name)
        self._player_class = player_class
        self._items = []
        self._health = 100
        self._weapon = None
    def attack(self, obj):
        while obj.get_health() > 0:
            if random() < 30:
                self._health -= randint(10, 25)
            obj.set_health(obj.get_health() - self.get_weapon().get_damage())
    def __repr__(self):
        return f'Player[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def set_health(self, health):
        self._health = health
    def get_health(self):
        return self._health
    def set_items(self, items):
        self._items = items
    def get_items(self):
        return self._items
    def get_player_class(self):
        return self._player_class
    def get_weapon(self):
        return self._weapon
    def add_item(self, item):
        self._items.append(item)

#===================================================================================
# Player's classes
class Archer(Player):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.set_items([])
        self.set_health(80)
        self._weapon = Weapon("Relict bow", 65)
    def __repr__(self):
        return f'Archer {self._name}, {self._health}HP, items: {self._items if self._items != [] else "no items"}, weapon: {self._weapon}'

class Knight(Player):
    def __init__(self, name):
        super().__init__(name, "Knight")
        self.set_health(120)
        self.set_items([])
        self._weapon = Weapon("Silver sword", 45)
    def __repr__(self):
        return f'Knight {self._name}, {self._health}HP, items: {self._items if self._items != [] else "no items"}, weapon: {self._weapon}'

class Ogr(Player):
    def __init__(self, name):
        super().__init__(name, "Ogr")
        self.set_health(150)
        self.set_items([])
        self._weapon = Weapon("Greeny mace", 80)
    def __repr__(self):
        return f'Ogr {self._name}, {self._health}HP, items: {self._items if self._items != [] else "no items"}, weapon: {self._weapon}'

class Gnome(Player):
    def __init__(self, name):
        super().__init__(name, "Gnome")
        self.set_health(100)
        self.set_items([])
        self._weapon = Weapon("Gold pickaxe", 50)
    def __repr__(self):
        return f'Gnome {self._name}, {self._health}HP, items: {self._items if self._items != [] else "no items"}, weapon: {self._weapon}'

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, "Wizard")
        self.set_health(80)
        self.set_items([])
        self._weapon = Weapon("Magical wand", 60)
    def __repr__(self):
        return f'Wizard {self._name}, {self._health}HP, items: {self._items if self._items != [] else "no items"}, weapon: {self._weapon}'

#===================================================================================
# Mobs
class Mob(Player):
    def __init__(self, name):
        super().__init__(name, "Mob")
        self.set_health(randint(70, 150))
        self._damage = random()
    def __repr__(self):
        return f'Mob[Name: {self._name}, damage: {self._damage}, health: {self.get_health()}]'
    def get_damage(self):
        return self._damage
    def set_damage(self, damage):
        self._damage = damage

#===================================================================================
# Items and weapons
class Item:
    def __init__(self, name, type_of_item ="Item"):
        self._name = name
        self._type = type_of_item
    def __repr__(self):
        return f'Item[Name: {self._name}, type: {self._type}]'
    def get_type(self):
        return self._type
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def set_type(self, type_of_item):
        self._type = type_of_item

class Weapon(Item):
    def __init__(self, name, damage, type_of_item="Weapon"):
        super().__init__(name, type_of_item)
        self._damage = damage
    def __repr__(self):
        return f'{self._name}, damage: {self._damage}'
    def get_damage(self):
        return self._damage