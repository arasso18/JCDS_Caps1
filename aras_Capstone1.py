#-------------------------------------------------DATABASE FUNCTION---------------------------------------------------------
def database():
    # Dictionaries Karyawan
    # NIK = Nomor Induk Karyawan
    karyawan = [
        {"NIK": 1, "Nama": "Jaehyun", "Departemen": "HR", "Jabatan": "Manager", "Gaji": 8000000},
        {"NIK": 2, "Nama": "Mark", "Departemen": "IT", "Jabatan": "Developer", "Gaji": 7500000},
        {"NIK": 3, "Nama": "Yuta", "Departemen": "Finance", "Jabatan": "Analyst", "Gaji": 6500000},
        {"NIK": 4, "Nama": "Johhny", "Departemen": "Marketing", "Jabatan": "Supervisor", "Gaji": 7000000},
        {"NIK": 5, "Nama": "Sion", "Departemen": "Sales", "Jabatan": "Salesman", "Gaji": 6000000}
    ]
    return karyawan

#-------------------------------------------------Check Input User---------------------------------------------------------
def validasi_input(input_str, tipe):
    if tipe == "angka":
        return input_str.isdigit()
    elif tipe == "huruf":
        return all(char.isalpha() or char.isspace() for char in input_str)
    elif tipe == "gaji":
        try:
            # Menghapus koma (separator ribuan) dari input sebelum memvalidasi
            input_str = input_str.replace(",", "")
            gaji = float(input_str)
            if gaji <= 0:
                print("Gaji harus lebih besar dari 0!")
                return False
            return True
        except ValueError:
            print("Gaji harus berupa angka!")
            return False
    return False

#-------------------------------------------------CREATE FUNCTION---------------------------------------------------------
def create_karyawan(karyawan, NIK, Nama, Departemen, Jabatan, Gaji):
    # Cek apakah NIK sudah ada di database
    for k in karyawan:
        if k["NIK"] == NIK:
            return False  # NIK sudah ada, kembalikan False
    
    # Jika NIK unik, tambahkan karyawan baru
    karyawan.append({"NIK": NIK, "Nama": Nama, "Departemen": Departemen, "Jabatan": Jabatan, "Gaji": Gaji})
    return True  # Data berhasil ditambahkan

#-------------------------------------------------READ FUNCTION---------------------------------------------------------
def read_karyawan(karyawan):
    print("Daftar Karyawan:")
    for k in karyawan:
        print("\n---------------------")
        print(f"Nama       : {k['Nama']}")
        print(f"NIK        : {k['NIK']}")
        print(f"Departemen : {k['Departemen']}")
        print(f"Jabatan    : {k['Jabatan']}")
        print(f"Gaji       : {k['Gaji']}")
        print("---------------------")

