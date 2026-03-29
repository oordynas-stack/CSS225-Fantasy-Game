import random

def chapter_1():
    print("\n--- CHAPTER 1: OAKHAVEN ---")
    print("It is a cold night, and the rain sweeps in from the west...")
    print("1. Interact with locals")
    print("2. Take on tasks")
    print("3. Search the north")
    
    choice = input("\nWhat is your move? (1/2/3): ")
    
    if choice == "1":
        print("OUTCOME: You learn about the 'Mountain Heart'.")
        return "informed"
    elif choice == "2":
        print("OUTCOME: You earn enough coins for extra rations.")
        return "supplied"
    else:
        print("You leave the village behind.")
        return "move_on"

chapter_1()