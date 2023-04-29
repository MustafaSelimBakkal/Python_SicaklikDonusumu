print("-" * 30)
print("1-Celcius")
print("2-Fahrenheit")
print("-"*30)

secim = input("Sizin Seçiminiz (1/2): ")

if secim == "1":
    print("\n# Celcius'tan Fahrenheit'e ")
    celcius = float(input("Celcius derecesini girin : "))
    fahrenheit = (celcius * 1.8) +32
    print(f"{celcius} Derece celcius, {fahrenheit} derece fahrenheite eşittir ")

elif secim == "2":
    print("\n# Fahrenheit'ten celcius'a ")
    fahrenheit = float(input("Fahrenheit derecesini girin : "))
    celcius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} Derece fahrenheit,{celcius} derece celciusa eşittir ")

else:
    print("Aferin! Programımı hackledin şimdi yeniden başlat.")
