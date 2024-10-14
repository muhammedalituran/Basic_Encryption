# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:35:01 2023

@author: ali.turan
"""
"""
16 haneli sayı ve büyük küçük harflerden oluşan random key üretmeyi sağlayan 
modül.
"""
import random


def keyGenerator() -> str:
    """16 haneli random bir key üreten fonksiyon
    
    Returns
    -------
    str
        16 haneli random key.

    """
    key = [] #Key değerlerini barındıracak olan liste.
    alphabet = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890"
    for i in range(0, 16):
        index = random.randint(0, 59)
        key.append(alphabet[index])
        
    return ''.join(key)
