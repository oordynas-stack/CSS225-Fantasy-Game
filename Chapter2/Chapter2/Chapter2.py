import random

def chapter_2():
    print("\n--- CHAPTER 2: THE TWILIGHT WOODS ---")
    print("A pack of Frost-Wolves led by a spectral Alpha surrounds you.")
    print("1. Fight")
    print("2. Use Magic")
    print("3. Climb")
    
    action = input("\nChoose (1/2/3): ")
    
    if action == "1":
        if random.randint(1, 10) > 4:
            print("WIN: You defeat the Alpha!")
            return "win"
        else:
            print("LOSS: Game Over.")
            return "dead"
    else:
        print("You move toward the tower.")
        return "next"

chapter_2()
