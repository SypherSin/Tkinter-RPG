import json
from tkinter import Tk, Label, Button, OptionMenu, StringVar

window = Tk()
window.title("Character Creation")

# Available options for race and class
races = {
    "Human": {"Strength": 10, "Dexterity": 10, "Constitution": 10},
    "Elf": {"Strength": 8, "Dexterity": 12, "Constitution": 8},
    "Dwarf": {"Strength": 12, "Dexterity": 8, "Constitution": 12}
}

classes = {
    "Warrior": {"Strength": 12, "Dexterity": 10, "Constitution": 12},
    "Mage": {"Strength": 8, "Dexterity": 10, "Constitution": 8},
    "Rogue": {"Strength": 10, "Dexterity": 12, "Constitution": 10}
}

# Variables to store the selected race, class, and character details
selected_race = StringVar()
selected_class = StringVar()
character_details = {
    "Race": "",
    "Class": "",
    "Stats": {}
}

# Function to handle the selection of race
def race_selected(*args):
    race = selected_race.get()
    character_details["Race"] = race
    update_stats(races[race])

# Function to handle the selection of class
def class_selected(*args):
    character_class = selected_class.get()
    character_details["Class"] = character_class
    update_stats(classes[character_class])

# Function to update the character's stats
def update_stats(stats):
    character_details["Stats"] = stats
    print("Updated stats:", character_details["Stats"])

# Create the dropdown menu for race
race_label = Label(window, text="Race:")
race_label.grid(row=0, column=0, padx=10, pady=10)
race_dropdown = OptionMenu(window, selected_race, *races.keys(), command=race_selected)
race_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Create the dropdown menu for class
class_label = Label(window, text="Class:")
class_label.grid(row=1, column=0, padx=10, pady=10)
class_dropdown = OptionMenu(window, selected_class, *classes.keys(), command=class_selected)
class_dropdown.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()

# Save character details to a JSON file
filename = "tkintertest/raceandclass.json"
with open(filename, "w") as file:
    json.dump(character_details, file, indent=4)

print(f"Character details saved to {filename}")