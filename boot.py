from sys import modules
def shell():
    exec(open("/shell.py").read())
    return __import__(mod_name)