# Latihan 2 - Membaca file (mode r), baris demi baris
with open("data/catatan.txt", "r", encoding="utf-8") as file:
    for baris in file:
        print(baris.strip())
