# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:13:33 2023

@author: ali.turan
"""

import encryption_decryption as en_de
import random_key_generator
import configparser

config = configparser.ConfigParser()

config.add_section("INFO")

key = random_key_generator.keyGenerator()
#Random key değerini ilgili kütüphaneden alır.

config.set("INFO", "key", key)

with open("keys/config.ini", 'w') as configfile:
    config.write(configfile)
#Alınan key değerini config.ini dosyasına kaydeder.

print(f"key: {key}")

crypted_word = en_de.createEnDeCrypted(key)
#Encryption ve Decryption için kullanılacak dictionary yapısını oluşturur.

print(f"Encrypted Word: {crypted_word['encrypt']}")
print(f"Decrypted Word: {crypted_word['decrypt']}")

encrypted_password = en_de.encryptor("@Deneme123$#&", crypted_word['encrypt'])
#Verilen stringi encrypt eder.

print(f"Encrypted Password: {encrypted_password}")

decrypted_password = en_de.decryptor(encrypted_password, crypted_word['decrypt'])
#Verilen encrypted stringi decrypt eder.

print(f"Decrypted password: {decrypted_password}")
