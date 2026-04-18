#1
def teskari(royxat):
    return royxat[::-1]

#2
import random

def random_tartib(royxat):
    random.shuffle(royxat)
    return royxat

#3
def katta_harf(matn):
    return matn.upper()

#4
def soz_soni(matn):
    return len(matn.split())

#5
def mavjudmi(royxat, qiymat):
    return qiymat in royxat
