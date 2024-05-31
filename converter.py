
select = input("Válaszd ki miből szeretnél váltani. Ha fahrenheit-ből Celsiusba írj egy C betűt, hogyha fordítva akkor F betűt: ")

# user_celsius = input(": ")
# fahrenheit = user_fahrenheit
# Celsius = user_celsius
# (Celsius * 9/5) + 32

if select == "F" or select == "f":
    user_fahrenheit = int(input("Mennyit szeretnél átváltani Celsiusból Fahrenheitba?: "))
    fahrenheit = (user_fahrenheit * 9/5) + 32
    print(f"{user_fahrenheit}°C = {fahrenheit}°F.")

if select == "C" or select == "c":
    user_celsius = int(input("Mennyit szeretnél átváltani Fahrenheitből Celsiusba?: "))
    celsius = (user_celsius - 32) / 1.8
    print(f"{user_celsius}°F = {celsius} °C.")