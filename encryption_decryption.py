import random
import numpy as np


def createEnDeCrypted(key: str) -> dict:
    """Şifreleme algoritması için girilen key değerine bağlı olarak random 
    şifreleme karakterlerini oluşturur.
    
    Aynı karakterin key-value çifti olarak tekrar denk gelmesini önlemek için 
    key-value değerleri ortadan ikiye ayrılmıştır.
    
    Parameters
    ----------
    key : str
        Encryption karakterlerinin oluşturulması için gereken seed'i sağlayan 
        key değeri.

    Returns
    -------
    dict
        Encryption ve decryption karakterlini içeren dictionary.
    """
    
    
    random.seed(key)#Random değerleri key değerine göre ayarlamayı sağlar.

    asciis = np.arange(32, 127)
    asciis = np.append(asciis, [230])
    #Şifrelemede kullanılacak karakterlerin ascii kodlarını barındıran np arrayi
    
    random.shuffle(asciis)#Karakterleri random olarak karıştırır.

    dict_encrypt_en = {}#Şifrelemede kullanılacak dictionary.
    value_list = []#Value değerlerinin depolandığı liste.

    for i in asciis:
        #Karakterleri key ve value olarak ortadan ikiye ayıran döngü.
        
        if len(dict_encrypt_en) < 48:
            dict_encrypt_en[f"{chr(i)}"] = ""
        else:
            value_list.append(chr(i))

    random.shuffle(value_list)
    j = 0

    for i in dict_encrypt_en:
        
        dict_encrypt_en[f"{i}"] = value_list[j]
        j += 1
        
    dict_encrypt_en_part2 = {v: k for k, v in dict_encrypt_en.items()}
    #Key ve value değerlerinin yerlerini değiştiren yapı.
    
    dict_encrypt_en.update(dict_encrypt_en_part2)
    #Part2'yi final haline ekleyerek bütün karakterler için key-value oluşturur.
    
    dict_decrypt_en = {v: k for k, v in dict_encrypt_en.items()}
    #Decryption için gereken dict yapısını key-value değerlerinin yeri
    #değiştirilerek oluşturur.
    
    return {"encrypt": dict_encrypt_en, "decrypt": dict_decrypt_en}


def encryptor(password: str, en_dict: dict) -> str:
    """Girilen Stringi Encrypt eden fonksiyon.

    Parameters
    ----------
    password : str
        Encrypt edilecek string.
    en_dict : dict
        Encryption için kullanıcalacak key-value değerlerini içeren dictionary.

    Returns
    -------
    str
        Encrypted string.

    """
    
    encrypted_password = []
    for i in range(0, len(password)):
        
        if password[i] in en_dict:
            encrypted_password.append(en_dict[f"{password[i]}"])
        else:
            encrypted_password.append(password[i])
    return ''.join(encrypted_password)


def decryptor(enc_password: str, de_dict: dict) -> str:
    """Şifrelenmiş stringi decrypte eden fonksiyon.

    Parameters
    ----------
    enc_password : str
        Encrypted string.
    de_dict : dict
        Decryption sağlayan karakterleri içeren dictionary.

    Returns
    -------
    str
        Decrypted string.

    """
    
    decryptedPassword = []
    for i in range(0, len(enc_password)):
        
        if enc_password[i] in de_dict:
            decryptedPassword.append(de_dict[f"{enc_password[i]}"])
        else:
            decryptedPassword.append(enc_password[i])
    return ''.join(decryptedPassword)
