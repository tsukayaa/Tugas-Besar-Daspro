# from array_csv import user
# File ini merupakan semua fungsi utama pada F02 dan F03 dan bonus FB01
from helpbase import *
aksesadmin = False #untuk menandakan apakah role user sekarang adalah admin/user
idcurrentuser = None #id dari user yang login sekarang, digunakan sebagai parameter
                    #dari fungsi yang memerlukan id user
# Deskripsi : Register

# Admin dapat mendaftarkan pengguna baru dengan memasukkan nama, username,
# dan password. Pengguna yang mendaftar otomatis memiliki role “user”.
# Pastikan username bersifat unik. Fungsi ini tidak dapat membuat user dengan
# role admin; untuk membuat user admin dapat mengedit file penyimpanan.
# Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”,
# dan angka 0-9.

# akses: admin
# >>> register
def validasi_reg(username_user):
    for i in range(length(username_user)):
        kondisi_salah = (0 <= ord(username_user[i]) <= 44 or 46 <= ord(username_user[i]) <= 47 or 58 <= ord(username_user[i]) <= 64 or 91 <= ord(username_user[i]) <= 94 or ord(username_user[i]) == 96 or 123 <= ord(username_user[i]) <= 127)
        if kondisi_salah:
            return False
    return True

def register(user_data):
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    while validasi_reg(username) == False:
        print("Username hanya boleh mengandung alfabet (A-Z & a-z), underscore (_), strip (-), dan angka (0-9)")
        nama = input("Masukkan nama: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    else:
        for row in user_data:
            if row[1] == username :
                print('Username', username, 'sudah terpakai, silakan menggunakan username lain')
                break
            else:
                user_id = int(row[0]) + 1
                user_id = str(user_id)
                user_baru = [user_id,username,nama,password,'User','0']
        print('Username', username, 'telah berhasil register ke dalam “Binomo”.')
        user_data += user_baru
    return user_data

# Deskripsi: Login

# Saat masuk ke dalam aplikasi, pengguna bisa login dengan memasukkan username dan password.
# Bila username dan password yang diinput cocok dengan username dan password pada file user,
# maka pengguna berhasil login. Untuk alur login dibebaskan;
# tidak harus mengetik “login” dulu diperbolehkan (misal, ketika sistem menyala user diwajibkan login,
# namun pastikan kalau belum login tidak bisa melakukan apa-apa selain login).

# akses: admin dan user
# >>> login
def login(user):
    while True:
        username_input = input("Masukkan username : ")
       # password_input = cipher_pass(input("Masukkan password : "))
        password_input = input("Masukkan password : ")

        for row in user:
            if row[1] == username_input and row[3] == password_input:
                print('Halo ' + username_input + '! Selamat datang di "Binomo".')
                if row[4] == 'Admin':
                    aksesadmin = True
                else:
                    aksesadmin = False
                idcurrentuser = int(row[0])
                return (aksesadmin,idcurrentuser)
                #akses['akun'] = data
        print("Password atau username salah atau tidak ditemukan.")
