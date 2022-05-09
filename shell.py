import os, utime, machine, cmd, sys, gc

#Define shell Class
class pyshell(cmd.Cmd):
    #Required Values for cmd Lib
    intro = "MicroPython Shell \nType ? or help For Help"
    prompt = ">>>"
    
    def do_reset(self, arg):    #Reset commands to reset device
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

    def do_ls(self, arg):   #list currrent directory command
        temp = os.listdir()
        print("Directory of \"",os.getcwd(),"\" :")
        print(*temp, sep = " | ")   #temp = array of current dir contents  | sep = separator for * method
        
    def do_exit(self,arg):  #exit shell command
        temp = input("ExitShell?\n?>>")
        if temp == "yes" or temp == "y":
            print("Closed Shell")
            sys.exit()
        else:
            print("Canceled")
            
    def do_cd(self,arg):    #change dir command
        try:
            os.chdir(arg)
        except OSError:
            print("*** Invalid Directory")
        
    def do_del(self,arg):   #delete file command
        print("Tip: Use rmdir To Delete Folders")
        temp = input(f"Do you Want to delete {arg}\n?>>")
        if temp == "y" or temp == "yes":
            os.remove(arg)
        else:
            print("Canceled")
        
    def do_rmdir(self,arg): # delete directory command
        temp = input(f"Do you Want to delete {arg}\n?>>")
        if temp == "y" or temp == "yes":
            try:
                os.rmdir(arg)
            except OSError as error:
                print("*** ", error)
                print("*** Cannot Remove Directory\nTip : You must empty a directory before removing it")
        else:
            print("Canceled")
            
    def do_mkdir(self,arg):     #make directory command
        try:
            os.mkdir(arg)
        except OSError:
            print("*** Incorrect Use Of Command")
            
    def do_rename(self,arg):    # rename file command
        args = arg.split(" ")
        try:
            os.rename(args[0], args[1])
        except OSError:
            print("*** Incorrect Use Of Command")
    
    def do_run(self,arg):       # run file commmand
        exec(open(arg).read())
        
    def do_format(self,arg):    #remove every file on the device
        if arg == "--all":
            valid = input("Do you want to delete Every single file on this device INCLUDING THIS SHELL\nType: \"Yes Delete All\"\n!?> ")
            if valid == "Yes Delete All":
                cur = os.listdir()
                for x in range(len(cur)):
                    try:
                        os.remove(cur[x])
                        print("Removed",cur[x])
                    except OSError:
                        os.rmdir(cur[x])
                        print("Removed",cur[x])
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
                print("Removed Every File\nDone!")
            else:
                print("Canceled")
                
    def do_out(self,arg): #ouput contents of file command 
        cwd = os.getcwd()
        print("\n",open(f"{cwd}{arg}", "r").read(),"\n")
    
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


# Runs program if is not imported                
if __name__ == "__main__":
    import os, utime, machine, cmd, sys, gc
    pyshell().cmdloop()