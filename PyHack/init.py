from exploit import *
import os

def list_files():
    with open('exploits.t', 'r') as f:
        print(f.read())


while True:
    tmp = sp.call('cls',shell=True)
    list_files()
  
    f = input('Enter an exploit name: ')
    if f == 'geckoX':
        geckoX()
    elif f == 'dwrite':
        dwrite()
    elif f == 'dreada':
        dreada()
    elif f == 'db':
        db()
    else:
        print('unable to find that exploit.')
    tmp = sp.call('pause',shell=True)
