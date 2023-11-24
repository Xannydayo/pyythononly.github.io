
# hello ges baca dokumentasi ini klo bingung ye
# 
# ini library yee
import sys
import pandas as pd
from tabulate import tabulate
from datetime import datetime
# library end

# date start sini
tanggal_sekarang = datetime.now()
# date end

# ini buat list bertambah saat input coy
total = [] 
# list total end

# ini buat cetak judul biar keren diatas list barang
print("")
print("")
print("date : ", tanggal_sekarang)
print("----------------------------------")
print("|           KASIR BSI            |")
print("----------------------------------")
# judul / nama toko end



# anggap aja ini gudang tempat list nama barang
def daftar_barang():
    data = {
        # no untuk nomor urut barang
        "No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        # no end

        # ini nama nama barangnya
        "Nama Barang": [
            "susu",
            "beras",
            "tepung",
            "whiskas",
            "minyak",
            "madu yusuf",
            "ubi",
            "dinamit",
            "senapan",
            "ban motor",
            "ramen",
            "indomie",
            "lemonilo",
            "nasi uduk",
            "minyak rem",
            "coklat",
            "topi sd",
            "bazzoka",
            "whisky",
            "kipas",
        ],
        # barang end

        # lupain
        # "sku":['s21','br5k','s2sa1','br5sak','s2ewq1','br425k','s2y51','br54t3k','st4321','brqwd5k','s224e3d1','br5r23k','2ed3s21','brr32r5k','sre2321','br5r32k','s2k781','br5ntyk','s21nrt','brnrt5k'],
        # lupain end

        # ini buat harganya ya coy
        "Harga": [16000, 14000, 19000, 17000, 29000, 20000, 25000, 21000, 12000, 26000, 11000, 13500, 28500, 17500, 29500, 26000, 22500, 21500, 12500, 27500],
        # harga end
    }
# gudang end

# pandas 1 start
    # ini buat print pandas biar listnya keluar
    df = pd.DataFrame(data)
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
# pandas end

# input barang start sup
    # ini buat masukin barang yang ingin kita beli cuy
    kode = int(input("Masukkan angka depan barang  : "))
    # jika true dia akan meneruskan
    if 1 <= kode <= len(data["No"]):
        nama = data["Nama Barang"][kode - 1]
        jumlah = int(input("Masukkan jumlah barang : "))
        harga = data["Harga"][kode - 1] * jumlah
        total.append((nama, jumlah, harga))
        tanya()
    # jika false dia akan error
    else:
        print("Kode barang tidak valid.")
        daftar_barang()
# input barang end

# function tanya start
# ini bagian function buat nanya apakah kita ingin menambah barang
def tanya():
    print("\n+--------------------------------+")
    tanya_input = input("  Ingin tambah barang? [y/t] :  ")
    print("+--------------------------------+")
    if tanya_input.lower() == "y":
        print('| barang apa yang ingin ditambah |')
        daftar_barang()
    # elif tanya_input.lower() == "Y":
    #     daftar_barang
    elif tanya_input.lower() == "t":
        akhir()
    elif tanya_input.lower() == "T":
        akhir()
    # ini jika kode yang kita masukan selain Y dan T
    else:
        print("Pilihan yang anda masukan salah!")
        tanya()
# function tanya end

# struk akhir
def akhir():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("UBSI Mart Ciledug")
    print("Jalan Ulujami Raya Ciledug")
    print("Telp 08271289318")
    print("")
    print("date : ", tanggal_sekarang)
    print("+------------------------------------+")
    print("|           Struk Belanja            |")
    print("+------------------------------------+")

    # memasukkan list barang yang sudah kita input ke dalam struk
    df_struk = pd.DataFrame(total, columns=["Nama Barang", "Jumlah", "Harga"])
    print(tabulate(df_struk, headers="keys", tablefmt="psql", showindex=False))

    # menghitung subtotal, diskon, dan total
    subtotal = df_struk["Harga"].sum()
    diskon = 0
    if subtotal > 500000:
        diskon = subtotal * 8 / 100
    elif subtotal > 300000:
        diskon = subtotal * 5 / 100
    elif subtotal > 200000:
        diskon = subtotal * 3 / 100
    elif subtotal > 100000:
        diskon = subtotal * 1 / 100

    # mencetak struk subtotal dengan format tabel
    df_pembayaran = pd.DataFrame(
        {
            "Subtotal ": [subtotal],
            "Potongan": [diskon],
            "Total": [subtotal - diskon],
        }
    )
    print(tabulate(df_pembayaran, headers="keys", tablefmt="psql", showindex=False))

    # memproses pembayaran
    print("+------------------------------------+")
    bayar = int(input("   Bayar            :     "))
    print("+------------------------------------+")

    # jika uang cukup, mencetak kembalian dengan format tabel
    if bayar >= (subtotal - diskon):
        kembalian = bayar - (subtotal - diskon)
        df_kembalian = pd.DataFrame({"Bayar": [bayar],"Kembali": [kembalian], "Anda Hemat": [diskon]})
        print(tabulate(df_kembalian, headers="keys", tablefmt="psql", showindex=False))
        print("+------------------------------------+")
        print("|            Terima Kasih            |")
        print("|          Telah Berbelanja          |")
        print("|            Di UBSI Mart            |")
        print("+------------------------------------+")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    # jika pembayaran kurang, memproses ulang pembayaran
    elif bayar < (subtotal - diskon):
        print("Uang anda kurang")
        tanya_uang()

# tanya_uang dan lainnya tetap seperti sebelumnya


# tanya starto
# nah ini looping yang buat pembayaran kurang jdi tetap di proses
def tanya_uang():
    print("\n--------------------------------------")
    tanya_uang = input("|  Ingin ulangi pembayaran? [y/t] :  ")
    print("--------------------------------------")
    # jika kita ketik Y/y maka pembayaran akan di looping
    if tanya_uang.lower() == "y":
        akhir()
    elif tanya_uang.lower() == "Y":
        akhir
    # sedangkan jika kita input T/t gagal coyy / di cancel
    elif tanya_uang.lower() == "t":
        return
    elif tanya_uang.lower() == "T":
        return
    else:
        tanya_uang()
# tanya berakhir coy

# ini daftar barang2 nya yok
daftar_barang()

# done suf tinggal baca ini klo bingung