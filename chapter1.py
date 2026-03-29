def chapter_1(hero):
    print(f"\n--- CHAPTER 1: THE VILLAGE OF OAKHAVEN ---")
    print(f"The traveler {hero.name} enters the tavern...")
    print("The sky is bruised purple, and the air smells of ozone.")
    print("You arrive at the local tavern looking for the 'Mountain Heart'.")
    print("1. Consult the Village Elder\n2. Gather supplies from the Blacksmith\n3. Leave immediately")
    
    choice = input("\nYour move: ")
    if choice == "1":
        print("The Elder tells you: 'Seek the guardian in the tower for the secret words.'")
        return "informed"
    elif choice == "2":
        print("The Blacksmith gives you a heavy cloak and a sturdy blade.")
        return "supplied"
    else:
        print("You head north into the biting wind.")
        return "rushed"

if __name__ == "__main__":
    chapter_1()