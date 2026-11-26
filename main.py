# Python Computer Toolkit
history = []

# Main Menu
while True:
    print("\n=== PYTHON CALCULATOR TOOLKIT ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Lihat Riwayat")
    print("6. Hapus Riwayat")
    print("7. Binary to Decimal Converter")
    print("8. Decimal to Binary Converter")
    print("9. Unit Converter")
    print("10. Keluar")

    pilihan = input("Pilih menu (1-10): ")

    if pilihan == "10":
        print("Terima kasih sudah menggunakan kalkulator!")
        break

    elif pilihan == "5":
        if len(history) == 0:
            print("Belum ada riwayat.")
        else:
            print("\n=== RIWAYAT PERHITUNGAN ===")
            for data in history:
                print(data)

    elif pilihan == "6":
        history.clear()
        print("Riwayat berhasil dihapus!")
    elif pilihan == "7":
        try:
            biner = input("Masukkan angka biner: ")
            desimal = int(biner, 2)

            print("Hasil desimal:", desimal)

        except ValueError:
            print("Input biner tidak valid! Gunakan angka 0 dan 1.")
    elif pilihan == "8":
        try:
            desimal = int(input("Masukkan angka desimal: "))
            biner = bin(desimal)[2:]

            print("Hasil biner:", biner)

        except ValueError:
            print("Input harus berupa bilangan bulat!")

    elif pilihan == "9":
        print("\n=== UNIT CONVERTER ===")
        print("1. Kilometer ke Meter")
        print("2. Meter ke Kilometer")
        print("3. Meter ke Centimeter")

        satuan = input("Pilih konversi (1-3): ")

        try:
            if satuan == "1":
               km = float(input("Masukkan kilometer: "))
               meter = km * 1000
               print("Hasil:", meter, "meter")

            elif satuan == "2":
                meter = float(input("Masukkan meter: "))
                km = meter / 1000
                print("Hasil:", km, "kilometer")

            elif satuan == "3":
                 meter = float(input("Masukkan meter: "))
                 cm = meter * 100
                 print("Hasil:", cm, "centimeter")

            else:
                 print("Pilihan tidak valid!")

        except ValueError:
                 print("Input harus berupa angka!")        

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

            history.append(
                f"{angka1} {operasi} {angka2} = {hasil}"
            )
    elif pilihan == "7":
        binary = input("Masukkan bilangan biner: ").strip()

        if binary and all(bit in "01" for bit in binary):
            hasil = int(binary, 2)
            print("Hasil desimal:", hasil)
        else:
            print("Input hanya boleh berisi 0 dan 1!")

    elif pilihan == "8":
        try:
            angka = int(input("Masukkan bilangan desimal: "))

            if angka >= 0:
                hasil = format(angka, "b")
                print("Hasil biner:", hasil)
            else:
                print("Masukkan bilangan positif atau nol!")

        except ValueError:
            print("Input harus berupa bilangan bulat!")

        except ValueError:
            print("Input harus berupa angka!")

    else:
        print("Pilihan tidak valid!")
