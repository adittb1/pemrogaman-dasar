data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("nomer 1")

print("data panen:")
for a, o in data_panen.items():
    nama_lokasi = o["nama_lokasi"]
    hasil_panen = o["hasil_panen"]
    print(f"data panen: {a}")
    print(f" lokasi: {nama_lokasi}")
    print(f" hasil panen: {hasil_panen}\n")
    
print("nomer 2")

hasil_panen_jagung = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f" Jumlah hasil panen jagung adalah: {hasil_panen_jagung} kg\n")

print("nomer 3")
nama_lokasi3 = data_panen["lokasi3"]["nama_lokasi"]
print(f" nama lokasi 3 adalah: {nama_lokasi3}\n")

print("nomer 4")
hasil_panen_padi = 0
hasil_panen_kedelai = 0

for lokasi, data in data_panen.items():
    hasil_panen_padi += data['hasil_panen']['padi']
    hasil_panen_kedelai += data['hasil_panen']['kedelai']
    
print(f" jumlah hasil panen padi: {hasil_panen_padi}")
print(f" jumlah hasil panen kedelai: {hasil_panen_kedelai}\n")

print("nomer 5")
hasil_panen_padi_kedelai = hasil_panen_padi + hasil_panen_kedelai
print(f" Total jumlah hasil panen padi dan kedelai dari semua lokasi: {hasil_panen_padi_kedelai}\n")

print("nomer 6")
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    hasil_panen = data['hasil_panen']
    
    if hasil_panen['padi'] > 1300 or hasil_panen['jagung'] > 800:
        print(f" {nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f" {nama_lokasi} dalam kondisi baik.")