#!/usr/bin/python3


import socket


print("\033[1;31m"+"┏┳┓╻ ╻╻┏━┓")
print("\033[1;31m"+"┃┃┃┗┳┛┃┣━┛")
print("\033[1;31m"+"╹ ╹ ╹ ╹╹ ")


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("\033[1;34m"+"Creada por S3RGI09 (Sergio Casero Verdial)")
print("\033[1;36m"+"--------------------------------------")
print("\033[1;33m"+"El nombre de tu ordenador es: " + hostname)
print("\033[1;31m"+"Tu direccion IP es: " + ip)
print("\033[1;36m"+"--------------------------------------")
