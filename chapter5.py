def chapter_5(final_res):
    print("\n--- CHAPTER 5: THE SUNRISE ---")
    
    if final_res == "peaceful_win":
        print("The ice melts away. You return to Oakhaven as a legendary hero.")
    elif final_res == "chaotic_win":
        print("The storm is gone, but the mountainside is scarred forever.")
    else:
        print("The winter never ends. You returned home a failure.")
    
    print("\nThank you for playing Nordic Fantasy!")

if __name__ == "__main__":
    chapter_5("peaceful_win")