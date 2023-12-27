import json
from multiprocessing import Process


def get_num(file_name: str):
    n = 0
    for i in range(1, 11):
        if i == 10:
            with open(f'{file_name}/0{i}.txt', 'r+') as f:
                l = f.read().split()
                for j in l:
                    if j.isnumeric():
                        n += int(j)
        else:
            with open(f'{file_name}/00{i}.txt', 'r+') as f:
                l = f.read().split()
                for j in l:
                    if j.isdigit():
                        n += int(j)
    print(f"Sonlarning yig'indisi: {n}")



def get_upper(file_name: str):
    uppers = []
    for i in range(1,11):
        if i ==10:
            with open(f'{file_name}/0{i}.txt', 'r+') as f:
                l = f.read().split()
                for i in l:
                    if i[0].isupper():
                        uppers.append(i)

        else:
            with open(f'{file_name}/00{i}.txt', 'r+') as f:
                l = f.read().split()
                for i in l:
                    if i[0].isupper():
                        uppers.append(i)
    with open('upper.txt', 'w+') as f:
        f.write(f'{uppers}')
    print('upper.txt ga yozildi !!!')




def count_chr(file_name):
    d = {}
    for i in range(128):
        d.update({chr(i): 0})
    d.update({'\n': 0})
    for i in range(1, 11):
        if i == 10:
            with open(f'{file_name}/0{i}.txt', 'r+') as f:
                r = f.read()
                for o in r:
                    if o in d.keys():
                        d[o] += 1
        else:
            with open(f'{file_name}/00{i}.txt', 'r+') as f:
                r = f.read()
                # print(r)
                for o in r:
                    if o in d.keys():
                        d[o] += 1
    with open('chars.json', 'w+') as f:
        json.dump(d, f, indent=4)
    print('chars.json ga yozildi !!!')

if __name__ == '__main__':
    file_name = 'descriptions'
    p1 = Process(target=get_num, args=(file_name,))
    p1.start()
    p1.join()
    p2 = Process(target=get_upper,args=(file_name,))
    p2.start()
    p2.join()
    p3 = Process(target=count_chr,args=(file_name,))
    p3.start()
    p3.join()