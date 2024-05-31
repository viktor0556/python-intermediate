

user = input("Csak A-t vagy B-t írj. Amikor kezdeni akarod írj egy Y betűt: ")


if user == "y" or user == "Y":
    A = []
    print("Ez egy személyiségteszt")
    print("")
    print("Kérlek, válaszolj spontánul, gondolkodás nélkül az alábbi kérdésekre!")
    print("")
    print("Melyik mondat írja le jobban, hogy milyen vagy?")
    print("")
    print("A. Nyitott vagyok az új dolgokra, és szívesen tanulok új dolgokat.")
    print("B. Precíz vagyok és szeretem a jól szervezett dolgokat.")
    user1 = input(": ")
    A.append(user1)

    print("2. Ha egy új projektbe kezdesz, akkor inkább:")
    print("A. Azonnal belekezdesz, és nem félsz a kudarctól.")
    print("B. Gondosan átgondolod a tervedet, és csak akkor kezdesz neki, ha biztos vagy benne, hogy sikerülni fog.")
    user1 = input(": ")
    A.append(user1)

    print("3. Ha egy új emberrel találkozol, akkor inkább:")
    print("A. Nyíltan és közvetlenül kommunikálsz vele.")
    print("B. Figyelmes és udvarias vagy vele.")
    user1 = input(": ")
    A.append(user1)

    print("4. Ha egy döntést kell hoznod, akkor inkább:")
    print("A. Az intuíciódat követed.")
    print("B. A logikát és a tényeket veszed figyelembe.")
    user1 = input(": ")
    print("")
    A.append(user1)

    a_count = A.count("A")
    b_count = A.count("B")

    print(f"A válaszaid: {A}")
    print("")
    print("Kiértékelés")
    print("")

    if a_count > b_count:
        print("A válaszaid alapján: Nyitott az új dolgokra, és szívesen tanul új dolgokat. Spontán és intuitív. Kreatív és ötletes. Elfogadó és toleráns.")
    elif a_count < b_count:
        print("A válaszaid alapján: Precíz és szereti a jól szervezett dolgokat. Gondos és körültekintő. Racionális és logikus. Megbízható és felelősségteljes.")
    else:
        print("A válaszaid alapján: Középponti személyiségtípusról van szó. A középponti személyiségtípusok általában rugalmasabbak és alkalmazkodóképesebbek, mint a tisztán nyitott vagy precíz típusok.")

    