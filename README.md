# CSS225-Fantasy-Game
NORDIC FANTASY: TECHNICAL DOCUMENTATION

LANGUAGES & TECHNOLOGIES:
- Python 3.7+
- Modular Architecture (Multiple .py files)
- Object-Oriented Programming

SYSTEM REQUIREMENTS:
- Any OS with Python 3.7 installed.
- Terminal/Command Prompt access.

CODING CONVENTIONS:
- Variable Naming: snake_case
- Modules: One file per narrative chapter
- State Management: Use the Player class object for inventory and flag storage.

ARCHITECTURE OVERVIEW:
# Game runs using a Controller pattern, in which each frame is a new Controller created each frame in main.py. Here a simple Player is created.
The program traverses a series of modular steps, generating code in each one and eventually completing with an ending module, and in the fifth step it passes the created object as a reference.
(chapter1.py through chapter5.py).

HOW TO START THE GAME:
1. Make sure all .py files in the same directory.
2. Run 'python main.py' using Python application.
