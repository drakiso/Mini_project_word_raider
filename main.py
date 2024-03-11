"""This project is about creating a word guess game.
The program randomly select a word from a list of word and the player have to
guess to chose word. The player has 5 tries maximum."""

import random

# keeps the name of the game
game_name = "word"

# read the file that contains all the words
# assign all the words in variable word_bank as a list
file = open("words.txt")
word_bank = file.readlines()

# remove the spaces at the beginning and end of each word.
word_bank = [word.strip().lower() for word in word_bank]

# random word, that the player will have to guess
random_word = random.choice(word_bank)

# letters the player has guessed that are in the incorrect (misplaced) location
misplaced_letter = []

# letters the player has guessed that are not in the word
incorrect_letter = []

# Maximum number of turns that are allowed
max_turns = 5

# Current number of turns the player has taken
current_turn = 1

print(f"Welcome to our {game_name} game. \n"
      f"The word to guess contains {len(random_word)} letters. \n"
      f"You have {max_turns} tries.")

while max_turns > 0:
    print(f"turn {current_turn}")
    guessed_word = input("\nEnter your word:    ").strip().lower()

    if guessed_word.isalpha() and len(guessed_word) == len(random_word):
        letter_index = 0

        if guessed_word == random_word:
            print(guessed_word)
            print("Houra you guessed the word")
            break
        else:
            for letter in guessed_word:
                if letter == random_word[letter_index]:
                    if letter in misplaced_letter:
                        misplaced_letter.remove(letter)
                    print(letter, end='')
                elif letter in random_word:
                    if letter not in misplaced_letter:
                        misplaced_letter.append(letter)
                    print("_", end='')
                else:
                    if letter not in incorrect_letter:
                        incorrect_letter.append(letter)
                    print("_", end='')

                letter_index += 1

            print(f"\nLetter you guessed but in the wrong position:", *misplaced_letter)
    else:
        print(f"{guessed_word} is not correct.")

    max_turns -= 1
    current_turn += 1

    if max_turns == 0:
        print("You lost")
    else:
        print(f"You have {max_turns} turns left")
