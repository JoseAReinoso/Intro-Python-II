# Implement a class to hold room information. This should have name and
# description attributes.

#github notes mvp 1 =
# Put the Room class in room.py based on what you see in adv.py.
# The room should have name and description attributes.
# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

#github notes mvp 2 =
# Make rooms able to hold multiple items

from item import Item


class Room:
    # MVP2 = The Room class should be extended with a list that holds the Items that are currently in that room.
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description =description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        #MVP 2 =Add functionality to the main loop that prints out all the items that are visible to the 
        # player when they are in that room.
        if self.items:
            result = f'this is {self.name} and has {self.description}. The items are\n'

            for i in self.items:
                result += f'item name: {i.name} item Description: {i.description} \n'
                return result
        else:
            return f'this is room {self.name} has its {self.description}'
     #Following will be methods=        

    def list_items(self):
        print(self.items)

#MVP 2 = Add the ability to add items to rooms.
    def add_item(self, item):
        self.items.append(item)
        return True
#MVP 2 = Add the ability to remove items to rooms.
    def remove_item_from_room(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return False      