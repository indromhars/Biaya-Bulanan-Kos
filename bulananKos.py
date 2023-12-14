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

# Hitung total biaya bulanan untuk 9 orang
totalBiaya9Orang = bayarPlnPerOrang + bayarPamPerOrang + bayarWifiPerOrang

# Hitung total biaya bulanan untuk 2 orang
totalBiaya2Orang = bayarPlnPerOrang + bayarPamPerOrang

# Trim the float output to 2 decimal places
bayarPlnPerOrang = round(bayarPlnPerOrang, 2)
bayarPamPerOrang = round(bayarPamPerOrang, 2)
bayarWifiPerOrang = round(bayarWifiPerOrang, 2)
totalBiaya9Orang = round(totalBiaya9Orang, 2)
totalBiaya2Orang = round(totalBiaya2Orang, 2)

print("\nTotal bayar PLN bulan ini adalah: " + str(bayarPlnPerOrang))
print("Total bayar PAM bulan ini adalah: " + str(bayarPamPerOrang))
print("Total bayar WiFi bulan ini adalah: " + str(bayarWifiPerOrang))
print("\nTotal biaya bulanan PLN, PAM, dan Wifi untuk 9 orang adalah: " + str(totalBiaya9Orang))
print("Total biaya bulanan PLN, dan PAM untuk 2 orang adalah: " + str(totalBiaya2Orang))