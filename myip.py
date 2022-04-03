#!/usr/bin/python3


import socket


print(" __  __       ___ ____ ")
print("|  \/  |_   _|_ _|  _ \ ")
print("| |\/| | | | || || |_) |")
print("| |  | | |_| || ||  __/ ")
print("|_|  |_|\__, |___|_|    ")
print("        |___/           ")


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Creada por S3RGI09 (Sergio Casero Verdial)")
print("--------------------------------------")
print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es: " + ip)
print("--------------------------------------")
