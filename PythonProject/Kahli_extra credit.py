import random

def choose_movie():
    movies = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight", "Forrest Gump", "Inception", "The Matrix", "Titanic"]
    return random.choice(movies)

def display_movie_title(movie, guessed_letters):
    display = ""
    for letter in movie:
        if letter.lower() in guessed_letters or letter == ' ':
            display += letter
        else:
            display += '_'
    return display

def movie_guessing_game():
    movie_to_guess = choose_movie().lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Movie Guessing Game!")

    while attempts > 0:
        display = display_movie_title(movie_to_guess, guessed_letters)
        print("\nMovie:", display)
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in movie_to_guess:
                print("Good guess!")
            else:
                print("Incorrect guess.")
                attempts -= 1

            guessed_letters.append(guess)

            if set(guessed_letters) == set(movie_to_guess):
                print("\nCongratulations! You guessed the movie:", movie_to_guess)
                break

        else:
            print("Invalid input. Please enter a single letter.")

    if attempts == 0:
        print("\nSorry, you're out of attempts. The correct movie was:", movie_to_guess)

if __name__ == "__main__":
    movie_guessing_game()
