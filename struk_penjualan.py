from datetime import datetime
import pytz
import pandas as pd
from tabulate import tabulate

indonesia_wib = pytz.timezone('Asia/Jakarta')

utc_now = datetime.utcnow()

wib_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indonesia_wib)

formatted_wib_now = wib_now.strftime('%A, %d %B %Y %H:%M:%S %Z')

tanggal_sekarang = datetime.now()
print("                  TOKO ACIRO          ")
print("   JL. PANJANG CIDODOL NO.1 CIPULIR KEB. LAMA  ")
print("          NPWP : 01.780.859.3-013.000     ")
print("date : ", formatted_wib_now)


# Fungsi Format Rupiah
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return "Rp " + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + "." + p


#tgl indonesia dan jam
indonesia_wib = pytz.timezone('Asia/Jakarta')

utc_now = datetime.utcnow()

wib_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indonesia_wib)

formatted_wib_now = wib_now.strftime('%A, %d %B %Y %H:%M:%S %Z')
# tanggal end

# Data Produk
produk = {
    "Kode": ["A", "B", "C", "D", "E", "F"],
    "Barang": [
        "Garantea Jasmine 350ml",
        "Qtela Tempe Ori 55g",
        "Kanzler Sosis Single Ori 65gr",
        "Yakult/5",
        "Lemonilo Mie Goreng 70g",
        "Tas Belanja Besar",
    ],
    "Harga": [4200, 6400, 8500, 10500, 9800, 4000],
}

# Konversi ke DataFrame
df_produk = pd.DataFrame(produk)

while True:  # Loop untuk mengulangi keseluruhan proses transaksi
    # Tampilkan Tabel Produk
    print("\nDaftar Produk:")
    print(tabulate(df_produk, headers="keys", tablefmt="psql", showindex=False))

    # Input dari Pengguna
    banyakBarang = 6
    pesanan = []

    for i in range(banyakBarang):
        kode = input(f"Masukkan Kode Barang ke-{i+1} [A-F]: ").upper()
        if kode not in df_produk["Kode"].values:
            print("Kode barang tidak valid. Silakan coba lagi.")
            continue

        try:
            jumlah = int(input("Jumlah Barang: "))
            if jumlah <= 0:
                raise ValueError("Jumlah barang harus lebih dari 0")

        except ValueError as e:
            print(f"Input tidak valid: {e}.")
            continue

        barang = df_produk[df_produk["Kode"] == kode].iloc[0]
        total = barang["Harga"] * jumlah
        pesanan.append([barang["Barang"], barang["Harga"], jumlah, total])

    # Konversi Pesanan ke DataFrame

    df_pesanan = pd.DataFrame(
        pesanan, columns=["Nama Barang", "Harga", "Qty", "Jumlah"]
    )

    # ...

# Calculate Total
    total_pembelian = df_pesanan["Jumlah"].sum()

# Calculate Subtotal before discount
    subtotal = df_pesanan["Jumlah"].sum()
    diskon = 0
# Calculate Discount
    if total_pembelian > 100000:
        diskon = total_pembelian * 10 / 100
    elif total_pembelian > 70000:
        diskon = total_pembelian * 8 /  100
    elif total_pembelian > 50000:
        diskon = total_pembelian * 5 / 100
    elif total_pembelian > 30000:
        diskon = total_pembelian * 3 / 100

# Apply Discount to Subtotal
    subtotal_after_diskon = subtotal - diskon


    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
# Display Receipt
    print("")
    print("                  TOKO ACIRO         ")
    print("     JL. PANJANG NO. 1 CIPULIR, KEB. LAMA ")
    print("         NPWP : 01.780.859.3-013.000 ")
    print("date : ", formatted_wib_now)
    print(df_pesanan)
    print('')
    print('')
    print(f"Total Pembelian : Rp {int(total_pembelian)}")
    print(f"Potongan        : Rp {int(diskon)}")
    print(f"netto           : Rp {int(subtotal_after_diskon)}")

# ...

# Pembayaran dan Kembalian
    while True:
        try:
            jumlah_bayar = int(input("Jumlah Bayar    : Rp "))
            if jumlah_bayar >= subtotal_after_diskon:
                kembalian = jumlah_bayar - subtotal_after_diskon
                print(f"Kembalian       : Rp {int(kembalian)}")
                print('JUMLAH ITEM BARANG : 6')
                break
            else:
                print("Uang tidak cukup. Silakan masukkan jumlah yang cukup.")
        except ValueError:
            print("Masukkan angka yang valid.") 
        # Tanya pengguna apakah ingin melakukan transaksi lain
    ulangi = input("\nApakah Anda ingin melakukan transaksi lain? (y/t): ").lower()
    if ulangi != "y":
        produk
        break
    
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    

