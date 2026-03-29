import chapter1, chapter2, chapter3, chapter4, chapter5
from player import Player

def start_game():
    print("--- NORDIC FANTASY: THE STORM BREAKER ---")
    
    name_input = input("Enter your hero's name: ")
    hero = Player(name_input)
    
    # Chapter 1
    chapter1.chapter_1(hero)
    
    # Chapter 2 
    res2 = chapter2.chapter_2(hero)
    if res2 == "dead":
        print(f"\n{hero.name} has fallen. Game Over.")
        return

    # Chapter 3
    secret_key = chapter3.chapter_3() 

    # Chapter 4
    final_res = chapter4.chapter_4(secret_key)

    # Chapter 5 - Final Ending
    chapter5.chapter_5(final_res)

if __name__ == "__main__":
    start_game()