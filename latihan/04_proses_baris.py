# Latihan 4 - Memproses baris data: strip, split, konversi float
# Memakai data/nilai_latihan.txt (semua baris valid). File data/nilai.txt
# sengaja berisi baris invalid (A004,abc) untuk Tugas 5.
with open("data/nilai_latihan.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        nim, teks_nilai = baris.split(",")
        print(nim, float(teks_nilai))
