# Latihan 3 - Menambah isi file (mode a)
with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Latihan append berhasil.\n")

print("Baris baru ditambahkan ke data/catatan.txt.")
