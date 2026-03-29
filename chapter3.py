def chapter_3():
    print("\n--- CHAPTER 3: THE JAGGED TOWER ---")
    print("An undead guardian sits upon a throne of ice, clutching a tablet.")
    print("1. Heal the guardian (Show Mercy)\n2. Attack the guardian\n3. Sneak past")
    
    choice = input("\nAction: ")
    if choice == "1":
        print("The guardian finds peace and whispers the words: 'Vento-Silex'.")
        return "has_passphrase" 
    elif choice == "2":
        print("You grab the tablet, but it is cracked and unreadable.")
        return "broken_tablet"
    else:
        print("You find a map, but the secret words remain a mystery.")
        return "map_only"

if __name__ == "__main__":
    chapter_3()