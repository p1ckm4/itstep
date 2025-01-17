import random
import string

def random_letter_generator():
    """
    A generator that yields random letters from the English alphabet.
    """
    while True:
        yield random.choice(string.ascii_letters)


generator = random_letter_generator()
for _ in range(10):
    print(next(generator))