#-------------------------------------------------UPDATE FUNCTION---------------------------------------------------------
def update_karyawan(karyawan, NIK):
    for k in karyawan:
        if k["NIK"] == NIK:
            # Menampilkan data lama sebelum update
            print("\nData Karyawan yang ingin diperbarui:")
            print("---------------------")
            print(f"Nama       : {k['Nama']}")
            print(f"NIK        : {k['NIK']}")
            print(f"Departemen : {k['Departemen']}")
            print(f"Jabatan    : {k['Jabatan']}")
            print(f"Gaji       : {k['Gaji']}")
            print("---------------------")

            # Meminta konfirmasi update
            konfirmasi = input(f"Apakah Anda yakin ingin mengubah data karyawan dengan NIK {NIK}? (y/n): ")
            if konfirmasi.lower() == "y":
                while True:
                    # Meminta input data baru
                    Nama = input(f"Masukkan Nama baru (current: {k['Nama']}): ")
                    Departemen = input(f"Masukkan Departemen baru (current: {k['Departemen']}): ")
                    Jabatan = input(f"Masukkan Jabatan baru (current: {k['Jabatan']}): ")
                    Gaji = input(f"Masukkan Gaji baru (current: {k['Gaji']}): ")

                    # Validasi Nama, Departemen, dan Jabatan hanya huruf dan spasi
                    if not (validasi_input(Nama, "huruf") or validasi_input(Departemen, "huruf") or validasi_input(Jabatan, "huruf")):
                        print("Nama, Departemen, dan Jabatan harus hanya berupa huruf dan spasi! Coba lagi.")
                        continue  # Minta user input ulang jika validasi gagal

                    # Validasi Gaji harus angka
                    if not validasi_input(Gaji, "gaji"):
                        print("Gaji harus berupa angka! Coba lagi.")
                        continue  # Minta user input ulang jika validasi gagal

                    # Jika semua valid, update data
                    k["Nama"] = Nama 
                    k["Departemen"] = Departemen
                    k["Jabatan"] = Jabatan
                    k["Gaji"] = float(Gaji.replace(",", ""))  # gaji disimpan dalam tipe float tanpa koma

                    # Tampilkan data yang baru dimasukkan untuk konfirmasi
                    print("\nData Karyawan setelah diperbarui:")
                    print("---------------------")
                    print(f"Nama       : {k['Nama']}")
                    print(f"NIK        : {k['NIK']}")
                    print(f"Departemen : {k['Departemen']}")
                    print(f"Jabatan    : {k['Jabatan']}")
                    print(f"Gaji       : {k['Gaji']}")
                    print("---------------------")

                    # Tanyakan apakah data baru sudah benar
                    konfirmasi = input("Apakah data baru sudah benar? (y/n): ")
                    if konfirmasi.lower() == "y":
                        print(f"Data karyawan dengan NIK {NIK} berhasil diperbarui.")
                        break  # Keluar dari loop jika data sudah benar
                    else:
                        print("Update dibatalkan, kembali ke menu utama.")  # Batalkan update jika data salah
                        return  # Kembali ke menu utama setelah pembatalan

            else:
                print("Update data dibatalkan.")
                return  # Kembali ke menu utama jika update dibatalkan
            return
    print("Karyawan dengan NIK tersebut tidak ditemukan.")

#-------------------------------------------------DELETE FUNCTIONS---------------------------------------------------------
def del_karyawan(karyawan, NIK):
    # Mencari data karyawan berdasarkan NIK
    for k in karyawan:
        if k["NIK"] == NIK:
            # Menampilkan data karyawan yang akan dihapus
            print("\nData Karyawan yang akan dihapus:")
            print("---------------------")
            print(f"Nama       : {k['Nama']}")
            print(f"NIK        : {k['NIK']}")
            print(f"Departemen : {k['Departemen']}")
            print(f"Jabatan    : {k['Jabatan']}")
            print(f"Gaji       : {k['Gaji']}")
            print("---------------------")

            # Konfirmasi penghapusan
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus data karyawan dengan NIK {NIK}? (y/n): ")
            if konfirmasi.lower() == "y":
                karyawan.remove(k)
                print(f"Karyawan dengan NIK {NIK} berhasil dihapus")
            else:
                print("Hapus data dibatalkan.")
            return
    print("Karyawan tidak ditemukan")

#-------------------------------------------------SEARCH FUNCTION---------------------------------------------------------
def search_karyawan(karyawan, search_value, search_type):
    found = False
    for k in karyawan:
        # Mencari berdasarkan NIK atau Nama
        if search_type == "NIK" and str(k["NIK"]) == search_value:
            print("\nData Karyawan:")
            print(f"Nama       : {k['Nama']}")
            print(f"NIK        : {k['NIK']}")
            print(f"Departemen : {k['Departemen']}")
            print(f"Jabatan    : {k['Jabatan']}")
            print(f"Gaji       : {k['Gaji']}")
            found = True
        elif search_type == "Nama" and search_value.lower() in k["Nama"].lower():
            # Jika Nama mengandung search_value (case insensitive)
            print("\nData Karyawan:")
            print(f"Nama       : {k['Nama']}")
            print(f"NIK        : {k['NIK']}")
            print(f"Departemen : {k['Departemen']}")
            print(f"Jabatan    : {k['Jabatan']}")
            print(f"Gaji       : {k['Gaji']}")
            found = True

    if not found:
        print(f"Karyawan dengan {search_type} '{search_value}' tidak ditemukan.")

