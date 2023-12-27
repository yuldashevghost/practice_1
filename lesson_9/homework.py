import os

import requests
from email.message import EmailMessage
import smtplib
from passwords import password

# ----  task-1   -----
# url_men = "https://randomuser.me/api/portraits/men/"
# url_women = "https://randomuser.me/api/portraits/women/"
# os.chdir("photos")
# for i in range(1, 6):
#     imgdata = requests.get(f"{url_men}{i}.jpg").content
#     with open(f"{i}.jpg", 'wb') as image:
#         image.write(imgdata)
#         print(f"")
#
# for i in range(6, 11):
#     imgdata = requests.get(f"{url_women}{i}.jpg").content
#     with open(f"{i}.jpg", 'wb') as image:
#         image.write(imgdata)
# os.chdir("..")
#
# ---- task-2  ----
with open("emails.csv", "r") as f:
    emails = list(map(lambda x: x.split(',')[1], f.read().splitlines()[1:]))
    # print(emails)

# ---- task-3 =--

server = "smtp.gmail.com"
sender = "misoluchun23@gmail.com"
receivers = emails

message = EmailMessage()
message["From"] = sender
message["To"] = receivers
message["Subject"] = "New photos!"
message.set_content("New photos uploaded to server")

dir = os.listdir("photos")
os.chdir("photos")
for i in dir:
    with open(i, 'rb') as image:
        message.add_attachment(image.read(), maintype='image', subtype="jpg", filename=i)


with smtplib.SMTP_SSL(server, 465) as server:
    server.login(sender, password)
    server.send_message(message)
    print("Email sent!")
