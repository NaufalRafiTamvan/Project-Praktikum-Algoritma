# Program Untuk Mengolah Data Harga Saham
Saham = [["TLKM", 18000], ["BBCA", 28000], ["BBRI", 21000]]


# Fungsi Untuk Menampilkan Semua Data
def list_Saham():
    i = 0
    for item in Saham:
        print("# " + str(i) + " | " + "Saham " + item[0] + " | " + "Harga " + str(item[1]) + " #")
        i += 1


# Memasukkan Saham Baru
def input_Saham():
    x, y = input("Nama dan Harga Saham: ").split()
    Saham.append([x, y])


# Mengedit Data Saham
def edit_data():
    list_Saham()
    i = int(input("Inputkan ID Saham: "))
    if i > len(Saham):
        print("ID salah")
    else:
        a, b = input("Nama dan Harga Saham: ").split()
        Saham[i] = [a, b]


# Menghapus Data()
def delete_data():
    list_Saham()
    i = int(input("Inputkan ID Saham: "))
    if i > len(Saham):
        print("ID salah")
    else:
        Saham.remove(Saham[i])


# Tampilan Menu Saham
def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] List Saham")
    print("[2] Input Saham")
    print("[3] Edit Saham")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = int(input("PILIH MENU> "))
    print("\n")

    if menu == 1:
        list_Saham()
    elif menu == 2:
        input_Saham()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Salah Pilih Mas Bro!!!")


if __name__ == "__main__":

    while True:
        show_menu()
