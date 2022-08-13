#! /bin/python3

from os import popen, path, system
from sys import argv

def get_repos():
    with open("/usr/slup/repos", 'r') as f:
        repos = json.load(f)



def install(name):
    if not MainCollected:
        print('collecting', name)

        for REPO in repos:

            system(f'wget {REPO}{name}.slup -q --show-progress')
            if not path.exists(name+'.slup'):
                print('unable to find', name); continue

            break
     
    CHK=popen(f'Rslup install {name}.slup').read() # don't remember what chk stands for lol

    done = 0
    try:
        CHK = CHK.split('////////')[1].strip('\n').strip(' ')
        
        try:
            # extremely dirty, did long time ago, don't care
            if CHK[:22] == 'Unresolved dependency:':
                Dname = CHK.split(' ')[2]
                print('[resolving dependency] ', Dname)
                install(Dname)
                return 0
        
        except:0 # cringe 
    except:0     # cringe wtf
    
    print(CHK)
    
    return 1

def remove(name):
    CHK = popen(f'Rslup remove {name}').read()
    
    if '////////' in CHK:
        print(CHK.split('////////')[1].strip('\n').strip(' '))
    
    print(CHK)
    return 1

try:
    action = argv[1]
    name = argv[2]
except:
    print('insufficent arguments'); exit(1)

try:
    action = eval(action)
except:
    print('invalid action argument'); exit(1)

done = 0
MainCollected = 0
while not done:
    done = action(name)
    if not MainCollected: MainCollected = 1
    #print('---------------------------',done)