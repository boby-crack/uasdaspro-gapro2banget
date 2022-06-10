import os
import pandas as pd


list_namaMenu = []
list_hargaMenu = []
list_quantityMenu = []
id=0

def selamatDatang():
    while True:
        os.system("clear")
        print("===========================================================")
        print("                  Welcome To SIXPACKS                      ")
        print("                Makan Asik Hanya di Sixpacks               ")
        print("===========================================================")
        print("1 - Login Sebagai Admin")
        print("2 - Lihat list Menu")
        print("3 - Keluar Dari Sistem")

        menu = int(
            input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))

        if menu == 1:
            loginAdmin()
        elif menu == 2:
            lihatMenuUser()
        elif menu == 3:
            print("Anda Berhasil Keluar Dari Sistem")
            print("terimah telah berkunjung ke toko Sixpacks")
            break
        else:
            print("masukkin yang bener boskuhh")


def loginAdmin():
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username.lower() == "admin" and password.lower() == "admin":
        adminPage()
    else:
        print("ANDA BUKAN ADMIN JANGAN SOK SOK JADI ADMIN YA \n\n")
        loginAdmin()


def adminPage():
    while True:

        print("===========================================================")
        print("                  Welcome To Admin Page                    ")
        print("===========================================================")
        print("1 - tambah Menu")
        print("2 - Lihat list Menu")
        print("3 - Hapus Menu")
        print("4 - logout admin")

        menu = int(
            input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))

        if menu == 1:
            tambahMenu()
        elif menu == 2:
            lihatMenuAdmin()
        # elif menu == 3:
        #     editMenu()
        elif menu == 3:
            hapusMenu()
        elif menu == 4:
            selamatDatang()
        else:
            print("masukkin yang bener boskuhh")


def tambahMenu():
    print("===========================================================")
    print("                  Tambah Menu                            ")
    print("===========================================================")

    namaMenu = input("Masukkan nama Menu : ")
    list_namaMenu.append(namaMenu)
    hargaMenu = int(input("Masukkan harga Menu : "))
    list_hargaMenu.append(hargaMenu)
    quantityMenu = input("Masukkan kuantitas Menu : ")
    list_quantityMenu.append(quantityMenu)

    print("===========================================================")
    print("                  Menu Berhasil Ditambahkan              ")
    print("===========================================================")
    print("Nama Menu : ", namaMenu)
    print("Harga Menu : ", hargaMenu)
    print("kuantitas Menu : ", quantityMenu)
    print("===========================================================")
    print("Menu Berhasil Ditambahkan")
    print("===========================================================")

    product = {
        "Nama ": list_namaMenu,
        "Harga ": list_hargaMenu,
        "kuantitas ": list_quantityMenu

    }

    df = pd.DataFrame(product)
    print(df)
    print("===========================================================")

    print("1 - Tambah Menu Lain")
    print("2 - Kembali")

    menu = int(input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))\

    if menu == 1:
        tambahMenu()
    elif menu == 2:
        adminPage()
    else:
        print("masukkin yang bener boskuhh")


def lihatMenuAdmin():
    print("===========================================================")
    print("                  Lihat Menu                             ")
    print("===========================================================")

    product = {
        "Nama ": list_namaMenu,
        "Harga ": list_hargaMenu,
        "kuantitas ": list_quantityMenu

    }

    df = pd.DataFrame(product)
    print(df)
    print("===========================================================")
    hold = input("Tekan apa saja Untuk kembali : ")
    if hold != "":
        adminPage()





def hapusMenu():
    print("===========================================================")
    print("                  Hapus Menu                             ")
    print("===========================================================")
    product = {
        "Nama ": list_namaMenu,
        "Harga ": list_hargaMenu,
        "kuantitas ": list_quantityMenu

    }

    df = pd.DataFrame(product)
    print(df)

    idMenu = int(input("Masukkan id Menu yang ingin anda hapus : "))
    isi = len(list_namaMenu)
    loop = 0

    while True:
        if idMenu == loop:
            list_namaMenu.pop(idMenu)
            list_hargaMenu.pop(idMenu)
            list_quantityMenu.pop(idMenu)
            print("===========================================================")
            print("                  Menu Berhasil Dihapus                 ")
            print("===========================================================")
            hold = input("Tekan apa saja Untuk melihat list Terbaru : ")
            if hold != "":
                lihatMenuAdmin()
            break
        elif idMenu > isi:
            print('data tidak ditemukan')
        loop += 1


