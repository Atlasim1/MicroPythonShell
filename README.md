# MicroPython Shell
This program for the Raspberry Pi Pico Microcontroller Running MicroPython. (May work on other platforms)
#
You can easily write files, do file management and run programs using simple commands.

# Features

- Reboot Device with "Machine" Module (May not work on all devices)

- Write file based on line-by-line input

- File management commands such as : 
  - ls
  - cd
  - del
  - rmdir
  - mkdir
  - rename

- Run Programs

- Erase all files from device

- Output File Contents

- Do Memory Management

- Fill Memory With Garbage :)

- Install And Remove programs with built-in tools

# Install

Installing usually depends on how you transfer files to your micro controller. 

## Required Files : 
- Add "cmd.py" to Root folder (/)
- Add "shell.py" to Root folder (/)
- Optionally, add contents of "boot.py" to "boot.py" file in device (this adds a "shell()" Function for quick starting )

## Device Dependencies : 

### Imports
- os, utime, machine, sys (on micropython)
- micropython port of cmd module (provided as cmd.py)
### Tested Compatible Devices
- Raspberry Pi Pico (the first one, if you're in the future)
- nothing else because i cant be bothered

# Command Reference 
Command (Argument), [optional argument]

*Currently, "help" and "?" Do not work because of difficulties
#

Currently, Using a command that is not listed Tries to load it as a Shodule (MpSh Program) If that fails, It throws an error

---

- reset 
  - Usage : > reset [-s][-f]
    - -f : Reboot machine in firmware mode 
    - -s : Do a soft reset
    - noarg : do a normal hard reset (May terminate serial connection)
  - Does a reset of a certain type (May not work on all devices)
- ls
  - Usage : > ls
  - List the current directory's contents
- exit
  - Usage : > exit
  - Exits the shell
- cd
  - Usage : > cd (directory)
  - Goes to specified directory
- del
  - Usage : > del (file)
  - Deletes Specified file (cannot delete directory)
- rmdir
  - Usage : > rmdir (directory)
  - Removes Specified Directory
- mkdir
  - Usage : > mkdir (directoryname)
  - Makes a directory with the specified name
- rename
  - Usage : > rename (file) (newname)
  - Renames a file Or Directory
- run
  - Usage : > run (program)
  - runs a file as a python script 
- format
  - Usage : > format [--all]
  - erases all files on device
  - --all : Including "shell.py" and "cmd.py"
- out
  - Usage : > out (file)
  - Outputs file contents
- writefile
  - Usage : > writefile
  - Writes a file (one line per line)
- loadmod
  - Usage : > loadmod (module)
  - Loads A Shodule (Program For MpSh)
- mem 
  - Usage : > mem (option)
  - mem dump > Shows Loaded Modules
  - mem fill > Fills memory with useless variables
  - mem unfill > Unloads all modules
  - mem free > Frees up some memory
  - mem avail > Shows available Memory
  - mem restore > Attempts to restore Imports
  - Does Many Things related to imports and modules
- programs
  - Usage : > programs (option)
  - programs load > Installs a program **without** an install scirpt
  - programs list > Lists installed Programs
  - programs remove > Uninstalls a program
  - programs install > Installs a program **with** an install script
  - programs setup > Setup Installing programs (Should be done only once)
