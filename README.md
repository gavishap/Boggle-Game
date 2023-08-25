
# Boggle Game

This is an implementation of the word game Boggle in Python using Tkinter for the graphical interface.


![image](https://github.com/gavishap/Boggle-Game/assets/71888304/c58b7691-0b70-423d-9f69-7be8a367941d)

## Overview

- Generates a random 4x4 Boggle board using a list of letter dice
- Allows the user to click on letters to form words
- Checks if user-created words are valid against a dictionary file
- Keeps track of score and time remaining

## Requirements

- Python 3
- Tkinter module

## Usage

Run `boggle.py` to start the game. A 4x4 board of random letters will be displayed. Click on adjoining letters to form words. When done, click the Submit button to submit the word. Valid words will be added to the score. An invalid word will produce an error message. 

The timer starts at 3 minutes. Try to find as many words as possible before time runs out!

## Implementation

- `boggle.py` - Main game GUI and logic
- `boggle_board_randomizer.py` - Generates random Boggle boards
- `boggle_dict.txt` - Dictionary of valid words  
- `ex11_utils.py` - Helper functions for finding words on board 

The board is represented as a 2D list of letters. The `select_letter` function tracks the sequence of clicked letters. `submit_word` checks the word against the dictionary and updates the score accordingly.

## Customizing

The valid word dictionary can be changed by modifying `boggle_dict.txt`. The board size, number of dice, and timer length can be adjusted by changing constants in `boggle.py` and `boggle_board_randomizer.py`.

## Credits

Boggle game idea and rules by Hasbro. Letter dice data from Wikipedia.
