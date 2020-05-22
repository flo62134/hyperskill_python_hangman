# Write your code here
import random

FAILURE = 'You are hanged!'
SUCCESS = 'You survived!'
ASK_FOR_INPUT = 'Guess the word:'
TITLE = 'H A N G M A N'
POSSIBLE_WORDS = ['python', 'java', 'kotlin', 'javascript']
HIDDEN_LETTER = '-'


def hint_word(word_to_hint: str):
    length = len(word_to_hint)
    hint = word_to_hint[0:3]
    return hint + (HIDDEN_LETTER * (length - 3))


def ask_attempt(hint_to_display: str):
    message = f"{ASK_FOR_INPUT} {hint_to_display}"
    return input(message)


def is_game_success(current_attempt: str, word_to_guess: str):
    if current_attempt == word_to_guess:
        return True
    else:
        return False


print(TITLE)
word = random.choice(POSSIBLE_WORDS)
hint = hint_word(word)
attempt = ask_attempt(hint)
print(SUCCESS if is_game_success(attempt, word) else FAILURE)
