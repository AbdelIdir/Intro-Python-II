from room import Room
from player import Player

# Declare all the rooms

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


room["foyer"].items.append("hi")
room["outside"].items.append("yo")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Luke", room["outside"])

# print(player1)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


playerKey = ""
exitButton = "q"

while playerKey != exitButton:
    playerKey = input("Please enter a direction (n,s,e,w): ")
    if playerKey == "n":
        if player1.current_room.n_to:
            player1.current_room = player1.current_room.n_to
            print(f"{player1.name} is in {player1.current_room}. These items are available in this room:{player1.current_room.items}")
        else:
            print("You cannot go there")
    if playerKey == "s":
        if player1.current_room.s_to:
            player1.current_room = player1.current_room.s_to
            print(f"{player1.name} is in {player1.current_room} These items are available in this room:{player1.current_room.items}")
        else:
            print("You cannot go there")
    if playerKey == "e":
        if player1.current_room.e_to:
            player1.current_room = player1.current_room.e_to
            print(f"{player1.name} is in {player1.current_room} These items are available in this room:{player1.current_room.items}")
        else:
            print("You cannot go there")
    if playerKey == "w":
        if player1.current_room.w_to:
            player1.current_room = player1.current_room.w_to
            print(f"{player1.name} is in {player1.current_room} These items are available in this room:{player1.current_room.items}")
        else:
            print("You cannot go there")
    else:
        print(
            "Type in a valid direction key: n,s,e,w")
