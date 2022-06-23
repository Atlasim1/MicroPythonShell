import os, utime, machine, cmd, sys, gc

#Define shell Class
class pyshell(cmd.Cmd):
    #Required Values for cmd Lib
    intro = "MicroPython Shell \nType ? or help For Help"
    prompt = ">>> "
    
    def do_reset(self, arg):    #Reset commands to reset device
        try:
            if arg == "-s":
                machine.soft_reset()
            elif arg == "-f":
                machine.bootloader()
            else:
                conf = input("Reset The Machine? (May Disconnect Serial Comms)")
                if conf == "y" or conf == "yes":
                    machine.reset
                else:
                    print("Cancelled Reset")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")

        
    def do_ls(self, arg):   #list currrent directory command
        try:
            temp = os.listdir()
            print("Directory of \"",os.getcwd(),"\" :")
            print(*temp, sep = " | ")   #temp = array of current dir contents  | sep = separator for * method
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
        
    def do_exit(self,arg):  #exit shell command
        try:
            temp = input("ExitShell?\n?>>")
            if temp == "yes" or temp == "y":
                print("Closed Shell")
                sys.exit()
            else:
                print("Canceled")
        except MemoryError:
            print("*** No Memory Available, Closing Anyways")
            sys.exit("Memory Failure")
        except NameError as error:
            print(f"*** Import Missing, Crashing To exit ({error})")
            raise NameError("Could not Load Required Module To Exit")
            
    def do_cd(self,arg):    #change dir command
        try:
            os.chdir(arg)
        except OSError:
            print("*** Invalid Directory")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
        
    def do_del(self,arg):   #delete file command
        try:
            print("Tip: Use rmdir To Delete Folders")
            temp = input(f"Do you Want to delete {arg}\n?>>")
            if temp == "y" or temp == "yes":
                os.remove(arg)
            else:
                print("Canceled")
        except OSError:
            print(" *** Incorrect Use Of Command")    
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
            
    def do_rmdir(self,arg): # delete directory command
        temp = input(f"Do you Want to delete {arg}\n?>>")
        if temp == "y" or temp == "yes":
            try:
                os.rmdir(arg)
            except OSError as error:
                print("*** ", error)
                print("*** Cannot Remove Directory\nTip : You must empty a directory before removing it")
            except MemoryError:
                print("*** No Memory Available")
            except NameError as error:
                print(f"*** Import Missing ({error})")
        else:
            print("Canceled")
            
    def do_mkdir(self,arg):     #make directory command
        try:
            os.mkdir(arg)
        except OSError:
            print("*** Incorrect Use Of Command")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
            
    def do_rename(self,arg):    # rename file command
        args = arg.split(" ")
        try:
            os.rename(args[0], args[1])
        except OSError:
            print("*** Incorrect Use Of Command")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
    
    def do_run(self,arg):       # run file commmand
        try:
            exec(open(arg).read())
        except OSError:
            print("*** File Not Found")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")

    def do_format(self,arg):    #remove every file on the device
        if arg == "--all": # if arg to delete all
            valid = input("Do you want to delete Every single file on this device INCLUDING THIS SHELL\nType: \"Yes Delete All\"\n!?> ")
            if valid == "Yes Delete All":
                cur = os.listdir()
                for x in range(len(cur)):
                    try: #except is directory
                        os.remove(cur[x]) # try to remove file
                        print("Removed",cur[x])
                    except OSError:
                        os.rmdir(cur[x]) # if failed, remove directory
                        print("Removed",cur[x])
                    except NameError as error:
                        print(f"*** Import Missing ({error})")
                print("Removed Every File\nDone!")
            else:
                print("Canceled")
        else:
            valid = input("Do you want to delete Every single file on this device Not including Shell\n!?>")
            if valid == "y" or valid == "yes":
                cur = os.listdir()
                for x in range(len(cur)):
                        if cur[x] == "shell.py" or cur[x] == "boot.py" or cur[x] == "cmd.py": # check if file is critical shell file 
                            x = x + 1 #if it is; dont delete it
                        else:# if it is delete it 
                            try: # try to except file is directory
                                os.remove(cur[x]) # remove file 
                                print("Removed",cur[x]) #log
                            except OSError: # will trigger if file is directory 
                                os.rmdir(cur[x]) #remove dir
                                print("Removed",cur[x]) #log
                            except NameError as error:
                                print(f"*** Import Missing ({error})")
                print("Removed Every File\nDone!")
            else:
                print("Canceled")
                
    def do_out(self,arg): #ouput contents of file command 
        try:
            cwd = os.getcwd()
            print("\n",open(f"{cwd}{arg}", "r").read(),"\n")
        except OSError:
            print("*** File Not Found")        
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
            
    def do_writefile(self,arg): # writes files
        print("File Input / Receive Program")
        filename = input("File Name >")
        file = open(filename, "a")
        while True:
            contents = input("CONTENTS (\"***!!!EXITTYPE!!!***\" To exit)> ")
            if contents == "***!!!EXITTYPE!!!***":
                file.close()
                break
            else:
                file.write(f"{contents}\n")
        
    def do_loadmod(self,args):
        try:
            os.rename(f"./{args}",f"/modules/{args}.py")
        except OSError:
            print("*** Bad File Name")
        except MemoryError:
            print("*** No Memory Available")    
        except NameError as error:
            print(f"*** Import Missing ({error})")
                    
    def do_mem(self,args):
        if args == "avail":
            free = gc.mem_free()
            print(f"Memory Available : {gc.mem_free()} Bytes")
        elif args == "free":
            old = gc.mem_free()
            gc.collect
            new = gc.mem_free()
            print(f"Collected {old - new} Bytes of garbage")
        elif args == "fill":
            print("Filling Memory")
            count = 1
            while True:
                try:
                    exec(f"useless{count} = \"f\"")
                except MemoryError:
                    break
                count = count + 1    
            print("Filled Memory! (You may have to fucking die)")
        elif args == "unfill":
            print("Unloading All Modules From Memory")
            number = 0
            todel = dir()
            while True:
                try:
                    exec(f"del {todel[number]}")
                    number = number + 1
                except IndexError:
                    print("Unloaded All Modules!")
                    break
        elif args == "dump":
            temp = dir()
            print(f"Memory Contents :")
            print(*temp, sep = " | ")
        elif args == "restore":
            print("Attempting to restore Memory Contents")
            exec("import os, utime, machine, cmd, sys, gc")
            print("Attempted to restore Memory Contents")
        else:
            print("*** Incorrect use of command ")
    
    def do_programs(self,args):
        argsls = args.split(" ")
        if argsls[0] == "load":
            try:
                os.rename(f"./{argsls[1]}",f"/modules/{argsls[1]}.prg")
            except OSError:
                print("*** Bad File Name")
            except MemoryError:
                print("*** No Memory Available")    
            except NameError as error:
                print(f"*** Import Missing ({error})")
        elif argsls[0] == "list": 
            try:
                temp = os.listdir("/modules/")
                print("Installed Programs : ")
                print(*temp, sep = " | ")     
            except OSError:
                print("*** Programs folder not located")
            except MemoryError:
                print("*** No Memory Available")      
            except NameError as error:
                print(f"*** Import Missing ({error})")
        elif argsls[0] == "remove":
            try:
                exec(open(f"/modules/uninst{argsls[1]}.rem").read())
            except OSError:
                try:
                    os.remove(f"/modules/{argsls[1]}.prg")
                except OSError:
                    print("*** Invalid Program")
        elif argsls[0] == "install":
            try:
                exec(open(f"{argsls[1]}.ins").read())
            except OSError:
                print("*** Invalid Install File\nTip : If your program dosent have an install file, use \"programs load\"")
        elif argsls[0] == "setup":
            try:
                os.mkdir("/modules")
                os.mkdir("/modules/uninst")
            except OSError:
                print("*** Programs aleready Setup")
        else:
            print("*** Incorrect Use Of Commands")
                    
    
    def default(self,args):
        try:
            exec(open(f"/modules/{args}.prg").read())
        except OSError:
            print("*** Bad command or Module Name")
        except MemoryError:
            print("*** No Memory Available")
        except NameError as error:
            print(f"*** Import Missing ({error})")
            
        # Runs program if is not imported                
if __name__ == "__main__":
    import os, utime, machine, cmd, sys, gc
    pyshell().cmdloop()