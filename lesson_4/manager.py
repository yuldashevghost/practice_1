# import json
# import os
#
# class FileManager:
#     def __init__(self, path, mode):
#         self.path = path
#         self.mode = mode
#
#     def __enter__(self):
#         file = open(file=self.path, mode=self.mode)
#         self.file = file
#         return file
#
#     def __exit__(self, *args, **kwargs):
#         self.file.close()
#
#
#
# import requests
# from pprint import pprint
# url = 'https://randomuser.me/api/'
# response = requests.get(url=url).json()
# data = response['results'][0]['picture']
# # os.mkdir('images')
# os.chdir('images')
# for i in data:
#     with open(f'{i}.jpg', 'wb') as f:
#         idata = requests.get(url=data[i]).content
#         f.write(idata)
import datetime
import json
import os


# @contextmanager
#
# def file_manager(file, m):
#     file = open(file, m)
#
#     try:
#         with open("log.txt", "a") as f:
#             f.write(f"file {datetime.datetime.now().strftime('%d %H %M %S')} da {m} rejimda ochildi")
#         yield file
#     finally:
#         with open('log.txt' 'w+') as f:
#             f.write(f"file {datetime.datetime.now()}da yopildi")
#         file.close()

if __name__ == "__main__":
    os.chdir('jokes.json')
    with file_manager('jokes.json') as f:
        data = json.load(f)
        print(data)