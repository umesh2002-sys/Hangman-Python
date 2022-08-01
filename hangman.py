import random
from re import A
from words import words
import string

def get_valid_word(words):
    word = random.choices(words)
    while '-' in word or  ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # letter user has to guess
    used_insert = set()

    lives = 8

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join (['a', 'b', 'c']) --> 'a b c'
        print('You have', lives,'Lives left and You have used those letter: ', ' '.join(used_insert))

        # What corrent word is (ie W - R D)
        word_list = [letter if letter in used_insert else '_' for letter in word]a
        print('Current words: ', ' '.join(word_list))

        # Getting user input
        user_insert = input('Guess a letter : ').upper()
        if user_insert in alphabet - used_insert:
            used_insert.add(user_insert)
            if user_insert in word_letters:
                word_letters.remove(user_insert)
            else:
                lives = lives -1
                print("Letter is not in a word.")

        elif user_insert in used_insert:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You Lose the word was ', word)
    else:
        print('yahh!!!! you guessed the word', word, 'You win!!!!')   

hangman()

