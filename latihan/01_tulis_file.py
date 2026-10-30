# Latihan 1 - Menulis file (mode w)
with open("data/catatan.txt", "w", encoding="utf-8") as file:
    file.write("Algoritma dan Pemrograman\n")
    file.write("Pertemuan 12\n")

print("File data/catatan.txt berhasil ditulis.")
