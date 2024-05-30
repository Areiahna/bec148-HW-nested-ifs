# Task 3: Default Path

# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

place = input("Choose a place: forest or cave? ")

if (place == "forest"):
        action = input("climb a tree or cross a river?")
        if (action == "climb a tree"):
            print("You found a bird's nest!")
        elif (action == "cross a river"):
            print("You found a boat!")
        else: 
            pass

elif (place == "cave"):
    action = input("Would you like to lit a torch or proceed in the dark? Enter 'lit' for torch or 'dark' to proceed.")
    if(action == "lit"):
        print("Lets explore the cave!")
    elif (action == 'dark'):
        print("I hope you packed night vivion goggles!")
    else:
        pass

else:
    pass
