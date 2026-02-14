import random

# List of words
words = ["python", "hangman", "developer", "programming", "computer"]

# Choose a random word
secret_word = random.choice(words)

# Create a list to store guessed letters
guessed_letters = []

# Create display word with underscores
display_word = []
for letter in secret_word:
    display_word.append("_")

# Number of attempts
attempts = 6

print("🎮 Welcome to Hangman!")
print("You have", attempts, "attempts to guess the word.")

# Game loop
while attempts > 0 and "_" in display_word:
    
    print("\nWord:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()
    
    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
    
    # Check if guess is correct
    elif guess in secret_word:
        print("Correct guess!")
        guessed_letters.append(guess)
        
        # Reveal correct letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    
    # If guess is wrong
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1
        print("Attempts left:", attempts)

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n😢 Game Over! The word was:", secret_word)
    