import random

def chapter_2(hero):
    print("\n--- CHAPTER 2: THE TWILIGHT WOODS ---")
    print("Frost-Wolves emerge from the shadows, led by a massive Alpha.")
    print("1. Stand and Fight\n2. Use a Flame Spell\n3. Hide in the ruins")
    
    choice = input("\nAction: ")
    if choice == "1":
        # Random logic for the battle outcome
        if random.randint(1, 10) > 4:
            print("VICTORY: You slay the Alpha and the pack scatters!")
            return "survived"
        else:
            return "dead" # This triggers the 'Game Over' in main.py
    elif choice == "2":
        print("The flames clear a path through the trees.")
        return "survived"
    else:
        print("You lose your supplies but manage to escape.")
        return "survived"

if __name__ == "__main__":
    chapter_2()