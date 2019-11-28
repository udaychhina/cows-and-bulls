import random
import os

# The global variables
guess_count = 0
guess_words = []
results = []
bulls = []
cows = []

# The file is opened, read and then split at every newline character.
# The 'words' list is created with these newly split words
words = open("words.txt").read().split()
# A random word is chosen from the list of words.
rand_word = random.choice(words)
game_word = list(rand_word)


def check_word():
    '''This function gets the word and increments all the values that
    need to be incremented with each guess'''
    global guess_count
    global bulls
    global cows
    # increments the guess count
    guess_count += 1
    # if the guess count reaches 11, that's the last try.
    word = input("Please enter your guess: ")

    # check if the word is the correct length
    if len(word) != 4:
        print("Please enter a 4 letter word!")
        guess_count -= 1
        del word
        check_word()
    else:
        print(f"You have entered \"{word}\".")
        # append the word to the list of guessed words
        guess_words.append(word)
        bulls.append(check_bulls(word))
        cows.append(check_cows(word))
        print_results()


def check_cows(word):
    input_word = list(word)
    cows = 0
    if input_word == game_word:
        exit("4 Bulls! You win!")
    else:
        for i in range(0, len(game_word)):
            for j in range(0, len(input_word)):
                if input_word[i] == game_word[j] and i != j:
                    cows += 1
    return cows


def check_bulls(word):
    input_word = list(word)
    bulls = 0
    if input_word == game_word:
        exit("4 Bulls! You win!")
    else:
        for i in range(0, len(game_word)):
            for j in range(0, len(input_word)):
                if input_word[i] == game_word[j] and i == j:
                    bulls += 1
    return bulls


def print_results():
    for i in range(0, guess_count):
        print("{}. {} --> {} Cow(s), {} Bull(s).".format(i + 1, guess_words[i],
        cows[i], bulls[i]))


def start():
    print("Hello, Welcome to Cows and Bulls!")
    print("# TODO: enter the rules")
    while guess_count < 10:
        check_word()
    if guess_count == 10 and bulls == 4:
        exit("You win!! \nThe word was: {}!".format(rand_word))
    else:
        exit("""AWW! You couldn't guess! Better luck next time, loser.\n
        The word was: {}""".format(rand_word))
start()














