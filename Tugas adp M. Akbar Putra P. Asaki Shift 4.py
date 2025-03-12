print('========== Daftar Film ===========')
print(f'1 = BOLANG THE MOVIE    Rp 50000')
print(f'2 = MalinG kandang      Rp 40000')
print(f'3 = Kampus Rangers      Rp 65000')
print(f'4 = Indonesia Emas 2045 Rp 80000') 
print(f'5 = Tiktok 2.0          Rp 30000')
print('==================================')

nama = input("Kenalan Dulu yuk kak :) (masukan nama): ")
kode = int(input(f"Masukan kode film nya ya {nama} (1,2,...,5): "))
jumlah = int(input(f"Mau berapa tiket {nama}: "))

satuan = 0
judul = ""

if kode == 1:
        satuan = 50000
        judul = "BOLANG THE MOVIE"
elif kode == 2:
        satuan = 40000
        judul = "MalinG kandang"
elif kode == 3:
        satuan = 65000
        judul = "Kampus Rangers"
elif kode == 4:
        satuan = 80000
        judul = "Indonesia Emas 2045"
elif kode == 5:
        satuan = 30000
        judul = "Tiktok 2.0"
else :
       print(f"Kepada {nama} yang terhormat, masukan kode filmnya sesuai yang tertera di atas ya:")
      
total_harga = jumlah * satuan
diskon = 0

if total_harga > 250000:
    diskon = total_harga * 0.35
elif total_harga > 100000:
    diskon = total_harga * 0.15
else:
    diskon = 0

total_bayar = total_harga - diskon

print('========= Struk Pemesanan Tiket =========')
print(f'Nama           : {nama}')
print(f'Judul Film     : {judul}')
print(f'Jumlah Tiket   : {jumlah}')
print(f'Harga Satuan   : Rp {satuan}')
print(f'Potongan Harga : Rp {diskon}')
print(f'Total Harga    : Rp {total_bayar}')
print('=========================================')
