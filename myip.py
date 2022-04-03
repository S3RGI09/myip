#!/usr/bin/python3


import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Creada por S3RGI09 (Sergio Casero Verdial)")
print("--------------------------------------")
print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es: " + ip)
print("--------------------------------------")
