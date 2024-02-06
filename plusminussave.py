import json
from tkinter import Tk, Label, Button

window = Tk()
window.title("Character Stats")

strength = 10
dexterity = 10
constitution = 10
intelligence = 10
wisdom = 10
charisma = 10

max_strength = 18
max_dexterity = 18
max_constitution = 18
max_intelligence = 18
max_wisdom = 18
max_charisma = 18

total_stat_points = 30

def save_stats():
    with open("tkintertest/stats.json", "w") as file:
        json.dump({
            "Strength": strength,
            "Dexterity": dexterity,
            "Constitution": constitution,
            "Intelligence": intelligence,
            "Wisdom": wisdom,
            "Charisma": charisma
        }, file, indent=4)

    window.destroy()

def increase_stat(stat):
    global strength, dexterity, constitution, intelligence, wisdom, charisma, total_stat_points
    if total_stat_points > 0:
        if stat == "strength":
            if strength < max_strength:
                strength += 1
                total_stat_points -= 1
       
        if stat == "dexterity":
            if dexterity < max_dexterity:
                dexterity += 1
                total_stat_points -= 1
                
        if stat == "constitution":
            if constitution < max_constitution:
                constitution += 1
                total_stat_points -= 1
                
        if stat == "intelligence":
            if intelligence < max_intelligence:
                intelligence += 1
                total_stat_points -= 1
                
        if stat == "wisdom":
            if wisdom < max_wisdom:
                wisdom += 1
                total_stat_points -= 1
                
        if stat == "charisma":
            if charisma < max_charisma:
                charisma += 1
                total_stat_points -= 1
                
    update_labels()

def decrease_stat(stat):
    global strength, dexterity, constitution, intelligence, wisdom, charisma, total_stat_points
    if stat == "strength":
        if strength > 0:
            strength -= 1
            total_stat_points += 1
            
    if stat == "dexterity":
        if dexterity > 0:
            dexterity -= 1
            total_stat_points += 1

    if stat == "constitution":
        if constitution > 0:
            constitution -= 1
            total_stat_points += 1
            
    if stat == "intelligence":
        if intelligence > 0:
            intelligence -= 1
            total_stat_points += 1
    
    if stat == "wisdom":
        if wisdom > 0:
            wisdom -= 1
            total_stat_points += 1
            
    if stat == "charisma":
        if charisma > 0:
            charisma -= 1
            total_stat_points += 1
            
    update_labels()
    
def update_labels():
    strength_label.config(text=f"Strength: {strength}/{max_strength}")
    dexterity_label.config(text=f"Dexterity: {dexterity}/{max_dexterity}")
    constitution_label.config(text=f"Constitution: {constitution}/{max_constitution}")
    intelligence_label.config(text=f"Intelligence: {intelligence}/{max_intelligence}")
    wisdom_label.config(text=f"Wisdom: {wisdom}/{max_wisdom}")
    charisma_label.config(text=f"Charisma: {charisma}/{max_charisma}")
    stat_points_label.config(text=f"Stat Points: {total_stat_points}")

strength_label = Label(window, text=f"Strength: {strength}/{max_strength}")
strength_label.grid(row=0, column=0, padx=10, pady=10)

dexterity_label = Label(window, text=f"Dexterity: {dexterity}/{max_dexterity}")
dexterity_label.grid(row=1, column=0, padx=10, pady=10)

constitution_label = Label(window, text=f"Constitution: {constitution}/{max_constitution}")
constitution_label.grid(row=2, column=0, padx=10, pady=10)

intelligence_label = Label(window, text=f"Intelligence: {intelligence}/{max_intelligence}")
intelligence_label.grid(row=3, column=0, padx=10, pady=10)

wisdom_label = Label(window, text=f"Wisdom: {wisdom}/{max_wisdom}")
wisdom_label.grid(row=4, column=0, padx=10, pady=10)

charisma_label = Label(window, text=f"Charisma: {charisma}/{max_charisma}")
charisma_label.grid(row=5, column=0, padx=10, pady=10)

stat_points_label = Label(window, text=f"Stat Points: {total_stat_points}")
stat_points_label.grid(row=6, column=0, padx=10, pady=10)

strength_plus_button = Button(window, text="+", command=lambda: increase_stat("strength"))
strength_plus_button.grid(row=0, column=1, padx=10, pady=10)

strength_minus_button = Button(window, text="-", command=lambda: decrease_stat("strength"))
strength_minus_button.grid(row=0, column=2, padx=10, pady=10)

dexterity_plus_button = Button(window, text="+", command=lambda: increase_stat("dexterity"))
dexterity_plus_button.grid(row=1, column=1, padx=10, pady=10)

dexterity_minus_button = Button(window, text="-", command=lambda: decrease_stat("dexterity"))
dexterity_minus_button.grid(row=1, column=2, padx=10, pady=10)

constitution_plus_button = Button(window, text="+", command=lambda: increase_stat("constitution"))
constitution_plus_button.grid(row=2, column=1, padx=10, pady=10)

constitution_minus_button = Button(window, text="-", command=lambda: decrease_stat("constitution"))
constitution_minus_button.grid(row=2, column=2, padx=10, pady=10)

intelligence_plus_button = Button(window, text="+", command=lambda: increase_stat("intelligence"))
intelligence_plus_button.grid(row=3, column=1, padx=10, pady=10)

intelligence_minus_button = Button(window, text="-", command=lambda: decrease_stat("intelligence"))
intelligence_minus_button.grid(row=3, column=2, padx=10, pady=10)

wisdom_plus_button = Button(window, text="+", command=lambda: increase_stat("wisdom"))
wisdom_plus_button.grid(row=4, column=1, padx=10, pady=10)

wisdom_minus_button = Button(window, text="-", command=lambda: decrease_stat("wisdom"))
wisdom_minus_button.grid(row=4, column=2, padx=10, pady=10)

charisma_plus_button = Button(window, text="+", command=lambda: increase_stat("charisma"))
charisma_plus_button.grid(row=5, column=1, padx=10, pady=10)

charisma_minus_button = Button(window, text="-", command=lambda: decrease_stat("charisma"))
charisma_minus_button.grid(row=5, column=2, padx=10, pady=10)

save_button = Button(window, text="Save", command=save_stats)
save_button.grid(row=7, column=0, padx=10, pady=10)

window.mainloop()