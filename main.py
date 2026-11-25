
riwayat = []

while True:
    print("\n=== PYTHON CALCULATOR ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Lihat Riwayat")
    print("6. Hapus Riwayat")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "7":
        print("Terima kasih sudah menggunakan kalkulator!")
        break

    elif pilihan == "5":
        if len(riwayat) == 0:
            print("Belum ada riwayat.")
        else:
            print("\n=== RIWAYAT PERHITUNGAN ===")
            for data in riwayat:
                print(data)

    elif pilihan == "6":
        riwayat.clear()
        print("Riwayat berhasil dihapus!")

    elif pilihan in ["1", "2", "3", "4"]:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == "1":
                hasil = angka1 + angka2
                operasi = "+"

            elif pilihan == "2":
                hasil = angka1 - angka2
                operasi = "-"

            elif pilihan == "3":
                hasil = angka1 * angka2
                operasi = "*"

            elif pilihan == "4":
                operasi = "/"

                if angka2 != 0:
                    hasil = angka1 / angka2
                else:
                    print("Tidak bisa membagi dengan nol!")
                    continue

            print("Hasil:", hasil)

            riwayat.append(
                f"{angka1} {operasi} {angka2} = {hasil}"
            )

        except ValueError:
            print("Input harus berupa angka!")

    else:
        print("Pilihan tidak valid!")
