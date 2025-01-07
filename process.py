from data import DataMahasiswa # type: ignore


class MahasiswaProcess:
    """Kelas untuk memproses data mahasiswa."""
    
    def __init__(self):
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