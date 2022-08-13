import json

name = input('Package name: ')
vers = input('Version: ')
exef = input('(main) executable file: ')

dipe = []
print('\nInsert package dependencies, leave empty to stop')
while 1:
    dname = input('Name: ')
    if dname == '':
        break
    
    dver = input('Version: ')
    if dver == '':
        break

    dipe.append({"name": dname, "version": dversion})

with open('descriptor', 'w') as f:
    f.write(json.dumps(
            {
                 "name": name,
                 "version": vers,
                 "execute": exef,
                 "dependencies": dipe
            }
        ))



