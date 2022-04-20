
from autentikasi import *
from allfunction import *
from helpbase import *

kepemilikan_data =[]
game_data = []
user_data = []
riwayat_data = []
aksesadmin = False
idcurrentuser = None

kepemilikan_data,game_data,user_data,riwayat_data,nama_folder= load()
print(kepemilikan_data)
print(game_data)
print(user_data)
print(riwayat_data)

# folder_name merupakan nama_folder pada F14
#consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name = load_data()

if __name__ == '__main__':
    finish = False
    perubahan = False
    if nama_folder != None:
        akses = login(user_data)
        aksesadmin = akses[0]
        idcurrentuser = akses[1]
        print()
        print()
        print("Berikut perintah yang dapat tersedia:\n")

        help(aksesadmin)

        print()
        print()
    if(aksesadmin):
        print("Y")
    else:
        print("N")
    print(idcurrentuser)
    while not finish:
        if nama_folder == None:
            # folder tidak ada
            finish = True
            continue

        perintah = input('>>> ')
        # khusus untuk prosedur register akan save data secara otomatis
        if perintah == 'register':
            if aksesadmin == True:
                user_data = register(user_data)
                perubahan = True
            else:
                print("Anda bukan Admin")

        elif perintah == 'tambah_game':
            if aksesadmin == True:
                game_data = tambah_game(game_data)
                perubahan = True
                print(game_data)
            else:
                print("Anda bukan Admin")


        elif perintah == 'ubah_game':
            if aksesadmin == True:
                game_data = ubah_game(game_data)
                perubahan = True
                print(game_data)
            else:
                print("Anda bukan Admin")


        elif perintah == 'ubah_stok':
            if aksesadmin == True:
                game_data = ubah_stok(game_data)
                perubahan = True
                print(game_data)
            else:
                print("Anda bukan Admin")

        elif perintah == 'list_game_toko':
            list_game_toko(game_data)

        elif perintah == 'buy_game': #masih bermasalah
            if aksesadmin == False:
                kepemilikan_data,game_data,user_data,riwayat_data = buy_game(idcurrentuser,kepemilikan_data,game_data,user_data,riwayat_data)
                perubahan = True
            else:
                print("Anda bukan User")

        elif perintah == 'list_game':
            if aksesadmin == False:
                list_game(idcurrentuser,kepemilikan_data, game_data)
            else:
                print("Anda bukan User")

        elif perintah == 'search_my_game':
            if aksesadmin == False:
                search_my_game(idcurrentuser,kepemilikan_data,game_data)
            else:
                print("Anda bukan User")

        elif perintah == 'search_game_at_store':
            search_game_at_store(game_data)

        elif perintah == 'topup':
            if aksesadmin == True:
                topup(user_data)
                print(user_data)
                perubahan = True
            else:
                print("Anda bukan Admin")

        elif perintah == 'riwayat':
            if aksesadmin == False:
                riwayat(idcurrentuser,riwayat_data)
            else:
                print("Anda bukan User")

        elif perintah == 'help':
            help(aksesadmin)

        elif perintah == 'exit':
            pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang telah diubah? (y/n) "))
            while not ((pilihan == 'Y') or (pilihan == 'y') or (pilihan == 'N') or (pilihan == 'n')):
                pilihan = str(input("Apakah Anda mau melakukan penyimpanan file yang telah diubah? (y/n) "))
            if (pilihan == 'Y') or (pilihan == 'y'):
                save(kepemilikan_data,game_data,user_data,riwayat_data,nama_folder)
            finish = True

        elif perintah == 'save':
            if(os.path.isdir('data')):
                print("Folder ada")
            else:
                print("Folder tidak ada")
            save(kepemilikan_data,game_data,user_data,riwayat_data,nama_folder)

        else :
            print("Perintah anda tidak valid")

    print("Program selesai")



