def chapter_5(final_outcome):
    print("\n--- CHAPTER 5: THE AFTERMATH ---")
    
    if final_outcome == "peaceful_victory":
        print("The storm clears gently. The locals hail you as 'Storm-Breaker'.")
    elif final_outcome == "chaotic_victory":
        print("The storm is gone, but the peak is destroyed. You survived a miracle.")
    else:
        print("The blizzard continues to rage. You returned home a failure.")
    
    print("\nYour journey has concluded. Thank you for playing.")

if __name__ == "__main__":
    chapter_5("peaceful_victory")
