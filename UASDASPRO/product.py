import os
import string
import random


def welcome():
    while True:
        os.system("clear")
        print("===========================================================")
        print("                  Welcome To SixSport                      ")
        print("                Belanja Asik di SixSport                   ")
        print("===========================================================")
        print("1 - Login Sebagai Admin")
        print("2 - Lihat list Produk")
        print("3 - Keluar Dari Sistem")

        menu = int(
            input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))

        if menu == 1:
            loginAdmin()
        elif menu == 2:
            userLihatProduk()
        elif menu == 3:
            print("terimah telah berkunjung ke toko SixSport")
            break
        else:
            print("masukkin yang bener boskuhh")


def loginAdmin():
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username == "admin" and password == "admin":
        adminPage()
    else:
        print("ANDA BUKAN ADMIN JANGAN SOK SOK JADI ADMIN YA \n\n")
        loginAdmin()


def adminPage():
    while True:

        print("===========================================================")
        print("                  Welcome To Admin Page                    ")
        print("===========================================================")
        print("1 - tambah produk")
        print("2 - Lihat list Produk")
        print("3 - edit produk")
        print("4 - hapus produk")
        print("5 - logout admin")

        menu = int(
            input("Silahkan Pilih Menu Untuk Melanjutkan Proses Transaksi :"))

        if menu == 1:
            tambahProduk()
        elif menu == 2:
            lihatProduk()
        elif menu == 3:
            editProduk()
        elif menu == 4:
            hapusProduk()
            break
        elif menu == 5:
            welcome()
        else:
            print("masukkin yang bener boskuhh")


product_template = {
    "nama_produk": "nama",
    "harga_produk": 20000,
    "stok_produk": 22,
}

data_product = {}


def tambahProduk():

    product = dict.fromkeys(product_template.keys())

    product['nama_produk'] = input("Masukkan nama produk: ")
    product['harga_produk'] = input("Masukkan harga produk: ")
    product['stok_produk'] = input("Masukkan stok produk: ")

    KEY = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=2))

    data_product.update({KEY: product})

    print(f"{'KEY':<10} {'NAMA':<10} {'HARGA':<10} {'STOK':<10}")

    for product in data_product:
        KEY = product
        NAMA = data_product[KEY]['nama_produk']
        HARGA = data_product[KEY]['harga_produk']
        STOK = data_product[KEY]['stok_produk']

        print(f"{KEY:<10} {NAMA:<10} {HARGA:^7} {STOK:^10}")

    print("\n")
    is_done = input(
        "Apakah anda ingin menambahkan produk lagi? (y/n) ")
    if is_done == "y":
        tambahProduk()
    else:
        adminPage()


def lihatProduk():
    print(f"{'KEY':<10} {'NAMA':<10} {'HARGA':<10} {'STOK':<10}")

    for product in data_product:
        KEY = product
        NAMA = data_product[KEY]['nama_produk']
        HARGA = data_product[KEY]['harga_produk']
        STOK = data_product[KEY]['stok_produk']

        print(f"{KEY:<10} {NAMA:<10} {HARGA:^7} {STOK:^10}")

    print("\n")
    is_done = input("apaka anda ingin menambah produk? (y/n) ")
    if is_done == "y":
        tambahProduk()
    else:
        adminPage()


def userLihatProduk():
    print(f"{'KEY':<10} {'NAMA':<10} {'HARGA':<10} {'STOK':<10}")

    isi_produk = len(data_product)
    if isi_produk >= 1:
        for product in data_product:
            KEY = product
            NAMA = data_product[KEY]['nama_produk']
            HARGA = data_product[KEY]['harga_produk']
            STOK = data_product[KEY]['stok_produk']
            print(f"{KEY:<10} {NAMA:<10} {HARGA:^7} {STOK:^10}")
        print("\n")
        membeli = input("apakah anda ingin membeli produk? (y/n) ")
        if membeli == "y":
            beliProduk()
        else:
            print('inputan error')
            welcome()
    else:
        print('===============================')
        print('maaf produk sedang kosong')
        back = input("ketikkan apa saja untuk kembali:")
        if back != "":
            welcome()
        else:
            welcome()


