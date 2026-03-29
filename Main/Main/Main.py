import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def start_adventure():
    print("--- NORDIC FANTASY: THE STORM BREAKER ---")
    
    # 1. Progression Variable
    has_passphrase = False

    # CHAPTER 1
    # call the function from the chapter1.py file
    status = chapter1.chapter_1()
    print(f"\nYou leave Oakhaven with the status: {status}")

    # CHAPTER 2
    # call the function from chapter2.py
    battle_result = chapter2.chapter_2()
    
    if battle_result == "dead":
        print("\nYour journey ends here. The wolves howl over the frozen tundra.")
        return # stops the game if lose

    # CHAPTER 3
    # check if the player gets secret item
    secret_outcome = chapter3.chapter_3()
    
    if secret_outcome == "has_passphrase":
        has_passphrase = True
        print("\n[ITEM ADDED]: You have memorized the ancient pass-phrase.")

    # CHAPTER 4
    # pass the 'has_passphrase' variable into Chapter 4
    # how Chapter 4 'knows' what you did in Chapter 3
    final_action = chapter4.chapter_4(has_passphrase)

    # CHAPTER 5
    # ending depends on the result of the final action
    chapter5.chapter_5(final_action)

# starts the game
if __name__ == "__main__":
    start_adventure()
