import argparse
import sys
import os

def load():
    parser = argparse.ArgumentParser()

    parser.add_argument("nama_folder")
    args=parser.parse_args()

    input_path = args.nama_folder

    if not os.path.isdir(input_path):
        print('Folder ' + input_path +' tidak ditemukan')
        sys.exit()
    else:
        print('Selamat datang di antarmuka Binomo')
        #change_to_array(input_path+'game.csv')
        #change_to_array(input_path+'user.csv')
        #change_to_array(input_path+'riwayat.csv')
        #change_to_array(input_path+'kepemilikan.csv')