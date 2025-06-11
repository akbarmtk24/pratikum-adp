from termcolor import cprint, colored
import os

os.system ('cls')

for i in range(5):
    merah = 31 + i * 2
    cprint(" " * merah + colored(" " * 19, 'red', 'on_red'))

print("")  

for i in range(5):
    jarak = 17 - i * 2
    biru = colored(" " * 17, 'blue', 'on_blue')
    hijau = colored(" " * 19, 'green', 'on_green')
    cprint(" " * jarak + biru + " " * 5 + hijau)

for i in range(3):
    jarak = 7 - i * 2
    biru = colored(" " * 17, 'blue', 'on_blue')
    cprint(" " * jarak + biru)


cprint(" " * 52 + colored(" "*7, 'white', 'on_white'))   
cprint(" " * 48 + colored(" "*13, 'white', 'on_white'))    
cprint(" " * 46 + colored(" "*17, 'white', 'on_white'))    
cprint(" " * 46 + colored(" "*18, 'white', 'on_white'))    
cprint(" " * 38 + colored(" "*4, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))    
cprint(" " * 34 + colored(" "*9, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))    
cprint(" " * 30 + colored(" "*15, 'white', 'on_white') + " " * 6 + colored(" "*17, 'white', 'on_white'))   
cprint(" " * 28 + colored(" "*18, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))  
cprint(" " * 29 + colored(" "*18, 'white', 'on_white') + " " * 6 + colored(" "*17, 'white', 'on_white'))    
cprint(" " * 20 + colored(" "*4, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))   
cprint(" " * 18 + colored(" "*8, 'white', 'on_white') + " " * 6 + colored(" "*17, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))   
cprint(" " * 16 + colored(" "*12, 'white', 'on_white') + " " * 6 + colored(" "*16, 'white', 'on_white') + " " * 6 + colored(" "*18, 'white', 'on_white'))  

