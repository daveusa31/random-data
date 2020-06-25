import random


def random_element(_list):
    secure_random = random.SystemRandom()
    return secure_random.choice(_list)
