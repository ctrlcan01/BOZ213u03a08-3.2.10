kelime = input("Bir kelime giriniz: ")
kelime = kelime.upper()

for harf in kelime:
    if harf in "AEIOU":
        continue

    print(harf)
