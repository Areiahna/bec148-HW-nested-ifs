#Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print("Your venue will be held in our:", venue)

print("="*50)
