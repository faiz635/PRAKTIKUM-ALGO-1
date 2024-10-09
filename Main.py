# PRAK ALGO 1

panjang = float(input("masukan panjang ruangan : "))
lebar = float(input("masukan lebar ruangan :"))
satuan = input ("masukan satuan (meter/inci):")
luas = panjang * lebar 
print(f'''
      luas ruangan dengan panjang {float(panjang)} dan lebar {float(lebar)} adalah {luas}{satuan}
''')


nama = input("Nama kamu siapa?")
asal = input ("Dari mana asal kamu ?")
asal_sekolah = input("Sebelumnya sekolah di mana?")
print(f'''
Halo selamat siang {nama} Wah dari {asal} Pasti menyenangkan sekolah di {asal_sekolah}
 ''')
