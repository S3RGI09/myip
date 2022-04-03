#!/usr/bin/python3


import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("--------------------------------------")
print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es: " + ip)
print("--------------------------------------")
