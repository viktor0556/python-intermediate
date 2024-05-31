import random
import string

chars = string.ascii_letters
chars = list(chars)

random.shuffle(chars)

# print(chars)
# print(key)

# Encrypt

user = int(input("Milyen hosszúra szeretnéd a kódot?: "))

for char in range(user):
    char = random.choice(chars)
    print(char, end=" ")
print(" ← A random generált Kódot")


# print(f"Eredeti kód: {plain_text}")
# print(f"titkosított kód: {cipher_text}")