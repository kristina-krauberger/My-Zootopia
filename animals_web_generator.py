import json

def load_data(file_path):
    """Load JSON file"""
    with open(file_path,"r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
#print(animals_data)

# Name: American Foxhound
# Diet: Omnivore
# Location: North-America
# Type: Hound


def show_info(animals_data):

    for animal in animals_data:
        print(f"Name: {animal.get("name")}")
        print(f"Diet: {animal.get("characteristics").get("diet")}")
        print(f"Location: {animal.get("locations")[0]}")
        #print(f"Location: {", ".join(animal["locations"])}")    #split ist string → liste und join ist liste → string
        print(f"Type: {animal.get("characteristics").get("type")}")
        print()

show_info(animals_data)

