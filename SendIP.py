import socket
import smtplib, ssl

email = "@gmail.com"
password = ""


context = ssl.create_default_context()
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
message = """\
Subject: Hi there

""" + str(IP_addres)

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls(context=context)
server.ehlo()
server.login(email, password)
server.sendmail(email, email, message)
