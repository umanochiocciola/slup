# slup

summary:</br>

[setup instructions](https://github.com/umanochiocciola/slup#setup-instructions)</br>
[usage instructions](https://github.com/umanochiocciola/slup#usage-instructions)</br>
[slup creation instructions](https://github.com/umanochiocciola/slup#slup-creation-instructions)</br>
[mod applications](https://github.com/umanochiocciola/slup#mod-applications)</br>

## setup instructions


run theese commands to get slup up and running
>  wget https://github.com/umanochiocciola/slup/raw/main/SLUP.zip</br>
  unzip SLUP.zip</br>
  cd SLUP</br>
  sudo sh setup_slup.sh</br>

to clean up,

> cd ..
  rm -r SLUP
  rm SLUP.zip

you have now added `slup` and `Rslup` commands


## usage instructions


to install a slup:</br>
run <code> slup install NAME</code><br>
it will
- resolve dependencies
- add NAME command and its assets
- clean up
 
to remove a slup:</br>
run <code> slup install NAME</code><br>
it will 
- remove NAME command and its assets
it WON'T
- check if any other slup was depending on it

## slup creation instructions

to create a slup package, first of all create a directory named exactly as your package[1^] like this

expected directory:</br>
```
slupname/
        /descriptor
        /(main executable)
        /(assets)/            (optional)
               / all the libraries, images and stuff you may need
        /readme               (optional)
```

(in the readme write non slup dependencies and whatever you want to be printed at the end of the installation)

the descriptor file will tell slup installer what to do,</br>
fill it like this

expected descriptor file content:</br>
```
{
    "name"         : "YourPackageName",
    "version"      : "0.0.0 and so on",
    
    "execute"      : "main executable file",
    
    
    "dependencies" : [
        {
            "name"    : "WhateverDependency",
            "version" : "0.0.0 and so on",
        },
        # only slup dependencies, not things installed by other means. You need to ask polightely the user to resolve them by themselves
    ],
    
    #optional
    "assets"       : "relative path to your assets folder, in the example above (assets)",

}
```
[^1]: where YourPackageName is identical to your directory name

when everything is ready, commit your package

commiting slup:</br>

1. zip your package directory (structured as described on 'expected directory') and change the `.zip` to `.slup`
2. (if compiled language) prepare a folder (named as you package) with all your source code and clear instructions on how to compie/run it
3. upload your .slup file directly as /YourPackage.slup in this repository
4. (if compiled language) upload your source code folder as /sources/YourPackage in this repository
5. start pull request! Mods will review and admit it in the main branch as soon as possible

## Mod appliactions
  If you have a general programming knowledge and wanna help, please consider applying for mod.</br>
  Your chores will be:
  - check (possibly on a chroot or virtual machine) user submitted executables
  - check that the submitted source code compiles to the user submitted executable
  - check descriptor sintax and directory structure
  - if everything is ok and nothing funny is going on, merge the pull request
  
  to apply, email me [here](lorenzomari22@gmail.com)
  

