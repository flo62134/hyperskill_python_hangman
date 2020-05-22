# Write your code here
import random

FAILURE = 'You are hanged!'
SUCCESS = 'You survived!'
ASK_FOR_INPUT = 'Guess the word:'
TITLE = 'H A N G M A N'
POSSIBLE_WORDS = ['python', 'java', 'kotlin', 'javascript']

word = random.choice(POSSIBLE_WORDS)
print(TITLE)
attempt = input(ASK_FOR_INPUT)
if attempt == word:
    print(SUCCESS)
else:
    print(FAILURE)