def lihatMenuUser():
    print("===========================================================")
    print("                  Lihat Menu                             ")
    print("===========================================================")

    product = {
        "Nama ": list_namaMenu,
        "Harga ": list_hargaMenu,
        "kuantitas ": list_quantityMenu

    }

    df = pd.DataFrame(product)
    if list_namaMenu != []:
        print(df)
    else:
        print('Maaf produk sedang kosong')
        confirm=input('kembali ke halaman home (y/n) : ')
        selamatDatang()



    beli = input("Apakah anda ingin membeli (y/n) : ")
    if beli.lower() == "y":
        beliMenu()
        print("===========================================================")
    elif beli.lower() == "n":
        print("Terima kasih telah berkunjung ke toko Sixpacks")
    else:
        print("masukkin yang bener boskuhh")


def beliMenu():
    print("===========================================================")

    idMenu = int(input("Masukkan id Menu yang ingin anda beli : "))
    isi = len(list_namaMenu)
    loop = 0
    while True:
        if idMenu > isi:
            print('data tidak ditemukan')
        else:
            print("===========================================================")
            print("                  Produk yang anda pilih                  ")
            print("===========================================================")
            print("Nama Menu : ", list_namaMenu[loop])
            print("Harga Menu : ", list_hargaMenu[loop])
            print("kuantitas Menu : ", list_quantityMenu[loop])
            print("===========================================================")
            confirm = input('apakah yakin ingin beli ? (y/n) : ')
            if confirm == "n":
                selamatDatang()
            elif confirm == "y":
                checkout()
       
        loop += 1

def checkout():
    nama=input("nama anda : ")
    email=input("email anda : ")
    jumlah_beli=int(input("masukan jumlah beli : "))
    idMenu = int(input("Masukkan id Menu yang ingin anda beli : "))
    isi = len(list_namaMenu)
    loop = 0
    while True:
        if idMenu > isi :
            print('data tidak ditemukan')
            selamatDatang()
        else:
            print("===========================================================")
            print("                  Hasil Checkout                  ")
            print("===========================================================")
            print("Nama Menu : ", list_namaMenu[loop])
            print("Harga Menu : ", list_hargaMenu[loop])
            print("Nama Pembeli : ", nama)
            print("Email Pembeli : ", email)
            print("Jumlah beli : ", jumlah_beli)
            total=int(list_hargaMenu[loop]) * jumlah_beli
            list_quantityMenu[loop]=int(list_quantityMenu[loop])-jumlah_beli
            print("Total harga : ", total)
            bayar=int(input('masukan uang anda : '))
            if total == bayar:
                    print("uang anda pas : ",bayar)
            elif total > bayar:
                print('uang anda kurang')
                back = input("ketikkan apa saja untuk kembali:")
                if back != "":
                    lihatMenuUser()
            elif total < bayar:
                kembalian = bayar-total
                print(f'kembalian anda : {kembalian}')
            print("===========================================================")
            print("                  Pembelian Berhasil                       ")
            print("===========================================================")
            confirm = input('apakah ingin melihat produk lagi ? (y/n) : ')
            if confirm == "n":
                selamatDatang()
            elif confirm == "y":
                lihatMenuUser()
            
        loop += 1

selamatDatang()







# def editMenu():
#     print("===========================================================")
#     print("                  Edit Menu                             ")
#     print("===========================================================")

#     product = {
#         "Nama ": list_namaMenu,
#         "Harga ": list_hargaMenu,
#         "kuantitas ": list_quantityMenu

#     }

#     df = pd.DataFrame(product)

#     print(df)

#     idMenu = int(input("Masukkan id Menu yang ingin anda edit : "))
#     isi = len(list_namaMenu)
#     loop = 0

