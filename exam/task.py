# import json
# import os
# import requests
# from pprint import pprint
#
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
# url = 'http://164.92.64.76/desc/'
# response = requests.get(url=url).json()
# data = response
# os.mkdir('images')
# os.chdir('images')
# for i in data:
#     with open(f'{i}.jpg', 'wb') as f:
#         idata = requests.get(url=data[i]).content
#         f.write(idata)
for i in range(1, 10):
    with open(f"descriptions/{i}.txt", "r") as f:
        data = f.read()

        print(data)