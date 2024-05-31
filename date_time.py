import datetime

# Kérj be két dátumot a felhasználótól.
kezdeti_datum = input("Kezdő dátum: ")
vegso_datum = input("Végső dátum: ")

# Konvertáld a dátumokat `datetime` objektummá.
kezdeti_datum = datetime.datetime.strptime(kezdeti_datum, "%Y-%m-%d")
vegso_datum = datetime.datetime.strptime(vegso_datum, "%Y-%m-%d")

# Használd a `timedelta()` függvényt a két dátum közötti időtartam kiszámításához.
idotartam = vegso_datum - kezdeti_datum

# Írd ki a kiszámított időtartamon.
print("Az időtartam:", idotartam)