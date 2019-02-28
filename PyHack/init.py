from exploits.geckoX import *
import os

def list_files():
    with open('exploits.t', 'r') as f:
        print(f.read())


while True:
    list_files()
  
    func = input('Enter an exploit name: ')
    if func == 'geckoX':
        geckoX()
    else:
        print('unable to find that exploit.')
