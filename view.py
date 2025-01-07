# Kelas untuk menampilkan data mahasiswa
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