#-------------------------------------------------MAIN PAGE FUNCTION---------------------------------------------------------
def main_page():
    karyawan = database()

    while True:
        print("\nSelamat Datang ke Database Neo Culture Tech!")
        print("="*80)
        print("\nMenu Utama:")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Update Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            while True:
                NIK = input("Masukkan NIK: ")
                if not validasi_input(NIK, "angka"):
                    print("NIK harus berupa angka!")
                    continue
                NIK = int(NIK)
                
                # Cek apakah NIK sudah ada di database
                for k in karyawan:
                    if k["NIK"] == NIK:
                        print(f"NIK {NIK} sudah terdaftar! Silahkan masukkan NIK lain.")
                        break
                else:
                    # Jika NIK tidak ditemukan, lanjutkan dengan input lainnya
                    break
            
            Nama = input("Masukkan Nama: ")
            if not validasi_input(Nama, "huruf"):
                print("Nama harus hanya berupa huruf!")
                continue
            Departemen = input("Masukkan Departemen: ")
            if not validasi_input(Departemen, "huruf"):
                print("Departemen harus hanya berupa huruf!")
                continue
            Jabatan = input("Masukkan Jabatan: ")
            if not validasi_input(Jabatan, "huruf"):
                print("Jabatan harus hanya berupa huruf!")
                continue
            
            # Meminta input Gaji
            while True:
                Gaji = input("Masukkan Gaji: ")
                if validasi_input(Gaji, "gaji"):
                    Gaji = float(Gaji.replace(",", ""))  # Menghapus koma dan mengonversi ke float
                    break
                else:
                    print("Gaji harus berupa angka dengan format yang benar!")
            
            # Menanyakan konfirmasi untuk menyimpan data
            konfirmasi = input(f"Apakah Anda ingin menyimpan data karyawan {Nama} dengan NIK {NIK} ke database? (y/n): ")
            if konfirmasi.lower() == "y":
                if create_karyawan(karyawan, NIK, Nama, Departemen, Jabatan, Gaji):
                    print("Data berhasil disimpan.")
                else:
                    print("Gagal menyimpan data. NIK sudah ada.")
            else:
                print("Data tidak disimpan.")
            print("Terima kasih!")

        elif pilihan == "2":
            tampilkan = input("Tampilkan seluruh data (1) atau cari berdasarkan NIK (2) atau Nama (3)? Pilih (1/2/3): ")
            if tampilkan == "1":
                read_karyawan(karyawan)
            elif tampilkan == "2":
                NIK = input("Masukkan NIK karyawan yang ingin dicari: ")
                if not validasi_input(NIK, "angka"):
                    print("NIK harus berupa angka!")
                    continue
                search_karyawan(karyawan, NIK, "NIK")
            elif tampilkan == "3":
                Nama = input("Masukkan Nama karyawan yang ingin dicari: ")
                search_karyawan(karyawan, Nama, "Nama")
            print("Terima kasih!")

        elif pilihan == "3":
            NIK = input("Masukkan NIK karyawan yang ingin diperbarui: ")
            if not validasi_input(NIK, "angka"):
                print("NIK harus berupa angka!")
                continue
            NIK = int(NIK)
            update_karyawan(karyawan, NIK)
            print("Terima kasih!")

        elif pilihan == "4":
            NIK = input("Masukkan NIK karyawan yang ingin dihapus: ")
            if not validasi_input(NIK, "angka"):
                print("NIK harus berupa angka!")
                continue
            NIK = int(NIK)
            del_karyawan(karyawan, NIK)
            print("Terima kasih!")

        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

#-------------------------------------------------MAIN EXECUTION---------------------------------------------------------
main_page()