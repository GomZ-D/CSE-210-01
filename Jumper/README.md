#Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

##Rules
*The puzzle is a secret word randomly chosen from a list.
*The player guesses a letter in the puzzle.
*If the guess is correct, the letter is revealed.
*If the guess is incorrect, a line is cut on the player's parachute.
*If the puzzle is solved the game is over.
*If the player has no more parachute the game is over.
## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Jumper             (source code for game)
  +-- game              (specific game classes)
    +-- director.py
    +-- graphic.py
    +-- terminal_server.py
    +-- word.py
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
  +-- README.md           (general info)
```

## Required Technologies
---
* Python 3.9.0

## Authors

*Diego Gomez (gom21026@byui.edu)