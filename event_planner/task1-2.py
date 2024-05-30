#Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))

venue = print("large hall" if attendees > 100 else "conference room")

print(venue)

print("="*50)

# Task 2:Catering Choices

dietary = input("Would you like vegetarian food:")

caterer = print("I'd reccomend our Veggie Delight Caterers!" if dietary == 'yes' else 'Thats okay! We have other options like our Gourmet Meals Caterers!')

print(caterer)