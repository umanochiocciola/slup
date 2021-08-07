from os import popen, system
from sys import argv


def install(name):
    system(f'wget https://github.com/umanochiocciola/slup/raw/main/{name}.slup')
        
    CHK=popen(f'slup install {name}').read()

    CHK = CHK.split('////////')[1]
    
    try:

        if CHK[:22] == 'Unresolved dependency:':
            Dname = CHK.split(' ')[1]
            install(Dname)
            return 0

    except:
        print(CHK)
        return 1

name = argv[1]
done = 0
while not done:
    done = install(name)