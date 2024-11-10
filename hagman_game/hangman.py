# hangman.py

def print_hangman(incorrect_guesses):
    """Prints the hangman figure based on the number of incorrect guesses."""
    hangman_parts = [
        "------\n|    |\n     |\n     |\n     |\n     |\n---------",
        "------\n|    |\nO    |\n     |\n     |\n     |\n---------",
        "------\n|    |\nO    |\n|    |\n     |\n     |\n---------",
        "------\n|    |\nO    |\n/|    |\n     |\n     |\n---------",
        "------\n|    |\nO    |\n/|\\   |\n     |\n     |\n---------",
        "------\n|    |\nO    |\n/|\\   |\n/     |\n     |\n---------",
        "------\n|    |\nO    |\n/|\\   |\n/ \\   |\n     |\n---------",
        "------\n|    |\nO    |\n/|\\   |\n/ \\   |\nGAME OVER |\n---------"
    ]
    print(hangman_parts[incorrect_guesses])

def print_word_progress(secret_word, correct_guesses):
    """Prints the current progress of the word with blanks for unguessed letters."""
    progress = ''.join([letter if letter in correct_guesses else '_' for letter in secret_word])
    print("Word: " + ' '.join(progress))

def hangman_game(secret_word):
    """Main function to run the Hangman game."""
    secret_word = secret_word.lower()
    correct_guesses = set()
    incorrect_guesses = set()
    max_wrong_guesses = 8
    wrong_guesses = 0

    print("Welcome to Hangman!")

    while wrong_guesses < max_wrong_guesses:
        print_word_progress(secret_word, correct_guesses)
        print_hangman(wrong_guesses)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"Good guess: {guess} is in the word!")
        else:
            incorrect_guesses.add(guess)
            wrong_guesses += 1
            print(f"Oops! {guess} is not in the word.")

        if all(letter in correct_guesses for letter in secret_word):
            print_word_progress(secret_word, correct_guesses)
            print("Congratulations, you guessed the word!")
            break

    if wrong_guesses == max_wrong_guesses:
        print_hangman(wrong_guesses)
        print(f"Game Over! The word was: {secret_word}")

# Start the game with a chosen word
hangman_game("python")
