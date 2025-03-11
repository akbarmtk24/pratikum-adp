menu_film = {
    "01": {"judul": "1 jurusan 7 laprak          ", "harga": 44000},
    "02": {"judul": "ganteng ganteng jodohku     ", "harga": 55000},
    "03": {"judul": "manusia terakhir di kampus  ", "harga": 60000},
    "04": {"judul": "aku, kamu, dan 10 sks       ", "harga": 78000},
    "05": {"judul": "harga yang tak pasti        ", "harga": 90000},
    "06": {"judul": "kampus power rangers        ", "harga": 99000},
    "07": {"judul": "sistem kebut semalam        ", "harga": 65000},
    "08": {"judul": "aku diam-diam gamon         ", "harga": 84000},
    "09": {"judul": "I'AM STEVE                  ", "harga": 32000},
    "10": {"judul": "tukang sate madura naik haji", "harga": 85000}
}
print("================FILM BIOSKOP YANG SEDANG TAYANG================")
for kode, data in menu_film.items():
    print(f"|  {kode}  | {data["judul"]}             | Rp{data["harga"]} |")
print("===============================================================")

nama = input("kenalan dulu yuk kak (masukan nama) : ")
kode = input(f"masukin kode film yang mau di tonton ya {nama} (01,02,...,10) : ")
jumlah = int(input(f"berapa banyak tiketnya {nama} : "))

satuan = menu_film[kode]["harga"]
total_harga = satuan*jumlah

if total_harga > 250000 :
    diskon = 0.35*total_harga
elif total_harga > 100000 :
    diskon = 0.15*total_harga
else :
    diskon = 0

harga_setelah_diskon = total_harga - diskon

print("===========STRUK PEMBELIAN TIKET===========")
print(f"nama                 : {nama}")
print(f"Judul Film           : {menu_film[kode]["judul"]}")
print(f"Jumlah Tiket         : {jumlah}")
print(f"Harga Satu Tiket     : Rp{satuan}")
print(f"Total Sebelum Diskon : Rp{total_harga}")
print(f"Diskon               : Rp{(diskon)}")
print(f"Total                : Rp{(harga_setelah_diskon)}")
print("===========================================")
print("              SELAMAT MENONTON")
print(f"                 ==={nama}===")
print("           Kasih Bintang Lima yak")
print("             untuk Bioskop kami")
print("================TERIMA KASIH===============")
