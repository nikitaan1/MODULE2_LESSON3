#Task 1

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2

attendees = int(input("Enter number of attendees: "))


venue = "large hall" if attendees > 100 else "conference room"
print(venue)

sound_system = "audio system" if attendees > 500 else "projector"
print(sound_system)

#Task 3

attendees = int(input("Enter number of attendees: "))
vegeterian_food = True


venue = "large hall" if attendees > 100 else "conference room"
print(venue)

sound_system = "audio system" if attendees > 500 else "projector"
print(sound_system)

print("Veggie Delight Caterers") if vegeterian_food else "Gourmet Meals Caterers"