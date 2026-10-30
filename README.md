# pertemuan-12-file-io-2225250113

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Masya Bantani |
| **NIM** | 2225250113 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python, serta menangani error dasar (`FileNotFoundError` dan `ValueError`) dengan `try-except` yang spesifik.

## Struktur Folder

```
pertemuan-12-file-io-2225250113/
|-- README.md
|-- .gitignore
|-- data/
|   |-- catatan.txt          # dipakai latihan 1-3
|   |-- nilai.txt            # input Tugas 5 (berisi baris invalid A004,abc)
|   |-- nilai_latihan.txt    # data bersih untuk latihan 4
|   |-- hasil_rekap.txt      # output Tugas 5
|   `-- uji/                 # data untuk test case
|-- latihan/
|   |-- 01_tulis_file.py
|   |-- 02_baca_file.py
|   |-- 03_append_file.py
|   |-- 04_proses_baris.py
|   |-- 05_file_not_found.py
|   `-- 06_value_error.py
`-- tugas/
    `-- rekap_nilai_file.py
```

## Format File Input

Satu record per baris dengan format `NIM,nilai`:

```
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Aturan validasi: baris kosong dilewati, baris yang bukan format `NIM,nilai` atau nilainya bukan angka (atau di luar 0-100) dilaporkan lalu dilewati. Statistik hanya memakai data valid. Nilai >= 60 dihitung lulus.

## Cara Menjalankan

Jalankan dari root folder proyek:

```bash
python3 latihan/01_tulis_file.py     # lalu 02, 03, 04, 05, 06 secara berurutan
python3 tugas/rekap_nilai_file.py
```

Untuk menguji file lain (opsional):

```bash
python3 tugas/rekap_nilai_file.py <file_input> <file_output>
```

## Error yang Ditangani

- `FileNotFoundError`: file input tidak ada, program menampilkan pesan dan tidak crash.
- `ValueError`: nilai bukan angka atau jumlah kolom salah, ditangani per baris sehingga record lain tetap diproses.

## Test Case

| No | Kasus | Kondisi | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|---|
| 1 | Normal | `data/uji/nilai_normal.txt` (4 baris valid) | Semua record diproses, rekap benar | 4 data valid, rata-rata 82.25, min 74.00, maks 92.00, lulus 4 | Lulus |
| 2 | File hilang | `data/uji/tidak_ada.txt` tidak tersedia | Pesan file tidak ditemukan, tidak crash | `File tidak ditemukan: data/uji/tidak_ada.txt`, file output tidak dibuat | Lulus |
| 3 | Nilai invalid | `data/nilai.txt` berisi `A004,abc` | Baris invalid dilewati, record lain diproses | `Baris 4 dilewati: A004,abc`; 5 data valid, rata-rata 83.40 | Lulus |
| 4 | Baris kosong | `data/uji/nilai_baris_kosong.txt` | Baris kosong dilewati | 3 data valid, rata-rata 85.00, tanpa pesan error | Lulus |
| 5 | Batas lulus | `data/uji/nilai_batas_lulus.txt` (60, 59, 60.5, 100) | Nilai 60 dihitung lulus | 4 data valid, lulus 3 (nilai 59 tidak lulus) | Lulus |

Hasil `data/hasil_rekap.txt` untuk `data/nilai.txt`:

```
Jumlah data valid: 5
Rata-rata: 83.40
Minimum: 74.00
Maksimum: 92.00
Jumlah lulus: 5
```

## Refleksi

Error yang saya temukan adalah baris `A004,abc` pada `data/nilai.txt`: nilai `abc` tidak bisa diubah ke `float` sehingga muncul `ValueError`. Awalnya jika satu baris salah, seluruh program berhenti. Dengan `try-except` di dalam loop per baris, program melaporkan baris yang salah (`Baris 4 dilewati: A004,abc`) lalu melanjutkan ke baris berikutnya, sehingga rekap tetap dihitung dari 5 data valid. Saya juga memakai exception yang spesifik, bukan `except:` umum, supaya kesalahan pemrograman lain tidak tersembunyi.

## Exit Ticket

- Perbedaan paling penting antara mode `w` dan `a` adalah `w` menulis dari awal dan menimpa isi lama file, sedangkan `a` menambahkan data di akhir tanpa menghapus isi lama.
- Error file yang paling perlu saya antisipasi adalah `FileNotFoundError`, yaitu ketika file input tidak ada atau path/nama filenya salah.
- Alasan saya menggunakan `with` adalah karena file otomatis ditutup setelah blok selesai, bahkan jika terjadi error, sehingga lebih aman dan rapi.
- Konsep Pertemuan 12 yang akan membantu debugging pada Pertemuan 13 adalah penanganan error per baris dan test case jalur normal/error (file hilang, baris kosong, nilai invalid), karena penyebab masalah jadi mudah dilacak.

## Catatan Bantuan AI

Saya menggunakan bantuan AI dalam menyusun kerangka kode, README, dan dokumen pendukung. Kode, format data, strategi error handling, test case, dan refleksi sudah saya periksa dan dapat saya jelaskan sendiri. Referensi: bahan ajar Pertemuan 12 dan dokumentasi resmi Python.
