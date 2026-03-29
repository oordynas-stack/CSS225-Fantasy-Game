def chapter_3():
    print("\n--- CHAPTER 3: THE JAGGED TOWER ---")
    print("A crumbling tower looms over the pass. Inside, an undead guardian sits.")
    print("It clutches an ancient stone tablet and moans in eternal pain.")
    print("\n1. Show Mercy: Use a healing prayer on the guardian.")
    print("2. Loot the Body: Try to pry the tablet from its cold hands.")
    print("3. Search the Ruins: Look for another way around.")
    
    choice = input("\nHow do you proceed? (1/2/3): ")
    
    if choice == "1":
        print("\n[PROGRESSION] The guardian finds peace. It whispers a PASS-PHRASE before crumbling.")
        return "has_passphrase"
    elif choice == "2":
        print("\n[RESULT] You trigger a poison trap! You grab the tablet but feel weak.")
        return "injured"
    else:
        print("\n[RESULT] You find a hidden map that bypasses the guardian entirely.")
        return "map"

if __name__ == "__main__":
    chapter_3()