#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dobrodošli u pycharm restoran"

menu = {}

while True:
    jelo = raw_input("Koje jelo hoćete da žderete? ")
    cijena = raw_input("Unesite cijenu jela.")
    print "unjeli ste jelo : " + jelo + ", kojemu je cijena: " + cijena

    menu[jelo]= cijena

    new = raw_input("Želite li unesti novo jelo (da/ne)")

    if new == "ne" :
        break

menu_file = open("menu.txt" , "w+")
print "Menu :"
menu_file.write("%s: %s kn " % (jelo, menu[jelo]))
for jelo in menu :
    print jelo,  menu[jelo]


menu_file.write("%s: %s kn " % (jelo, menu[jelo]))


menu_file.close()

print "END"