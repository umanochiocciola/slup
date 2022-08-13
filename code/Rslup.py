#! /bin/python3

from sys import argv
from os import path, system
import json

def main(action, slupfile, *garbage):
 
    action = globals().get(action, nosuchaction)
    action(slupfile)


def nosuchaction(slupfile):
    error("Invalid action for", slupfile)


def GetInstalled():
    with open("/usr/slup/installed_slups", 'r') as f:
        installed = json.loads(f.read())
    
    return installed

def addInstalled(desc):
    print('added', desc['name'], 'to installed packages')
    with open("/usr/slup/installed_slups", 'r') as f:
        installed = json.loads(f.read())
    
    installed.append(desc)
    
    with open("/usr/slup/installed_slups", 'w') as f:
        f.write(json.dumps(installed))


def removeInstalled(desc):
    with open("/usr/slup/installed_slups", 'r') as f:
        installed = json.loads(f.read())
    
    installed.remove(desc)
    
    with open("/usr/slup/installed_slups", 'w') as f:
        f.write(json.dumps(installed))



def install(slupfile):
    print("installing "+slupfile)
    
    if not path.exists(slupfile):
        error('given slupfile doesn\'t exist')

    slupfolder='.'.join(slupfile.split('.')[:-1])
    print(slupfolder)
    if path.exists(slupfolder):
        system(f"rm -r {slupfolder}")

    print("unzippin'")
    system(f'unzip {slupfile} 2>/dev/null 1>&2')
    slup_path = path.abspath(slupfolder)
    print("-->", slup_path)
    system("ls "+slup_path)
    
    try:
        with open(f"{slup_path}/descriptor", 'r') as f:
            descriptor = json.loads(f.read())
    except Exception as e:
        error('Invalid or missing descriptor (', e, ')', clean=slup_path)
    
    
    try:
        installed = GetInstalled()
        
        for i in descriptor["dependencies"]:
            solved = 0
            for j in installed:
                if i['name'] == j['name'] and i['version'] == j['version']:
                    solved = 1
                    
            if not solved: error("Unresolved dependency:", i["name"], 'version', i["version"], clean=slup_path)


        if path.exists(f"/usr/bin/{descriptor['name']}"):
            print("A program with this name was already installed not through SLUP.")
            descriptor["name"]=''
            while not len(descriptor["name"]):
                try: descriptor["name"] = input("rename this slup (CTRL+C to abort installation): ")
                except: error("operation interrupted by user", clean=slup_path)

        system(f'mkdir /usr/slups/{descriptor["name"]}')
        #print(f'mv {slup_path}/{descriptor["name"]} /usr/slups/')
        system(f'mv {slup_path}/{descriptor["name"]} /usr/slups/')

        with open(f"/usr/bin/{descriptor['name']}", 'w') as f:
            f.write(f"#! /bin/bash\ncd /usr/slups/{descriptor['name']}\n./{descriptor['execute']}")

        system(f"chmod +x /usr/bin/{descriptor['name']}")

        addInstalled(descriptor)
        
    except Exception as e:
        error("Invalid package descriptor (", e, ')', clean=slup_path)
    
    
    try:
        with open(f'{slup_path}/readme', 'r') as f:
            readme = f.read()
    except:
        readme = 0
    
    system(f'rm -r {slup_path}')
    system(f'rm -r {slupfile}')
    
    if readme: print(' -----\n', readme, '\n -----')
    print('Done')


def remove(slupname):
    installed = GetInstalled()
    
    slup = 0
    for i in installed:
        #print(i['name'])
        if i['name'] == slupname:
            
            slup = i
            break
    
    if not slup:
        error('given slup is not installed')
    
    print(f'removing {slup["name"]}')
    
    ThereAreAssets = slup.get('assets', 0)
    
    system(f'rm /usr/bin/{slup["name"]}')
    if ThereAreAssets:
        system(f'rm /usr/slups/{slup["name"]}')
    
    removeInstalled(slup)
    print(f'{slup["name"]} succesfully removed')
    

def error(*msg, clean=0):
    if clean:
        print(f'remove {clean}')
        system(f'rm -r {clean}')
    print('////////')
    print(*msg)
    exit(1)




if len(argv) < 3:
    error("insufficient arguments")

if __name__ == "__main__":
    main(*argv[1:])
