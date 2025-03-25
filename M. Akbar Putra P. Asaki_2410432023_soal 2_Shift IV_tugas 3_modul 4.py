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

print("=============VALIDASI PASSWORD ANDA=============")

while True :
    password = input("buat paswword anda yang mudah di ingat: ")

    panjang = False
    kecil = False
    kapital = False
    angka = False
    khusus = False
    emoji = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"

    if len(password) >= 8 :
        panjang = True
    else :
        print("karakter minimal 8!")
    
    for karakter in password :
        if "a" <= karakter <= "z":
            kecil = True
        elif "A" <= karakter <="Z":
            kapital = True
        elif "1" <= karakter <= "9":
            angka = True
        elif karakter in emoji :
            khusus = True
    
    if panjang and kecil and kapital and khusus and angka :
        print("selamat password and valid dan kuat")
        print("sistem di tutup!")
        break
    else :
        if not kecil :
            print("minimal 1 huruf kecil dalam password!")
        if not kapital :
            print("minimal 1 huruf kapital dalam password!")
        if not khusus :
            print ("minimal ada 1 karakter khusus dalam password! contoh (!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`)")
        if not angka :
            print("minimal ada 1 angka dalam password!")

        print("silakan coba lagi!")