# Deskripsi : Menambah game ke toko game
# Penambahan game pada toko game dilakukan melalui pengisian informasi game yang akan ditambahkan.
# Program lalu akan melakukan validasi apakah semua informasi yang dibutuhkan telah diinput oleh admin.
# Apabila terdapat informasi yang belum dimasukkan oleh pengguna, program akan meminta input lagi kepada pengguna.
# Hal ini akan dilakukan terus menerus sampai pengguna telah melakukan input semua informasi game.
# Game baru yang telah ditambahkan akan disimpan pada file csv.

# akses : admin
# berfungsi untuk mengambil data dari game.csv
# menambah game yang diinput ke csv --> ada di fungsional save
# pada fungsi ini, penambahan game dimasukkan ke memori bukan ke csv

# >>> tambah_game
from array_csv import game

def tambah_game(nama_game, kategori_game, tahun_rilis, harga_game, stok_awal):
    while (nama_game=='') or (kategori_game=='') or (tahun_rilis=='') or (harga_game=='') or (stok_awal==''):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO")
        nama_game = input("Masukkan nama game: ")
        kategori_game = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga_game = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
    else:
        print('Selamat! Berhasil menambahkan game', nama_game)
        game_baru = [[nama_game, kategori_game, tahun_rilis, harga_game, stok_awal]]
    return (game+game_baru)

# nama_game = input("Masukkan nama game: ")
# kategori_game = input("Masukkan kategori: ")
# tahun_rilis = input("Masukkan tahun rilis: ")
# harga_game = input("Masukkan harga: ")
# stok_awal = input("Masukkan stok awal: ")
# tambah_game(nama_game,kategori_game,tahun_rilis,harga_game,stok_awal)