guessable_numbers = range(1,11)
correct_number = 1
user = int(input("1-től 10-ig írj egy számot: "))

while user not in guessable_numbers:
    user = int(input("1-től 10-ig írj egy számot: "))
if user == 1:
    print("Helyes, eltaláltad")
elif user != correct_number:
    print("Nem talált!")