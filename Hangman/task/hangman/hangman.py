# Write your code here
import random

NOT_SINGLE_LETTER = 'You should input a single letter'

NOT_ASCII_LOWERCASE = 'It is not an ASCII lowercase letter'

ALREADY_TRIED = 'You already typed this letter'

NO_IMPROVEMENTS = 'No improvements'

ATTEMPT_FAILURE = 'No such letter in the word'
ASK_LETTER = 'Input a letter:'
FAILURE = 'You are hanged!'
SUCCESS = 'You survived!'
ASK_FOR_INPUT = 'Guess the word:'
TITLE = 'H A N G M A N'
POSSIBLE_WORDS = ['python', 'java', 'kotlin', 'javascript']
HIDDEN_LETTER = '-'
MAX_ATTEMPTS = 8


def hint_word(word_to_hint: str):
    length = len(word_to_hint)
    hint = word_to_hint[0:3]
    return hint + (HIDDEN_LETTER * (length - 3))


def ask_attempt(hint_to_display: str):
    message = f"{ASK_FOR_INPUT} {hint_to_display}"
    return input(message)


def ask_letter():
    return input(ASK_LETTER)


def is_letter_correct(letter: str, word: str):
    return letter in word


def is_letter_improvement(letter: str, hint: str):
    return letter not in hint


def is_letter_already_tried(letter: str, already_tried):
    return letter in already_tried


def is_game_success(attempt: str, word: str):
    if attempt == word:
        return True
    else:
        return False


def add_letter_in_hint(letter_to_add: str, current_hint: str, word: str):
    new_hint = ''
    for index in range(len(word)):
        if current_hint[index] != HIDDEN_LETTER or word[index] == letter_to_add:
            new_hint += word[index]
        else:
            new_hint += current_hint[index]

    return new_hint


def display_title():
    print(TITLE)


def display_end_message(display_success_message: bool):
    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")
    print(SUCCESS if display_success_message else FAILURE)


def is_letter_ascii_lowercase(letter: str):
    return letter.isascii() and letter.islower()


def is_single_letter(string_to_check: str):
    return len(string_to_check) == 1


def has_errors(attempt: str, already_tried_letters):
    if is_letter_already_tried(attempt, already_tried_letters):
        return ALREADY_TRIED

    if not is_single_letter(attempt):
        return NOT_SINGLE_LETTER

    if not is_letter_ascii_lowercase(attempt):
        return NOT_ASCII_LOWERCASE

    return False


n_attempts = 0
attempted_letters = []
word_to_guess = random.choice(POSSIBLE_WORDS)
letter_attempt = ''
already_guessed = HIDDEN_LETTER * len(word_to_guess)
display_title()

while n_attempts < MAX_ATTEMPTS:
    print()
    print(already_guessed)
    letter_attempt = ask_letter()
    error = has_errors(letter_attempt, attempted_letters)
    if error:
        print(error)
        continue

    attempted_letters.append(letter_attempt)
    if not is_letter_improvement(letter_attempt, already_guessed):
        print(NO_IMPROVEMENTS)
        n_attempts += 1
    elif is_letter_correct(letter_attempt, word_to_guess):
        already_guessed = add_letter_in_hint(letter_attempt, already_guessed, word_to_guess)
    else:
        print(ATTEMPT_FAILURE)
        n_attempts += 1

is_success = is_game_success(already_guessed, word_to_guess)
display_end_message(is_success)
