#program mengecek bonus dan diskon

total_belanja = int(input("masukkan total harga barang: Rp"))

if total_belanja >= 100000:
    print("kamu mendapatkan bonus jilbab plisket")
    print("dan anda mendapatkan diskon 5%")

    diskon = total_belanja*5/100
    total = total_belanja-diskon
else  :
    total = total_belanja

print("total yang harus dibayar: Rp",total)
print("Terima kasih sudah berbelanja")
print("Datang lagi ya...")
