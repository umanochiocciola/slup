# slup

summary:</br>

[setup instructions](https://github.com/umanochiocciola/slup#setup-instructions)</br>
[usage instructions](https://github.com/umanochiocciola/slup#usage-instructions)</br>
[slup creation instructions](https://github.com/umanochiocciola/slup#slup-creation-instructions)</br>
[mod applications](https://github.com/umanochiocciola/slup#mod-applications)</br>

## setup instructions

>  wget https://github.com/umanochiocciola/slup/raw/main/SLUP.zip</br>
  unzip SLUP.zip</br>
  cd SLUP</br>
  sudo sh setup_slup.sh</br>


## usage instructions

install a slup:</br>
<code>  slup install NAME</code><br>
 
remove a slup:</br>
<code>  slup install NAME</code><br>

## slup creation instructions

expected directory:</br>
```
slupname/
        /descriptor
        /(main executable)
        /assets/            (optional)
               / whatever code, images and stuff you may need
```

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
    ],
    
    #optional
    "assets"       : "relative path to your assets folder",

}
```
commiting slup:</br>

1. zip your package directory (structured as described on 'expected directory') and change the `.zip` to `.slup`
2. prepare a folder (named as you package) with all your source code and clear instructions on how to compie/run it
3. upload your .slup file directly as /YourPackage.slup in this repository
4. upload your source code folder as /sources/YourPackage in this repository
5. start pull request! Mods will review and admit it in the main branch as soon as possible

## Mod appliactions
  If you have a general programming knowledge and wanna help, please consider applying for mod.</br>
  Your chores will be:
  - check (possibly on a chroot or virtual machine) user submitted executables
  - check that the submitted source code compiles to the user submitted executable
  - check descriptor sintax and directory structure
  - if everything is ok and nothing funny is going on, merge the pull request
  
  to apply, email me [here](lorenzomari22@gmail.com)
  