#     while idMenu < isi:
#         if idMenu == loop:
#             print("Nama Menu : ", list_namaMenu[idMenu])
#             print("Harga Menu : ", list_hargaMenu[idMenu])
#             print("kuantitas Menu : ", list_quantityMenu[idMenu])
#             editNama = input('apakah ingin merubah nama Menu ? (y/n)')
#             if editNama.lower() == "y":
#                 list_namaMenu[idMenu] = input("Masukkan nama Menu : ")
#                 editHarga = input('apakah ingin merubah harga Menu ? (y/n)')
#                 if editHarga.lower() == "y":
#                     list_hargaMenu[idMenu] = int(
#                         input("Masukkan harga Menu : "))
#                     editQuantity = input(
#                         'apakah ingin merubah kuantitas Menu ? (y/n)')
#                     if editQuantity.lower() == "y":
#                         list_quantityMenu[idMenu] = input(
#                             "Masukkan kuantitas Menu : ")
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     elif editQuantity.lower() == "n":
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     else:
#                         print("masukkin yang bener boskuhh")
#                         hold = input(
#                             "Tekan apa saja Untuk Kembali : ")
#                         if hold != "":
#                             adminPage()
#                 elif editHarga.lower() == "n":
#                     editQuantity = input(
#                         'apakah ingin merubah kuantitas Menu ? (y/n)')
#                     if editQuantity.lower() == "y":
#                         list_quantityMenu[idMenu] = input(
#                             "Masukkan kuantitas Menu : ")
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     elif editQuantity.lower() == "n":
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     else:
#                         print("masukkin yang bener boskuhh")
#                         hold = input(
#                             "Tekan apa saja Untuk Kembali : ")
#                         if hold != "":
#                             adminPage()
#                 else:
#                     print("masukkin yang bener boskuhh")
#                     hold = input(
#                         "Tekan apa saja Untuk Kembali : ")
#                     if hold != "":
#                         adminPage()
#             elif editNama.lower() == "n":
#                 editHarga = input('apakah ingin merubah harga Menu ? (y/n)')
#                 if editHarga.lower() == "y":
#                     list_hargaMenu[idMenu] = int(
#                         input("Masukkan harga Menu : "))
#                     editQuantity = input(
#                         'apakah ingin merubah kuantitas Menu ? (y/n)')
#                     if editQuantity.lower() == "y":
#                         list_quantityMenu[idMenu] = input(
#                             "Masukkan kuantitas Menu : ")
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     elif editQuantity.lower() == "n":
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     else:
#                         print("masukkin yang bener boskuhh")
#                         hold = input(
#                             "Tekan apa saja Untuk Kembali : ")
#                         if hold != "":
#                             adminPage()
#                 elif editHarga.lower() == "n":
#                     editQuantity = input(
#                         'apakah ingin merubah kuantitas Menu ? (y/n)')
#                     if editQuantity.lower() == "y":
#                         list_quantityMenu[idMenu] = input(
#                             "Masukkan kuantitas Menu : ")
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     elif editQuantity.lower() == "n":
#                         print(
#                             "===========================================================")
#                         print(
#                             "                  Menu Berhasil Diedit                 ")
#                         print(
#                             "===========================================================")
#                         hold = input(
#                             "Tekan apa saja Untuk melihat list menu terbaru : ")
#                         if hold != "":
#                             lihatMenuAdmin()
#                     else:
#                         print("masukkin yang bener boskuhh")
#                         hold = input(
#                             "Tekan apa saja Untuk Kembali : ")
#                         if hold != "":
#                             adminPage()
#                 else:
#                     print("masukkin yang bener boskuhh")
#                     hold = input(
#                         "Tekan apa saja Untuk Kembali : ")
#                     if hold != "":
#                         adminPage()
#             else:
#                 print("masukkin yang bener boskuhh")
#                 hold = input(
#                     "Tekan apa saja Untuk Kembali : ")
#                 if hold != "":
#                     adminPage()
#             break
#         elif idMenu > isi:
#             print('data tidak ditemukan')
#         loop += 1