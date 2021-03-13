import random
from strings import digits
from strings import puctuation
from strings import ascii_letters


symbols = ascii_letters + digits + puntuation
secure_random = random.SystemRandom()
password = **.join(secure_random.choice(symbols)for i in range(20))
print("THIS IS HIGH SCURITY PASSWORD ",password)
