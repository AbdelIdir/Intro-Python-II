from room import Room
from player import Player
from item import Item

from colored import fg, bg, attr
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     " 🕳 North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """ 🌄 Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """ 🏔 A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """ 💰 The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """  💎 You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

backP = {
    'Knife': Item("Utility Knife",
                  "A do it all knife that can be used for many purposes. "),

    'Stick': Item("Stick", "Dry stick, can be used to start a fire. ")
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


room["foyer"].items.append("Knife")
room["foyer"].items.append("Dagger")
room["foyer"].items.append("Helmet")
room["outside"].items.append("Potion")
room["overlook"].items.append("Pickaxe")
room["narrow"].items.append("Chicken")
room['treasure'].items.append("Gold")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Luke", room["outside"])
# player1.backpack.append(backP["Knife"])

# for item in player1.backpack:
#     print(item)
# print(player1.backpack[0])

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

# for item in room:
# if item == Inputitem:
# player1.backpack.append
#


while playerKey != exitButton:
    playerKey = input("%sPlease enter a direction (n,s,e,w): %s" %
                      (fg(4), attr(0)))
    if playerKey == "n":
        if player1.current_room.n_to:
            player1.current_room = player1.current_room.n_to
            print(
                f"{player1.name} is in {player1.current_room.name}.\t {player1.current_room.description}   \n This room contains these items:\n  ")
            for item in player1.current_room.items:
                print(f"➡{item} \n")

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}")

            player_action = input(
                "What would you like to do with the items ? (Take/Drop): ")
            take_or_drop = player_action.split(" ")
            for index, item in enumerate(player1.current_room.items, start=0):
                if take_or_drop[0] == "take"and take_or_drop[1] == item:
                    player1.current_room.items.pop(index)
                    player1.backpack.append(item)
                    print(f"You picked up {item} into your backpack !")
            for index, item in enumerate(player1.backpack, start=0):
                if take_or_drop[0] == "drop"and take_or_drop[1] == item:
                    player1.backpack.pop(index)
                    player1.current_room.items.append(item)

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}\n")
            print("This 🚪room  now contain these items: \n")
            for item in player1.current_room.items:
                print(f"➡{item} \n")
        else:
            print("%sYou cannot go there ❌🚪%s" % (fg(1), attr(0)))
    elif playerKey == "s":
        if player1.current_room.s_to:
            player1.current_room = player1.current_room.s_to
            print(
                f"{player1.name} is in {player1.current_room.name}.\t {player1.current_room.description}   \n This room contains these items:\n  ")
            for item in player1.current_room.items:
                print(f"➡{item} \n")

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}")

            player_action = input(
                "What would you like to do with the items ? (Take/Drop): ")
            take_or_drop = player_action.split(" ")
            for index, item in enumerate(player1.current_room.items, start=0):
                if take_or_drop[0] == "take"and take_or_drop[1] == item:
                    player1.current_room.items.pop(index)
                    player1.backpack.append(item)
                    print(f"You picked up {item} into your backpack !")
            for index, item in enumerate(player1.backpack, start=0):
                if take_or_drop[0] == "drop"and take_or_drop[1] == item:
                    player1.backpack.pop(index)
                    player1.current_room.items.append(item)

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}\n")
            print("This 🚪room  now contain these items: \n")
            for item in player1.current_room.items:
                print(f"➡{item} \n")
        else:
            print("%sYou cannot go there ❌🚪%s" % (fg(1), attr(0)))
    elif playerKey == "e":
        if player1.current_room.e_to:
            player1.current_room = player1.current_room.e_to
            print(
                f"{player1.name} is in {player1.current_room.name}.\t {player1.current_room.description}   \n This room contains these items:\n  ")
            for item in player1.current_room.items:
                print(f"➡{item} \n")

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}")

            player_action = input(
                "What would you like to do with the items ? (Take/Drop): ")
            take_or_drop = player_action.split(" ")
            for index, item in enumerate(player1.current_room.items, start=0):
                if take_or_drop[0] == "take"and take_or_drop[1] == item:
                    player1.current_room.items.pop(index)
                    player1.backpack.append(item)
                    print(f"You picked up {item} into your backpack !")
            for index, item in enumerate(player1.backpack, start=0):
                if take_or_drop[0] == "drop"and take_or_drop[1] == item:
                    player1.backpack.pop(index)
                    player1.current_room.items.append(item)

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}\n")
            print("This 🚪room  now contain these items: \n")
            for item in player1.current_room.items:
                print(f"➡{item} \n")
        else:
            print("%sYou cannot go there ❌🚪%s" % (fg(1), attr(0)))
    elif playerKey == "w":
        if player1.current_room.w_to:
            player1.current_room = player1.current_room.w_to
            print(
                f"{player1.name} is in {player1.current_room.name}.\t {player1.current_room.description}   \n This room contains these items:\n  ")
            for item in player1.current_room.items:
                print(f"➡{item} \n")

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}")

            player_action = input(
                "What would you like to do with the items ? (Take/Drop): ")
            take_or_drop = player_action.split(" ")
            for index, item in enumerate(player1.current_room.items, start=0):
                if take_or_drop[0] == "take"and take_or_drop[1] == item:
                    player1.current_room.items.pop(index)
                    player1.backpack.append(item)
                    print(f"You picked up {item} into your backpack !")
            for index, item in enumerate(player1.backpack, start=0):
                if take_or_drop[0] == "drop"and take_or_drop[1] == item:
                    player1.backpack.pop(index)
                    player1.current_room.items.append(item)

            print("You have these items in your backpack 👜 : \n")
            for item in player1.backpack:
                print(f"➡{item}\n")
            print("This 🚪room  now contain these items: \n")
            for item in player1.current_room.items:
                print(f"➡{item} \n")
        else:
            print("%sYou cannot go there ❌🚪%s" % (fg(1), attr(0)))

    else:
        print(
            "%sType in a valid direction key: n,s,e,w%s" % (fg(1), attr(0)))
