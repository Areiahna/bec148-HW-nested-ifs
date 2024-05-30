# Task 2: Setting the Scene..

#Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if (place == "forest"):
        action = input("climb a tree or cross a river?")
        if (action == "climb a tree"):
            print("You found a bird's nest!")
        else:
            action = "cross a river"
            print("You found a boat!")
else:
    place = "cave"
    action = input("Would you like to lit a torch or proceed in the dark? Enter 'lit' for torch or 'dark' to proceed.")
    if(action == "lit"):
        print("Lets explore the cave!")
    else:
        print("I hope you packed night vivion goggles!")
