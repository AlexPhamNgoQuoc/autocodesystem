import random

def hangman():
    words = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']  # List of words to guess
    word = random.choice(words).lower()  # Select a random word from the list
    guessed_letters = []  # List to store the guessed letters
    tries = 6  # Number of tries allowed

    print("Welcome to Hangman!")
    print("_ " * len(word))  # Print underscores for each letter in the word
    
    while tries > 0:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct guess!")
        else:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")
        
        # Print the word with guessed letters filled in and underscores for unknown letters
        print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word.")
            break
    
    if tries == 0:
        print("Game over. You ran out of tries.")
        print(f"The word was: {word}")

hangman()
