import json

# Initialize empty list to store places
places = []

# Prompt the user to enter a place
while True:
    place = input("Enter a place (or 'q' to quit): ")
    
    if place.lower() == 'q':  # Ensures 'q' works regardless of case
        break
    
    places.append(place)

# Convert list to JSON object
places_json = json.dumps(places)

# Display all places
print("All places entered:")
print(places_json)
