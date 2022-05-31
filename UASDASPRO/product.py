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
        print("1 - tambah produk")
        print("2 - Lihat list Produk")
        print("3 - edit produk")
        print("4 - hapus produk")

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
        else:
            print("masukkin yang bener goblog")


product_template = {
    "nama_produk": "nama",
    "harga_produk": 20000,
    "stok_produk": 22,
}

data_product = {}


print


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
        welcome()


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
                        print("masukkin yang bener goblog")
                        editProduk()
                else:
                    print("masukkin yang bener goblog")
                    editProduk()
            else:
                print("masukkin yang bener goblog")
                editProduk()
        else:
            print("key tidak ditemukan")
            editProduk()
    else:
        welcome()


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
        welcome()
    else:
        print("masukkin yang bener goblog")
        hapusProduk()


welcome()
