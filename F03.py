# Deskripsi: Login

# Saat masuk ke dalam aplikasi, pengguna bisa login dengan memasukkan username dan password.
# Bila username dan password yang diinput cocok dengan username dan password pada file user,
# maka pengguna berhasil login. Untuk alur login dibebaskan;
# tidak harus mengetik “login” dulu diperbolehkan (misal, ketika sistem menyala user diwajibkan login,
# namun pastikan kalau belum login tidak bisa melakukan apa-apa selain login).

# akses: admin dan user
# >>> login
# username = input("Masukkan username: ")
# password = input("Masukkan password: ")

from array_csv import user
from perpustakaan_fungsi import length

def login(username, password):
    for row in range (length(user)):
        if user[row][1] != username or user[row][3] != password:
            print("Password atau username salah atau tidak ditemukan.")
        else:
            print('Halo', user[row][2], '! Selamat datang di "Binomo".')
