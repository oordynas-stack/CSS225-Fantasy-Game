def chapter_4(passphrase_status):
    print("\n--- CHAPTER 4: THE MOUNTAIN PEAK ---")
    print("Massive bronze gears grind inside the peak. A Steam Centurion stands guard.")
    print("\n1. Use Pass-phrase (If you have it)")
    print("2. Destroy Core: Attack the machine directly.")
    print("3. Retreat: Run back to the safety of the woods.")
    
    choice = input("\nWhat is your final move? (1/2/3): ")
    
    if choice == "1":
        if passphrase_status == "has_passphrase":
            print("\n[SUCCESS] You speak the ancient words. The machine hums and shuts down.")
            return "peaceful_victory"
        else:
            print("\n[FAILURE] You try to speak, but you don't know the words. The Centurion attacks!")
            return "defeat"
    elif choice == "2":
        print("\n[OUTCOME] You shatter the core. A blinding flash of gold erupts!")
        return "chaotic_victory"
    else:
        print("\n[OUTCOME] You lose your nerve and run back down the mountain.")
        return "retreat"

if __name__ == "__main__":
    chapter_4("none")
