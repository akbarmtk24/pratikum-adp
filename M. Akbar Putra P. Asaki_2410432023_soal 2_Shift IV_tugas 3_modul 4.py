#program dengan pengkondisian dan perulangan bersarang untuk melakukan validasi SUATU PASSWORD
#JIKA PENGGUNA MEMASUKAN PASSWORD DENGAN VALID MAKA AKAN MUNCUL (Password Valid)
#jika tidak pengguna diminta memasukan password sampai valid
#password mengandung paling tidak 1 huruf besar satu huruf kecil satu angka dan satu karakter khusus
#panjang minimum karakter adalah 8 karakter

#minimal 8 karakter
#MINIMAL
# 1 huruf kecil
# 1 huruf kapital
# 1 angka
# 1 karakter khusus

print("===== SISTEM VALIDASI PASSWORD =====")

while True:
    password = input("Masukkan password: ")
    
    
    if len(password) >= 8:
        panjang_valid = True
    else:
        print("Password terlalu pendek! Minimal 8 karakter.")

    for char in password:
        if 'a' <= char <= 'z':
            huruf_kecil_valid = True
        elif 'A' <= char <= 'Z':
            huruf_besar_valid = True
        elif '0' <= char <= '9':
            angka_valid = True
        elif char in karakter_khusus:
            karakter_khusus_valid = True

    if panjang_valid and huruf_kecil_valid and huruf_besar_valid and angka_valid and karakter_khusus_valid:
        print("Password Valid! Selamat, Anda berhasil!")
        print("Sistem akan segera ditutup...")
        break  
    else:
        if not huruf_kecil_valid:
            print("Password harus mengandung setidaknya 1 huruf kecil.")
        if not huruf_besar_valid:
            print("Password harus mengandung setidaknya 1 huruf besar.")
        if not angka_valid:
            print("Password harus mengandung setidaknya 1 angka.")
        if not karakter_khusus_valid:
            print("Password harus mengandung setidaknya 1 karakter khusus (!@#$%^&*()-_=+[]{}|;:’\",.<>?/~`).")

        print("Silakan coba lagi...")