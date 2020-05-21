# Write your code here
FAILURE = 'You are hanged!'
SUCCESS = 'You survived!'
ASK_FOR_INPUT = 'Guess the word:'
TITLE = 'H A N G M A N'

word = 'python'
print(TITLE)
attempt = input(ASK_FOR_INPUT)
if attempt == word:
    print(SUCCESS)
else:
    print(FAILURE)
