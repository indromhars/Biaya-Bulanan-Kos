import math

# Set Variabel
pembayarPln = 11
pembayarPam = 11
pembayarWifi = 9

biayaPln = float(input("Masukkan biaya PLN bulan ini: "))
biayaPam = float(input("Masukkan biaya PAM bulan ini: "))
biayaWifi = float(input("Masukkan biaya Wifi bulan ini: "))

# Hitung biaya per orang untuk masing-masing biaya
bayarPlnPerOrang = biayaPln / pembayarPln
bayarPamPerOrang = biayaPam / pembayarPam
bayarWifiPerOrang = biayaWifi / pembayarWifi

# Bulatkan hasil biaya per orang ke atas
bayarPlnPerOrang = math.ceil(bayarPlnPerOrang)
bayarPamPerOrang = math.ceil(bayarPamPerOrang)
bayarWifiPerOrang = math.ceil(bayarWifiPerOrang)

# Hitung total biaya bulanan untuk 9 orang dan bulatkan ke atas
biaya9Orang = math.ceil((bayarPlnPerOrang + bayarPamPerOrang + bayarWifiPerOrang) / 500) * 500

# Hitung total biaya bulanan untuk 2 orang dan bulatkan ke atas
totalBiaya2Orang = math.ceil((bayarPlnPerOrang + bayarPamPerOrang) * 2 / 500) * 500

# Hitung total biaya setelah pengurangn uang om nur dan dibagi ke 9 orang
biayaKotor9Orang = (150000 - totalBiaya2Orang) / pembayarWifi
totalBiaya9Orang = math.ceil((biaya9Orang - biayaKotor9Orang) / 500) * 500

print("\nTotal bayar PLN bulan ini adalah:", bayarPlnPerOrang)
print("Total bayar PAM bulan ini adalah:", bayarPamPerOrang)
print("Total bayar WiFi bulan ini adalah:", bayarWifiPerOrang)
print("\nTotal biaya bulanan PLN, PAM, dan Wifi untuk 9 orang adalah:", totalBiaya9Orang)
print("Total biaya bulanan PLN, dan PAM untuk Om Nur adalah:", totalBiaya2Orang)
