# import httpx
# import os
# from pprint import pprint
# url = 'https://jsonplaceholder.typicode.com/users'
# response = httpx.get(url=url)
# data = response.json()
# # os.mkdir("users")
# os.chdir("users")
# for i in data:
#     with open(f"{i['username']}.csv", 'w') as f:
#         f.write(f"id: {i['id']}\n")
#         f.write(f"username: {i['username']}\n")
#         f.write(f"email: {i['email']}\n")
#         f.write(f"phone: {i['phone']}\n")
#         f.write(f"website: {i['website']}\n")
#         f.write(f"company: {i['company']}\n")


# Lists = ordered, mutable, allows dublicate elements
# Tuple = ordered, immutable, allows dublicate elements
# dictionary = key-value pairs, unordered, mutable
# set = unordered, muatable, no duplicates
# strings = ordered, immutable, text represention
# collections = counter, namedtuple, ordereddict, defaultdict, deque
# iteratools = product, permutation, combination, accumulate, groupby, and infinite iterators
