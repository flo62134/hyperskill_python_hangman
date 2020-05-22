NOPE = "I won't do it!"
MAGIC_WORD = 'Simon says'


def what_to_do(instructions: str):
    is_valid_instruction = instructions.startswith(MAGIC_WORD) \
                           or instructions.endswith(MAGIC_WORD)
    if is_valid_instruction:
        answer = instructions.replace(MAGIC_WORD, '')
        answer = answer.strip()
        return 'I ' + answer
    else:
        return NOPE
