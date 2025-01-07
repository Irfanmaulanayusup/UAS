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

if __name__ == "__main__":
    main()