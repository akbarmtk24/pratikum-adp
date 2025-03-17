modal = int(input("masukan modal awal : "))
bunga = int(input("masukan suku bunga tahunan (&) : "))
target = int(input("masukan target : "))
i = 1

while modal <= target :
    modal += modal*(bunga/100)
    print(f"Tahun ke-{i}: Rp{modal}")
    i+=1
    
print(f"target tercapai dalam {i-1} tahun!")