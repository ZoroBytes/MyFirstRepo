# Taking user inputs
a = int(input("Enter the bounty of your character: "))
b = input("Enter the danger level of character: ").lower()
c = input("Enter the category of character: ").lower()
d = input("Enter the starting two letters of the character you want to find: ").lower()
z = input("Enter the fruit name: ").lower()
e = input("Enter specific job only for Straw Hats: ").lower()

# Fleet Vice Admirals
if 1_000_000 <= a <= 3_000_000 and b == "viceadmiral" and c == "fleet":
    if d == "do":
        print("Fleet is Doberman")
    elif d == "da":
        print("Fleet is Dalmatian")
    elif d == "ho":
        print("Fleet is Hound")
    elif d == "to":
        print("Fleet is Tosa")
    elif d == "po":
        print("Fleet is Pomsky")
    else:
        print("Fleet character not found.")

# Admirals
elif a == 3_000_000_000 and b == "admiral":
    if z == "light fruit":
        print("Admiral is Kizaru")
    elif z == "gravity fruit":
        print("Admiral is Fujitora")
    else:
        print("No matching Admiral found.")

elif a == 5_000_000_000 and b == "admiral":
    if z == "magma fruit":
        print("Admiral is Akainu")
    elif z == "short fruit":
        print("Muskan D. Rawat")  # this is intentional
    else:
        print("No matching Admiral found.")

# Straw Hat Pirates
elif 1000<=a<=3_000_000_000 and b == "strawhatpirates" and c=="pirate":
    if e == "captain":
        print("Pirate King (Monkey D. Luffy) uses Sun God fruit with a Yonko bounty of 3 billion berries.")
    elif e == "swordsman":
        print("Pirate Hunter Roronoa Zoro - A conqueror with a bounty of 1.1 billion berries, second strongest in the crew.")
    elif e == "cook":
        print("Vinsmoke Sanji - Darkstep fighter, bounty: 1 billion and 32 thousand berries.")
    elif e == "helmsman":
        print("Jinbei - Water Kung Fu expert, bounty: 1.1 billion berries.")
    elif e == "archaeologist":
        print("Nico Robin - Easy guess, bounty: 930 million berries.")
    elif e == "navigator":
        print("Nami - Loves money, but captain comes first. Bounty: 366 million berries.")
    elif e == "musician":
        print("Brook - The chillest person, walks on water. Bounty: 383 million berries.")
    elif e == "god":
        print("God D. Usopp - Can solo his verse. Bounty: 5 million berries.")
    elif e == "shipwright":
        print("Franky - SUPERRRRR!!! Bounty: 394 million berries.")
    elif e == "doctor":
        print("Tony Tony Chopper - Need a heal? Cutie bounty: 1 thousand berries.")
    else:
        print("Straw Hat crew position not found.")
        
else:
    print("Character not found. Check inputs.")

# Printing the input values for reference
print(a, b, c, d, z, e)
