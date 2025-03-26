#It is just a basic code about one piece and show the character names based on bounties and chacter names,speciality,danger level etc.
a = int(input("Enter the bounty of your character: "))
b = input("Enter the danger level of character: ").lower()
c = input("Enter the category of character: ").lower()
d = input("Enter the starting two letters of the character you want to find: ")
z = input("Enter the fruit name: ").lower()
e = input("Enter specific job only for Straw Hats: ").lower()

if 1_000_000 <= a <= 3_000_000 and b == "viceadmiral" and c == "fleet":
    if d == "Do":
        print("Fleet is Doberman")
    elif d == "Da":
        print("Fleet is Dalmatian")
    elif d == "Ho":
        print("Fleet is Hound")
    elif d == "To":
        print("Fleet is Tosa")
    elif d == "Po":
        print("Fleet is Pomsky")

elif a == 3_000_000_000 and b == "admiral":
    if z == "light fruit":
        print("Admiral is Kizaru")
    elif z == "gravity fruit":
        print("Admiral is Fujitora")

elif a == 5_000_000_000 and b == "admiral" 
    if z == "magma fruit":
    print("Admiral is Akainu")
    elif z=="short fruit"
    print("Muskan D. Rawat")

elif b == "strawhatpirates" and e.lower() == "captain":
    print("Pirate King (Monkey D. Luffy) uses Sun God fruit with the bounty of an Yonko of 3 billion berries")

elif b == "strawhatpirates" and e.lower() == "swordsman":
    print("Pirate is Pirate Hunter {Roronoa Zoro} - Pure strength and not a simp with a conquer bounty of 1.1 billion berries and thousand berries on top the second strongest in the crew")

elif b == "strawhatpirates" and e.lower() == "cook":
    print("The person who is going to find the All Blue (Vinsmoke Sanji) uses Darkstep for fighting and having bounty of 1 billion and 32 thousand berries")

elif b == "strawhatpirates" and e.lower() == "helmsman":
    print("The person is blue and it is (Jinbei) - Good in Water Kung Fu having bounty of 1.1 billion berries")

elif b == "strawhatpirates" and e.lower() == "archaeologist":
    print("It is {Nico Robin} - Lol easy guess bro with slimy bounty of 930 million berries")

elif b == "strawhatpirates" and e.lower() == "navigator":
    print("She just loves money so much (Nami) but captain comes first having bounty of 366 million")

elif b == "strawhatpirates" and e.lower() == "musician":
    print("Bro is the chillest person alive (Brook) and can also walk on water having a cold bounty of 383 million berries")

elif b == "strawhatpirates" and e.lower() == "god":
    print("None other than the (God D. Usopp) - Bro can solo his verse having a well deserved bounty of 5 million berries")

elif b == "strawhatpirates" and e.lower() == "shipwright":
    print("The shipwright of the ship (Franky) - SUPERRRRRRR!!! and having rocky bounty of 394 million berries")

elif b == "strawhatpirates" and e.lower() == "doctor":
    print("This is none other than (Tony Tony Chopper) - Need a heal? with a cutie bounty of 1 thousand berries")

else:
    print("Character not found. Check inputs.")

print(a, b, c, d, z, e)
    
