
attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print("Your venue will be held in our:", venue)

print("="*50)

# Task 2: Venue Selection

selection = print("I'd like to recommend the use of our projector screens for your venue selection" if venue =='conference room' else "I'd recommend the use of our surround sound audio system for your venue selection")
