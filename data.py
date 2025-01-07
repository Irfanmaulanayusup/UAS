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
