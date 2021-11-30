import os
import csv

def login():
    login = {1:"admin", 2:"1234"}
    while True:
        user = input("User: ")
        
        if user == login[1]:
            password = input("Password: ")
            if password == login[2]:
                clear_screen()
                return main()
            else:
                clear_screen()
                print("Password Salah") 
                input("Tekan Enter Untuk Mencoba Kembali...")   
                
        else:
            clear_screen()
            print("Username Salah") 
            input("Tekan Enter Untuk Mencoba Kembali...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort(irr):
    for i in range(len(irr) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if irr[j + 1] > irr[j]:
                irr[j], irr[j + 1] = irr[j + 1], irr[j]
                no_swap = False
        if no_swap:
            return

def back_to_menu():
    print("\n")
    input("\t\tTekan Enter untuk kembali...")
    main()

total = {"buku": []}

with open("dataperpus.csv") as fp:
    reader  = csv.reader(fp)
    fields = next(reader)
    for row in reader:
        total["buku"].append(row)


def pilihan():
    
    clear_screen()
    print("----------------------------")
    print("|Daftar Buku Perpustakaan|")
    print("----------------------------")
    print("\t1. Buku Komik")
    print("\t2. Buku Sejarah")
    print("\t3. Buku Teknologi")
    print("\t4. Buku Masakan")
    print("\t5. Buku Novel")
    print("\t6. Kembali")
    print("Batas Peminjam Meminjam Buku Selama 5 Hari, Jika Peminjam Terlambat maka bayar denda sesuai hari")
    print("---------------------------")
    try :
        r = int(input("Masukkan Nomor Menu Yang Anda Inginkan: "))
        if r == 1:
            clear_screen()
            print("\t=====Pilihan Buku=====")
            print("\t1. Naruto")
            print("\t2. Jujutsu Kaisen")
            print("\t3. One Piece")
            print("\t4. Kembali")
            komik = int(input("Masukkan Pilihan Judul Buku : "))
            if komik == 1:
                clear_screen()
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = ("Naruto")
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    i = 1
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif komik == 2:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Jujutsu Kaisen"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif komik == 3:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "One Piece"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()
        
            elif komik == 4:
                clear_screen()
                ulang = print("Anda Yakin Ingin Kembali[y/n]??  ")
                if ulang == "y":
                    main()
                else:
                    pilihan()
        elif r == 2:
            clear_screen()
            print("\t======Pilihan Buku======")
            print("\t1. Sejarah Islam")
            print("\t2. Sejarah Dunia")
            print("\t3. Sejarah Kemerdekaan Indonesia")
            print("\t4. Kembali")
            g = int(input("Masukkan Pilihan Judul Buku: "))
            if g == 1:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Sejarah Islam"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\t|Nomor: ", (total["buku"][i][0]))
                    print("\t\t|Nama : ", (total["buku"][i][1]))
                    print("\t\t|Alamat: ", (total["buku"][i][2]))
                    print("\t\t|Umur: ", (total["buku"][i][3]))
                    print("\t\t|Nama Buku: ", (total["buku"][i][4]))
                    print("\t\t|Tanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                    
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif g == 2:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Sejarah Dunia"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    i = 1
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                  
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif g == 3:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Sejarah Indonesia"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                 
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif g == 4:
                clear_screen()
                ulang = print("Anda Yakin Ingin Kembali[y/n]??  ")
                if ulang == "y":
                    main()
                else:
                    pilihan()
        elif r == 3:
            clear_screen()
            print("\t======Pilihan Buku======")
            print("\t1. Teknologi Mobile")
            print("\t2. Perkembangan Komputer")
            print("\t3. Perkembangan USB")
            print("\t4. Kembali")
            k = int(input("Masukkan Pilihan Judul Buku : "))
            if k == 1:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Teknologi Mobile"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
            elif k == 2:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Perkembangan Komputer"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                  
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif k == 3:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Perkembangan USB"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                  
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif k == 4:
                clear_screen()
                ulang = print("Anda Yakin Ingin Kembali[y/n]?? ")
                if ulang == "y":
                    main()
                else:
                    pilihan()
        elif r == 4:
            clear_screen()
            print("\t======Pilihan Buku======")
            print("\t1. Tips Membuat Roti")
            print("\t2. Resep Pizza")
            print("\t3. Masakan Daerah ")
            print("\t4. Kembali")
            l = int(input("Masukkan Judul Yang Dipilih: "))
            if l == 1:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Tips Membuat Roti"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif l == 2:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Resep Pizza"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                    
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif l == 3:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Masakan Daerah "
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                 
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif l == 4:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Masakan Daerah "
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                 
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif l == 5:
                clear_screen()
                ulang = print("Anda Yakin Ingin Kembali[y/n]??  ")
                if ulang == "y":
                    main()
                else:
                    pilihan()
        elif r == 5:
            clear_screen()
            print("\t======Pilihan Buku======")
            print("\t1. Laskar pelangi")
            print("\t2. Perahu Kertas")
            print("\t3. Dilan 1990")
            print("\t4. Kembali")
            h = int(input("Masukkan Pilihan Judul Buku : "))
            if h == 1:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Laskar Pelangi"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                    
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif h == 2:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Perahu Kertas"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()
            elif h == 3:
                clear_screen()
                print("\tKARTU PEMINJAMAN")
                print("\t================")
                no = len(total["buku"])+1
                nama = input("Masukkan Nama Lengkap Peminjam: ")
                alamat = input("Masukkan Alamat lengkap Peminjam: ")
                umur = int(input("Masukkan Umur Peminjam: "))
                nk = "Dilan 1990"
                tgl = int(input("Tanggal Peminjaman: "))
                total["buku"].append([no, nama, alamat, umur, nk, tgl])
                print("\t\tKARTU PEMINJAMAN")
                print("\t\t================")
                for i in range (len(total["buku"])):
                    print("\t\tNomor: ", (total["buku"][i][0]))
                    print("\t\tNama : ", (total["buku"][i][1]))
                    print("\t\tAlamat: ", (total["buku"][i][2]))
                    print("\t\tUmur: ", (total["buku"][i][3]))
                    print("\t\tNama Buku: ", (total["buku"][i][4]))
                    print("\t\tTanggal Peminjaman:  ", (total["buku"][i][5]))
                    print()
                with open('dataperpus.csv', 'w', newline='') as outcsv:
                    writer = csv.DictWriter(outcsv, fieldnames = ["No", "Nama", "Alamat", "Umur", "Judul Buku", "Tanggal Peminjaman"])
                    writer.writeheader()
                    for i in range (len(total["buku"])):  
                        writer.writerow({'No': total["buku"][i][0], 'Nama': total["buku"][i][1], 'Alamat': total["buku"][i][2], 'Umur' : total["buku"][i][3], 'Judul Buku': total["buku"][i][4], 'Tanggal Peminjaman':total["buku"][i][5]})    
                
                print("Data Berhasil Disimpan!")
                back_to_menu()

            elif h == 4:
                clear_screen()
                ulang = str(print("Anda Yakin Ingin Kembali[y/n]??  "))
                if ulang == "y":
                    main()
                else:
                    pilihan()
        elif r == 6:
            main()
            return main()

    except ValueError:
        print("Input Salah, Coba Lagi!!!")
        back_to_menu()

def kartu():
    rows = []
    with open("dataperpus.csv") as fp:
        reader  = csv.reader(fp)
        fields = next(reader)
        i = 1
        for row in reader:
            rows.append(row)
        
        print(" _____________________________________________________________________________________________________________________________________")
        print("|___No___|__________Nama__________|_______________Alamat_______________|__Umur__|_______Judul Buku_______|_____Tanggal Peminjaman_____|")
   
        for row in rows:    
            a = ''
        
            if int(i) <= 9   :
                a = "|".ljust(3) + "[" + str(i) + "] ".ljust(4) + "|".ljust(3)
            if int(i)> 9:
                a = "|".ljust(3) + "[" + str(i) + "] ".ljust(3) + "|".ljust(3)
            if int(i) >= 99:
                a = "|".ljust(3) + "[" + str(i) + "] ".ljust(2) + "|".ljust(3)
            
               
            a += str(row[1]).ljust(22) + "|".ljust(3)
            a += str(row[2]).ljust(34) + "|".ljust(3)
            a += str(row[3]).ljust(6)  + "|".ljust(3)
            a += str(row[4]).ljust(22) + "|".ljust(3) 
            a += str(row[5]).ljust(26) + "|".ljust(3)
            i += 1
            print(a)
        print("|_____________________________________________________________________________________________________________________________________|")    
        input()



    
def Search(total,n,x):
    for y in range(0, n):
        if (total[y][0] == x):
            return y
    return - 1

def update():
    kartu()
    try:
        cari = input("Nomor Peminjam Yang Ingin Dicari :")
        result = Search(total["buku"], len(total["buku"]), cari)
        
        no = result + 1
        total["buku"][result][0] = no
        nama = input("\t\tMasukkan Nama Lengkap Peminjam: ")
        alamat = input("\t\tMasukkan Alamat lengkap Peminjam: ")
        umur = input("\t\tMasukkan Umur Peminjam: ")
        nk = input("\t\tJudul Buku: ")
        tgl = input("\t\tTanggal Peminjaman: ")
        
        total["buku"][result][0] = no
        total["buku"][result][1] = nama
        total["buku"][result][2] = alamat
        total["buku"][result][3] = umur
        total["buku"][result][4] = nk
        total["buku"][result][5] = tgl
        
        with open("dataperpus.csv", mode="w", newline="") as csv_file:
            fieldnames = ['No','Nama','Alamat','Umur','Judul Buku','Tanggal Peminjaman']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in total["buku"]:
                writer.writerow({'No': new_data[0], 'Nama': new_data[1], 'Alamat': new_data[2], 'Umur': new_data[3], 'Judul Buku': new_data[4], 'Tanggal Peminjaman': new_data[5]})
        
        print("Data Berhasil Di Update!")
        back_to_menu()
    except ValueError:
        print("Silahkan Ulangi Kembali!!")
        update()
    
def delete():
    kartu()
    try:
        cari = input("Nomor Peminjam Yang Ingin Dicari :")
        result = Search(total["buku"], len(total["buku"]), cari)
        del total["buku"][result]
        
        with open("dataperpus.csv", mode="w", newline="") as csv_file:
            fieldnames = ['No','Nama','Alamat','Umur','Judul Buku','Tanggal Peminjaman']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            i = 1
            for new_data in total["buku"]:
                writer.writerow({'No': new_data[0], 'Nama': new_data[1], 'Alamat': new_data[2], 'Umur': new_data[3], 'Judul Buku': new_data[4], 'Tanggal Peminjaman': new_data[5]})
                i += 1
        print("\t\tData telah terhapus!")
        return back_to_menu()
    except ValueError:
        print("Silahkan Ulangi Kembali!!")
        delete()

def denda():
    kartu()
    try:
        cari = input("Nomor Peminjam Yang Ingin Dicari :")
        result = Search(total["buku"], len(total["buku"]), cari)
    
    
        print("No :",(total["buku"][result][0]))
        print("Nama :",(total["buku"][result][1]))
        print("Alamat :",total["buku"][result][2])
        print("Umur :",total["buku"][result][3])
        print("Judul Buku :",total["buku"][result][4])
        print("Tanggal Peminjaman :",total["buku"][result][5])
        print()
    
            
        buku = int(input("\t\tMasukkan Peminjam Telat Berapa Hari Mengembalikan Buku: "))
        book = 2
        def hitung_denda(buku, book):
            if book >= 1:
                return buku ** 2
            return buku
        hasil = hitung_denda(buku, book)
        duit = hasil * 1000
        print(f'Peminjam dikenakan denda sebesar Rp.= {duit}')    

        print("Terimakasih!!")
        return main()
    except ValueError:
        print("\t\tSilahkan Masukkan Ulang!!")
        denda()

def main():
    while True: 
        print("\t\tSISTEM PERPUSTAKAAN")
        print("\t____________________________________")
        print("\t\t1. Daftar Buku")
        print("\t\t2. Pinjam Buku")
        print("\t\t3. Bayar Denda")
        print("\t\t4. Riwayat pinjam")
        print("\t\t5. Keluar          ")
        
    
        print("\t__________________________________________________________________________________________________________________")
        
        w = int(input("\t\tMasukkan Nomor Menu Yang Peminjam inginkan: "))   
        if w == 1:
            print("\tDAFTAR BUKU PERUPUSTAKAAN")
            buku_komik = ["Naruto", "One Piece", "Jujutsu Kaisen"]
            buku_sejarah = ["Sejarah Islam", "Sejarah Dunia", "Sejarah Indonesia"]
            buku_Teknologi = ["Teknologi Mobile", "Perkembangan Komputer", "Perkembangan USB"]
            buku_masakan = ["Tips Membuat Roti", "Resep Pizza", "Masakan Daerah "]
            buku_novel = ["Laskar Pelangi", "Perahu kertas", "Dilan 1990"]
            #Ascending
            print("\nSecara Ascending")
        
            bubbleSort(buku_komik)
            print("Buku Komik     : ", end="")
            for bk in buku_komik:
                if (bk == buku_komik[-1]):
                    print(format(bk), end=" ")
                else:
                    print(format(bk), end=", ")
            print()
            bubbleSort(buku_sejarah)
            print("Buku Sejarah     : ", end="")
            for bs in buku_sejarah:
                if (bs == buku_sejarah[-1]):
                    print(format(bs), end=" ")
                else:
                    print(format(bs), end=", ")
                print()
            bubbleSort(buku_Teknologi)
            print("Buku Teknologi     : ", end="")
            for bt in buku_Teknologi:
                if (bt == buku_Teknologi[-1]):
                    print(format(bt), end=" ")
                else:
                    print(format(bt), end=", ")
                print()
            bubbleSort(buku_masakan)
            print("Buku Masakan     : ", end="")
            for bm in buku_masakan:
                if (bm == buku_masakan[-1]):
                    print(format(bm), end=" ")
                else:
                    print(format(bm), end=", ")
                print()
            bubbleSort(buku_novel)
            print("Buku Novel     : ", end="")
            for bn in buku_novel:
                if (bn == buku_novel[-1]):
                    print(format(bn), end=" ")
                else:
                    print(format(bn), end=", ")
            print()
            
            #Descending
            print("\nSecara Descending")
            bubble_sort(buku_komik)
            print("Buku Komik     : ", end="")
            for bk in buku_komik:
                if (bk == buku_komik[-1]):
                    print(format(bk), end=" ")
                else:
                    print(format(bk), end=", ")
            print()
            bubble_sort(buku_sejarah)
            print("Buku Sejarah     : ", end="")
            for bs in buku_sejarah:
                if (bs == buku_sejarah[-1]):
                    print(format(bs), end=" ")
                else:
                    print(format(bs), end=", ")
            print()
            bubble_sort(buku_Teknologi)
            print("Buku Teknologi     : ", end="")
            for bt in buku_Teknologi:
                if (bt == buku_Teknologi[-1]):
                    print(format(bt), end=" ")
                else:
                    print(format(bt), end=", ")
            print()
            bubble_sort(buku_masakan)
            print("Buku Masakan     : ", end="")
            for bm in buku_masakan:
                if (bm == buku_masakan[-1]):
                    print(format(bm), end=" ")
                else:
                    print(format(bm), end=", ")
            print()
            bubble_sort(buku_novel)
            print("Buku Novel     : ", end="")
            for bn in buku_novel:
                if (bn == buku_novel[-1]):
                    print(format(bn), end=" ")
                else:
                    print(format(bn), end=", ")
            print()
            input("Tekan Enter Untuk Kembali...")
            clear_screen()
            main()
        elif (w == 2):
            pilihan()
        elif w == 3:
            denda()
        elif w == 4:
            peminjaman()    
        elif w == 5:
            print("Terima Kasih Telah Memakai Program Ini")
            SystemExit
            break
        exit()
                       
       

def peminjaman():
    try:
            print("\t-----------------------------")
            print("\t\t1. Data Peminjam")
            print("\t\t2. Update Data")
            print("\t\t3. Delete Data")
            print("\t\t4. Exit")
            print("\t-----------------------------")
            cari = int(input("\t\tMasukkan nomor pilihan Peminjam: "))
            if cari == 1:
                    kartu()
            
            elif cari == 2:
                        update()
            elif cari == 3:                
                        delete()
            elif cari == 4:
                    print("Thank youu")
                    exit()
    except ValueError:
        print("Silahkan Ulangi Kembali!!")
        peminjaman()

login() 