def beliProduk():
    print("\n")
    key = input("Masukkan key produk yang ingin di beli: ").upper()
    print("===========================================================")
    if key in data_product:
        NAMA = data_product[key]['nama_produk']
        HARGA = data_product[key]['harga_produk']
        STOK = int(data_product[key]['stok_produk'])
        print(f"nama produk :{NAMA}")
        print(f"harga produk :{HARGA}")
        print(f"stok produk :{STOK}")
        print("===========================================================")
        if STOK > 0:
            namaPembeli = input("Masukkan nama Anda: ")
            nohp = input("Masukkan No.Hp Anda: ")
            alamat = input("Masukkan alamat Anda: ")
            beli = int(input("ingin beli berapa : "))
            if beli <= STOK:
                total = beli * int(data_product[key]['harga_produk'])
                print(f"NAMA :{namaPembeli}")
                print(f"NO.HP :{nohp}")
                print(f"ALAMAT :{alamat}")
                print(f"beli :{beli} pcs")
                print(f'total belanja anda {total}')
                bayar = int(input("masukan nominal uang anda : "))
                sisa_stok = int(data_product[key]['stok_produk']) - beli
                data_product[key]['stok_produk'] = sisa_stok
                print("===========================================================")
                print("                  Hasil checkout                           ")
                print("===========================================================")
                if total == bayar:
                    print("uang anda pas")
                elif total > bayar:
                    print('uang anda kurang')
                    back = input("ketikkan apa saja untuk kembali:")
                    if back != "":
                        beliProduk()

                elif total < bayar:
                    kembalian = bayar-total

                print(f"Nama :{namaPembeli}")
                print(f"No.HP :{nohp}")
                print(f"Alamat :{alamat}")
                print(f'barang yang di beli : {NAMA}')
                print(f'harga satuan barang : {HARGA}')
                print(f'anda membeli : {beli} item')
                print(f'total harga yang di beli : {total}')
                print(f'uang anda : {bayar}')
                print(f'kembalian anda : {kembalian}')
                print("===========================================================")
                print("                  Terima kasih atas Pembelian anda         ")
                back = input("ketikkan apa saja untuk kembali:")
                if back != "":
                    welcome()

            else:
                print("===========================================================")
                print('pembelian melebihi stok')
                ulang = input(
                    "apakah anda ingin ulang transaksi pembelian (y/n) : ")
                if ulang == "y":
                    beliProduk()
                else:
                    print("kembali ke halaman home")
                    userLihatProduk()
                    welcome()

        else:
            print("maaf stok sedang kosong")
            ubah = input('apakah anda ingin merubah pembelian produk (y/n) : ')
            if ubah == "y":
                beliProduk()
            else:
                print("kembali ke halaman home")
                welcome()
    else:
        print("key tidak ditemukan")
        ulang = input(
            "apakah anda ingin ulang transaksi pembelian (y/n) : ")
        if ulang == "y":
            beliProduk()
        else:
            print("kembali ke halaman home")
            userLihatProduk()
            welcome()


