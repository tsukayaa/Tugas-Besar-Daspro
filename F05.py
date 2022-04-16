# Deskripsi : Mengubah game pada toko game

# Mengubah game pada toko game dilakukan melalui pengisian informasi game yang akan diubah.
# Setelah itu game dengan informasi baru yang telah diubah akan disimpan pada file csv.
# Admin juga tidak harus mengisi semua field selain field ID, sehingga saat admin ingin
# membiarkan value field tertentu agar sesuai dengan value field  data yang lama,
# admin dapat melewatinya dengan mengosongkan. Tidak bisa mengubah stock pada fungsional ini.
# Field ID tidak dapat diubah, hanya digunakan sebagai keyword pencari game.

# akses: admin
# berfungsi mengubah data yang ada pada csv

# >>> ubah_game
# from perpustakaan_fungsi import length
# from array_csv import game

# inisiasi
# id_game = input("Masukkan ID Game: ")
# nama_game = input("Masukkan nama game: ")
# kategori = input("Masukkan kategori: ")
# tahun_rilis = input("Masukkan tahun rilis: ")
# harga = input("Masukkan harga: ")
def ubah_game():
    global game_data
    for row in range (1, length(game)):
        if game_data[row][0] == id:
            if (nama != ''):
                game_data[row][1] = nama
            if (kategori != ''):
                game_data[row][2] = kategori
            if (rilis != ''):
                game_data[row][3] = rilis
            if (harga != ''):
                game_data[row][4] = harga
    return game_data






