from sys import argv
from os import path, system
import json

def main(action, slupfile, *garbage):

    if action == 'install':
        install(slupfile)

def GetInstalled():
    with open("/usr/slup/installed_slups", 'r') as f:
        installed = json.loads(f.read())
    
    return installed

def addInstalled(name, version):
    with open("/usr/slup/installed_slups", 'r') as f:
        installed = json.loads(f.read())
    
    installed.append({"name": name, "version": version})
    
    with open("/usr/slup/installed_slups", 'w') as f:
        f.write(json.dumps(installed))
        

def install(slupfile):
    slupfile = slupfile+'.slup'
    
    if not path.exists(slupfile):
        error('given slupfile doesn\'t exist')

    system(f'unzip {slupfile}')
    slup_path = path.abspath(''.join(slupfile.split('.')[:-1]))
    
    try:
        with open(f"{slup_path}/descriptor", 'r') as f:
            descriptor = json.loads(f.read())
    except Exception as e:
        error('Invalid or missing descriptor (', e, ')')
    
    
    try:
        installed = GetInstalled()
        for i in descriptor["dependencies"]:
            if not i in installed:
                error("Unresolved dependency:", i["name"], 'version', i["version"])


        system(f'mv "{slup_path}/{descriptor["execute"]}" /usr/bin')
        system(f'chmod +x /usr/bin/{descriptor["execute"]}')

        addInstalled(descriptor["name"], descriptor["version"])
        
    except Exception as e:
        error("Invalid package descriptor (", e, ')')
    
    
    system(f'rm -r {slup_path}')
    print('Done!')



def error(*msg):
    print('////////')
    print(*msg)
    exit(1)







if len(argv) < 3:
    error("insufficient arguments")


if __name__ == "__main__":
    main(*argv[1:])
