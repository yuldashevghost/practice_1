import os
from time import sleep

command_list = ['ls', 'touch', 'mkdir', 'cd', 'move', '\\q']
status = True
timer = True


def ls():
    print(f"- {os.getcwd()} manzildagi fayllar va papkalar ro'yxati")
    print(" -", *os.listdir(os.getcwd()))
    if timer:
        sleep(10)
        os.system('cls')


def touch():
    try:
        filename = input("- Yangi fayl nomini kiriting: ")
        open(filename, 'x')
    except FileExistsError:
        print(" - Bunday fayl avvaldan yaratilgan. Bunday nom bilan yangi fayl yaratolmaysiz.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- \"{os.getcwd()+'//'+filename}\" nomli fayl muvaffaqqiyatli hosil qilindi")
    if timer:
        sleep(7)
        os.system('cls')


def mkdir():
    try:
        dname = input("- Yangi papka nomini kiriting: ")
        os.mkdir(dname)
    except FileExistsError:
        print("- Bunday papka avvaldan yaratilgan. Bunday nom bilan yangi papka yaratolmaysiz.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- {dname} nomli papka muvaffaqqiyatli yaratildi")
    if timer:
        sleep(7)
        os.system('cls')



def cd():
    try:
        directory = input("- Yangi joylashunvi kiriting: ")
        os.chdir(directory)
    except FileNotFoundError:
        print("- Bunday manzil mavjud emas")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"{os.getcwd()} - Joylashuv o'zgartirildi")
    if timer:
        sleep(6)
        os.system('cls')


def move():
    try:
        filename = input("- Ko'chirmoqchi bo'lgan faylingiz manzilini kiriting: ")
        dest = input("- Fayl uchun yangi manzilni kiriting: ")
        os.rename(filename, dest)
    except FileExistsError:
        print(
            "- Ko'chirish jarayonida xatolik yuz berdi.")
    except FileNotFoundError:
        print("- Bunday fayl topilmadi.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print("- Muvaffaqqiyatli ko'chirildi")
    if timer:
        sleep(7)
        os.system('cls')


while status:
    command = input("\n- Buyruqni kiriting: ")
    if command in command_list:
        if command == 'ls':
            ls()
        elif command == 'touch':
            touch()
        elif command == 'mkdir':
            mkdir()
        elif command == 'cd':
            cd()
        elif command == 'move':
            move()
        elif command == '\\q':
            status = False
    else:
        print("- Buyruq noto'g'ri kitirildi. Qayta kiriting")
        print("  ESLATMA: help buyrug'i orqali buyruqlar ro'yxatini olishingiz mumkin")
        input("  Davom etish uchun ENTER tugmasini bosing...")
        continue

print("Dastur yakunlandi")