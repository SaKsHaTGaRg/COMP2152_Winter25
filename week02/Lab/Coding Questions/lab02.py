import random

weapons = ["Use Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Elements: ", weapons)



# Roll dice
weaponRoll = random.randint(1, 6)
hero_combat_strength = weapons[weaponRoll - 1]

print(f"You rolled a {weaponRoll}. Your weapon is: {hero_combat_strength}")
try:
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