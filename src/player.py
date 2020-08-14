# Write a class to hold player information, e.g. what room they are in
# currently.

#github notes mvp 1 =
#Put the Player class in player.py.
#Players should have a name and current_room attributes

#Github notes MVP 2 =
#Make rooms able to hold multiple items
#Make the player able to carry multiple items
#Add items to the game that the user can carry around
from item import Item


class Player:
    def __init__(self, name, current_room, items= [] ):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.inventory = []

    def __str__(self):
        if self.inventory:
            result = f'Name: {self.name} is in {self.current_room} \n {self.current_room.description} Items are \n'
            for i in self.inventory:
                result += f'items names: {i.name} item description: {i.description} \n'
            return result

        else:
            return f"Name: {self.name} is in {self.current_room.name} \n {self.current_room.description}"       

    