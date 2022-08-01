#!/usr/bin/python3

# Importa la libreria per l'utilizzo delle regex 
import re

file = open("iplist.txt", "r") # Apri il file in read
lines = file.readlines() #leggi ogni riga
re_ip = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
 
for line in lines: #Per ogni riga
    ip = re.findall(re_ip,line)
    #print(ip)
    if re.match(r'^\s*$', line): #se ha degli spazi
        continue #salta
    if ip: # se ip
        print(',' .join(ip)) #stampa a video
        