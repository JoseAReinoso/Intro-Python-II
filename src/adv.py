from room import Room
from player import Player


# Declare all the rooms
#Dictionary of rooms mapping name to Room
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player = Player("Jose", room['outside'])
#setting up a default comman variable
command=''

#this is saying as long q word is not press it will run whats inside otherwise it will do the next code
while command != 'q':
     # GAME DIALOG # * Prints the current description (the textwrap module might be useful here).
    print(f"    Current player:   {player.name}")
    print(f"    Current Room:     {player.current_room.name}")
    # * Prints the current room name
    print(f"    Room Description: {player.current_room.description}")
 # PLAYER MOVEMENT AND COMMANDS
 # * Waits for user input and decides what to do.
 # MVP # 2 Add a new type of sentence the parser can understand: two words. example take drop etc etc.
    command = input('Please enter a command. Direction: [n] , [s] , [e] , [w]. Actions [drop] , [take] , [i] , [get] , [q] = quit the game: ')
    # Write a loop that:

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

    if command == 'n':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        else:
            print("You can not go here please try again")

    elif command  == 's':
        if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
    elif command == 'e':
        if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')
        
    elif command == 'w':
        if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
        else:
                print("You can not go here please try again!")
                input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')       


# If the user enters "q", quit the game.
 # Q TO QUIT THE GAME
    if command == 'q':
        print("You have exited the game.")
        break


 