def chapter_4(secret_key):
    print("\n--- CHAPTER 4: THE MOUNTAIN PEAK ---")
    print("A giant Steam Centurion guards the weather machine.")
    print("1. Speak the secret words\n2. Attack the Machine Core\n3. Attempt to deactivate manually")
    
    choice = input("\nFinal Action: ")
    
    if choice == "1":
        
        if secret_key == "has_passphrase":
            print("The Centurion bows. You shut down the machine peacefully.")
            return "peaceful_win"
        else:
            print("You don't know the words! The Centurion attacks.")
            return "failure"
    elif choice == "2":
        print("The core explodes, clearing the storm but destroying the peak.")
        return "chaotic_win"
    else:
        print("You failed to stop the machine in time.")
        return "failure"

if __name__ == "__main__":
    chapter_4("none")