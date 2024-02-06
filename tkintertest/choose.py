import tkinter as tk
import json

from tkinter import messagebox

#--------------------------------------------------------------------------

def save_name(window, nameentry1, nameentry2, nameentry3, nameentry4):
    # Get the value from the entry widget
    character_name_first = nameentry1.get()
    character_name_last = nameentry2.get()
    character_name_nickname = nameentry3.get()
    character_name_secret = nameentry4.get()

    with open("tkintertest/name.json", "w") as file:
        json.dump({
            "First Name": character_name_first,
            "Last Name": character_name_last,
            "Nickname": character_name_nickname,
            "Secret Name": character_name_secret
        }, file, indent=4)

    # Clear the entry widget
    nameentry1.delete(0, tk.END)
    nameentry2.delete(0, tk.END)
    nameentry3.delete(0, tk.END)
    nameentry4.delete(0, tk.END)

    # Destroy the current window
    window.destroy()

    # Open the Choose Stats screen
    choose_stats_screen()

#--------------------------------------------------------------------------

def choose_name_screen():
    # Create the tkinter window
    window = tk.Tk()

    # Create the widgets for the "Choose Name" screen
    namelabel1 = tk.Label(window, text="First Name", width=30)
    namelabel1.grid(row=0, column=0, padx=10, pady=10)

    nameentry1 = tk.Entry(window)
    nameentry1.grid(row=1, column=0, padx=10, pady=10)

    namelabel2 = tk.Label(window, text="Last Name", width=30)
    namelabel2.grid(row=2, column=0, padx=10, pady=10)

    nameentry2 = tk.Entry(window)
    nameentry2.grid(row=3, column=0, padx=10, pady=10)

    namelabel3 = tk.Label(window, text="Nickname", width=30)
    namelabel3.grid(row=4, column=0, padx=10, pady=10)

    nameentry3 = tk.Entry(window)
    nameentry3.grid(row=5, column=0, padx=10, pady=10)

    namelabel4 = tk.Label(window, text="Secret Name", width=30)
    namelabel4.grid(row=6, column=0, padx=10, pady=10)

    nameentry4 = tk.Entry(window)
    nameentry4.grid(row=7, column=0, padx=10, pady=10)

    namebutton = tk.Button(window, text="Save Name", command=lambda: save_name(window, nameentry1, nameentry2, nameentry3, nameentry4))
    namebutton.grid(row=8, column=0, padx=10, pady=10)

    # Start the tkinter event loop
    window.mainloop()

#--------------------------------------------------------------------------

def save_stats(window, statentry1, statentry2, statentry3, statentry4, statentry5, statentry6):
    # Get the value from the entry widget
    character_strength = int(statentry1.get())
    character_dexterity = int(statentry2.get())
    character_constitution = int(statentry3.get())
    character_intelligence = int(statentry4.get())
    character_wisdom = int(statentry5.get())
    character_charisma = int(statentry6.get())

    # Set the desired total stat points
    desired_total_stat_points = 20

    # Calculate the total sum of the entered stats
    total_stat_points = (
        character_strength
        + character_dexterity
        + character_constitution
        + character_intelligence
        + character_wisdom
        + character_charisma
    )

    # Calculate the remaining points
    remaining_points = desired_total_stat_points - total_stat_points

    # Update the remaining points label
    remaining_points_label.config(text="Remaining Points: {}".format(remaining_points))

    # Check if the total sum exceeds the desired total
    if total_stat_points > desired_total_stat_points:
        # Display an error message and return without saving
        error_message = "Total stat points cannot exceed {}".format(desired_total_stat_points)
        tk.messagebox.showerror("Error", error_message)
        return

    # Create a dictionary to store the input
    data = {
        "Strength": character_strength,
        "Dexterity": character_dexterity,
        "Constitution": character_constitution,
        "Intelligence": character_intelligence,
        "Wisdom": character_wisdom,
        "Charisma": character_charisma
    }

    # Save the input to a JSON file
    with open("tkintertest/stats.json", "w") as file:
        json.dump(data, file, indent=4)

    # Clear the entry widgets
    statentry1.delete(0, tk.END)
    statentry2.delete(0, tk.END)
    statentry3.delete(0, tk.END)
    statentry4.delete(0, tk.END)
    statentry5.delete(0, tk.END)
    statentry6.delete(0, tk.END)

    # Destroy the current window
    window.destroy()

#--------------------------------------------------------------------------

def choose_stats_screen():
    # Create the tkinter window
    window = tk.Tk()

    # Destroy the Choose Name window (if it exists)
    for widget in window.winfo_children():
        widget.destroy()

    # Create the widgets for the "Choose Stats" screen
    statlabel1 = tk.Label(window, text="Strength", width=30)
    statlabel1.grid(row=0, column=0, padx=10, pady=10)

    statentry1 = tk.Entry(window)
    statentry1.grid(row=1, column=0, padx=10, pady=10)

    statlabel2 = tk.Label(window, text="Dexterity", width=30)
    statlabel2.grid(row=2, column=0, padx=10, pady=10)

    statentry2 = tk.Entry(window)
    statentry2.grid(row=3, column=0, padx=10, pady=10)

    statlabel3 = tk.Label(window, text="Constitution", width=30)
    statlabel3.grid(row=4, column=0, padx=10, pady=10)

    statentry3 = tk.Entry(window)
    statentry3.grid(row=5, column=0, padx=10, pady=10)

    statlabel4 = tk.Label(window, text="Intelligence", width=30)
    statlabel4.grid(row=6, column=0, padx=10, pady=10)

    statentry4 = tk.Entry(window)
    statentry4.grid(row=7, column=0, padx=10, pady=10)

    statlabel5 = tk.Label(window, text="Wisdom", width=30)
    statlabel5.grid(row=8, column=0, padx=10, pady=10)

    statentry5 = tk.Entry(window)
    statentry5.grid(row=9, column=0, padx=10, pady=10)

    statlabel6 = tk.Label(window, text="Charisma", width=30)
    statlabel6.grid(row=10, column=0, padx=10, pady=10)

    statentry6 = tk.Entry(window)
    statentry6.grid(row=11, column=0, padx=10, pady=10)

    statbutton = tk.Button(
        window,
        text="Choose Stats",
        command=lambda: save_stats(
            window,
            statentry1,
            statentry2,
            statentry3,
            statentry4,
            statentry5,
            statentry6
        )
    )
    statbutton.grid(row=12, column=0, padx=10, pady=10)

    # Create a label to display the remaining points
    remaining_points_label = tk.Label(window, text="Remaining Points", width=30)
    remaining_points_label.grid(row=13, column=0, padx=10, pady=10)

    # Start the tkinter event loop
    window.mainloop()

#--------------------------------------------------------------------------

# Open the Choose Name screen
choose_name_screen()