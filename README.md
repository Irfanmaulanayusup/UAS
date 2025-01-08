# UAS
Kelas DataMahasiswa:

# Kelas untuk merepresentasikan data mahasiswa
class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa."""
        self.daftar_mahasiswa.append({'nama': nama, 'nilai': nilai})

    def get_data(self):
        """Mengembalikan daftar mahasiswa."""
        return self.daftar_mahasiswa

Menyimpan data mahasiswa dalam list.

Metode tambah: Menambahkan mahasiswa ke dalam list.

Metode get_data: Mengambil daftar mahasiswa.

# Kelas MahasiswaView:



class MahasiswaView:
    @staticmethod
    def tampilkan_list(daftar_mahasiswa):
        """Menampilkan list data mahasiswa dalam format tabel."""
        if not daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("+-------------------+-------+")
        print("|       Nama        | Nilai |")
        print("+-------------------+-------+")
        for mhs in daftar_mahasiswa:
            print(f"| {mhs['nama']: <15} | {mhs['nilai']: <5} |")
        print("+-------------------+-------+")




Menampilkan daftar mahasiswa dalam format tabel.

Metode tampilkan_list: Mencetak tabel mahasiswa ke layar.

# Kelas MahasiswaProcess dan fungsi validasi nilai
from data import DataMahasiswa # type: ignore


class MahasiswaProcess:
    """Kelas untuk memproses data mahasiswa."""
    
    def _init_(self):
        self.data_mahasiswa = DataMahasiswa()

    def tambah_mahasiswa(self, nama, nilai):
        """Menambah mahasiswa baru."""
        self.data_mahasiswa.tambah(nama, nilai)

    def tampilkan_mahasiswa(self):
        """Menampilkan semua data mahasiswa."""
        return self.data_mahasiswa.get_data()


def validasi_nilai(nilai):
    """Fungsi untuk memvalidasi input nilai."""
    try:
        nilai = float(nilai)  # Mengonversi nilai ke float
        if nilai < 0:
            raise ValueError("Nilai tidak boleh negatif.")
        return nilai
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return None  # Mengembalikan None jika konversi gagal

Mengelola proses penambahan dan penampilan data mahasiswa.

Metode tambah_mahasiswa: Menambahkan mahasiswa baru.

Metode tampilkan_mahasiswa: Mengambil daftar mahasiswa untuk ditampilkan.

Fungsi validasi_nilai:

Memvalidasi nilai yang dimasukkan pengguna.

Mengonversi nilai ke float dan memeriksa apakah valid.

Fungsi main:
from process import MahasiswaProcess, validasi_nilai
from view import MahasiswaView


def main():
    process = MahasiswaProcess()
    view = MahasiswaView()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            nilai_valid = validasi_nilai(nilai)
            if nilai_valid is not None:
                process.tambah_mahasiswa(nama, nilai_valid)
                print(f"Data mahasiswa {nama} berhasil ditambahkan dengan nilai {nilai_valid}.")
        elif pilihan == '2':
            daftar_mahasiswa = process.tampilkan_mahasiswa()
            view.tampilkan_list(daftar_mahasiswa)
        elif pilihan == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if _name_ == "_main_":
    main()


Menjalankan menu interaktif untuk menambah dan menampilkan data mahasiswa.

Mengelola input pengguna dan validasi nilai.
