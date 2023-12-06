from random import choice
from stages import stages_, logo
from words import words_


"""This program is based on the infamous hangman game."""

print(logo)
# Declare and assign lives, list of words, a random choice and the word length
lives_left = 6
chosen_word = choice(words_)
word_length = len(chosen_word)

# display code
display = ["_" for letter in chosen_word]

# ask user for a guess till they guess it all
while "_" in display:
    guess = input("Guess a letter: ").lower()
    # check if letter was already guessed!
    if guess in display:
        print(f"Already guessed {guess}, try again!")

    # replace _ with guess if it matches a letter in the chosen word!
    for index in range(word_length):
        if guess == chosen_word[index]:
            display[index] = guess

    # check if guess is not in the chosen word, then reduce lives by 1
    if guess not in chosen_word:
        print(stages_[lives_left], "\n", f"{guess} is not in the word. Try again!")
        lives_left -= 1

        # once there's no more lives left, exit the game
        if lives_left < 0:
            print("Game over! You lost!")
            break

    # let the user see how far they've guessed or not guessed...
    print("".join(display))

if "_" not in display:
    print(f"Well done champ! The word is in fact {chosen_word}, You win!")
