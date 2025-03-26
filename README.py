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

elif a == 3_000_000_000 and b == "admiral" and c == "fleet":
    if z == "light":
        print("Admiral is Kizaru")
    elif z == "gravity":
        print("Admiral is Fujitora")

elif a == 5_000_000_000 and b == "admiral" and c == "fleet" and z == "magma":
    print("Admiral is Akainu")

elif a == 3_000_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "captain":
    print("Pirate King (Monkey D. Luffy) uses Sun God fruit")

elif a == 1_100_001_100 and b == "strawhatpirates" and c == "pirate" and e.lower() == "swordsman":
    print("Pirate is Pirate Hunter {Roronoa Zoro} - Pure strength and not a simp")

elif a ==1_032_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "cook":
    print("The person who is going to find the All Blue (Vinsmoke Sanji) uses Darkstep for fighting")

elif a == 1_100_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "helmsman":
    print("The person is blue and it is (Jinbei) - Good in Water Kung Fu")

elif a == 930_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "archaeologist":
    print("It is {Nico Robin} - Lol easy guess bro")

elif a == 366_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "navigator":
    print("She just loves money so much (Nami) but captain comes first")

elif a == 383_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "musician":
    print("Bro is the chillest person alive (Brook) and can also walk on water")

elif a == 500_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "god":
    print("None other than the (God D. Usopp) - Bro can solo his verse")

elif a == 394_000_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "shipwright":
    print("The shipwright of the ship (Franky) - SUPERRRRRRR!!!")

elif a == 1_000 and b == "strawhatpirates" and c == "pirate" and e.lower() == "doctor":
    print("This is none other than (Tony Tony Chopper) - Need a heal?")

else:
    print("Character not found. Check inputs.")

print(a, b, c, d, z, e)
    
