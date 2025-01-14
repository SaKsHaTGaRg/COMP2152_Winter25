import random

weapons = ["Use Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Elements: ", weapons)

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue
try:
    weapon_selected = get_valid_int_input("Enter the index of the weapon you'd like to fight with : ")
    # Roll dice
    weaponRoll = random.randint(1, 6)
    hero_combat_strength = weapons[weaponRoll - 1]

    print(f"You rolled a {weaponRoll}. Your weapon is: {hero_combat_strength}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")
    if hero_combat_strength != "Use Fist":
            print("Thank goodness you didn't roll the Fist...")

except IndexError:
    print("Error: Invalid element index!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")