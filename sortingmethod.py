
words = []
numbers = []
entire = words, numbers

def sort_method(user):
    while user != "Nem" or user != "nem":
        user = input("Írj szavakat vagy számokat: ")
        if isinstance(user, str) and user.isdigit():
            numbers.append(user)
            print("Sikeresen hozzáadva a számok listához")
        elif isinstance(user, str):
            words.append(user)
            print("Sikeresen hozzáadva a szavak listához")
        if user == "Nem" or user == "nem":
            print(f"Szavak: {words} Számok: {numbers}")

sort_method(entire)