def editProduk():
    print(f"{'KEY':<10} {'NAMA':<10} {'HARGA':<10} {'STOK':<10}")
    for product in data_product:
        KEY = product
        NAMA = data_product[KEY]['nama_produk']
        HARGA = data_product[KEY]['harga_produk']
        STOK = data_product[KEY]['stok_produk']

        print(f"{KEY:<10} {NAMA:<10} {HARGA:^7} {STOK:^10}")

    print("\n")
    ubah = input("apakah anda ingin merubah produk ? (y/n) :")
    if ubah == "y":

        key = input("Masukkan key produk yang ingin di edit: ")

        if key in data_product:
            edit_nama = input("apakah anda ingin mengubah nama produk? (y/n) ")
            if edit_nama == "y":
                data_product[key]['nama_produk'] = input(
                    "Masukkan nama produk baru: ")
                edit_harga = input(
                    "apakah anda ingin mengubah harga produk? (y/n) ")
                if edit_harga == "y":
                    data_product[key]['harga_produk'] = input(
                        "Masukkan harga produk baru: ")
                    edit_stok = input(
                        "apakah anda ingin mengubah stok produk? (y/n) ")
                    if edit_stok == "y":
                        data_product[key]['stok_produk'] = input(
                            "Masukkan stok produk baru: ")
                        print("\n")
                        print("produk berhasil diubah")
                        editProduk()
                    elif edit_stok == "n":
                        print("produk berhasil diubah")
                        editProduk()
                    else:
                        print("masukkan yang bener")
                        editProduk()
                elif edit_harga == "n":
                    edit_stok = input(
                        "apakah anda ingin mengubah stok produk? (y/n) ")
                    if edit_stok == "y":
                        data_product[key]['stok_produk'] = input(
                            "Masukkan stok produk baru: ")
                        print("\n")
                        print("produk berhasil diubah")
                        editProduk()
                    elif edit_stok == "n":
                        print("produk berhasil diubah")
                        editProduk()
                    else:
                        print("masukkan yang bener")
                        editProduk()
                else:
                    print("masukkan yang bener")
                    editProduk()
            elif edit_nama == "n":
                edit_harga = input(
                    "apakah anda ingin mengubah harga produk? (y/n) ")
                if edit_harga == "y":
                    data_product[key]['harga_produk'] = input(
                        "Masukkan harga produk baru: ")
                    edit_stok = input(
                        "apakah anda ingin mengubah stok produk? (y/n) ")
                    if edit_stok == "y":
                        data_product[key]['stok_produk'] = input(
                            "Masukkan stok produk baru: ")
                        print("\n")
                        print("produk berhasil diubah")
                        editProduk()
                    elif edit_stok == "n":
                        print("produk berhasil diubah")
                        editProduk()
                    else:
                        print("masukkan yang bener")
                        editProduk()
                elif edit_harga == "n":
                    edit_stok = input(
                        "apakah anda ingin mengubah stok produk? (y/n) ")
                    if edit_stok == "y":
                        data_product[key]['stok_produk'] = input(
                            "Masukkan stok produk baru: ")
                    elif edit_stok == "n":
                        print("anda tidak mengubah apapun")
                        editProduk()
                    else:
                        print("masukkin yang bener boskuhh")
                        editProduk()
                else:
                    print("masukkin yang bener boskuhh")
                    editProduk()
            else:
                print("masukkin yang bener boskuhh")
                editProduk()
        else:
            print("key tidak ditemukan")
            editProduk()
    else:
        adminPage()


def hapusProduk():
    print(f"{'KEY':<10} {'NAMA':<10} {'HARGA':<10} {'STOK':<10}")
    for product in data_product:
        KEY = product
        NAMA = data_product[KEY]['nama_produk']
        HARGA = data_product[KEY]['harga_produk']
        STOK = data_product[KEY]['stok_produk']

        print(f"{KEY:<10} {NAMA:<10} {HARGA:^7} {STOK:^10}")

    print("\n")
    hapus = input("apakah anda ingin menghapus produk? (y/n) ")
    if hapus == "y":
        key = input("Masukkan key produk yang ingin dihapus: ")
        if key in data_product:
            del data_product[key]
            print("produk berhasil dihapus")
            hapusProduk()
        else:
            print("key tidak ditemukan")
            hapusProduk()
    elif hapus == "n":
        adminPage()
    else:
        print("masukkin yang bener boskuhh")
        hapusProduk()


welcome()
