"""Tugas 5 - Rekap nilai dari file.

Membaca data/nilai.txt (format: NIM,nilai), memvalidasi setiap baris,
menghitung ringkasan, lalu menulis hasilnya ke data/hasil_rekap.txt.

Cara menjalankan (dari root folder proyek):
    python3 tugas/rekap_nilai_file.py
Opsional, untuk menguji file lain:
    python3 tugas/rekap_nilai_file.py <file_input> <file_output>
"""
import sys

NILAI_LULUS = 60


def baca_data(nama_file):
    """Baca dan validasi file. Kembalikan list (nim, nilai) yang valid.

    Jika file tidak ada, tampilkan pesan dan kembalikan list kosong.
    Baris kosong dilewati; baris invalid dilaporkan lalu dilewati.
    """
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    if not 0 <= nilai <= 100:
                        raise ValueError("nilai di luar rentang 0-100")
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
    return data


def tulis_rekap(nama_file, data):
    """Hitung statistik dari data valid lalu tulis ke nama_file."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return False

    nilai = [item[1] for item in data]
    jumlah_lulus = sum(1 for x in nilai if x >= NILAI_LULUS)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {len(nilai)}\n")
        file.write(f"Rata-rata: {sum(nilai) / len(nilai):.2f}\n")
        file.write(f"Minimum: {min(nilai):.2f}\n")
        file.write(f"Maksimum: {max(nilai):.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")
    return True


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "data/nilai.txt"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "data/hasil_rekap.txt"

    data = baca_data(input_file)
    if data and tulis_rekap(output_file, data):
        print(f"Record valid diproses: {len(data)}")
        print(f"Rekap ditulis ke {output_file}")


if __name__ == "__main__":
    main()
