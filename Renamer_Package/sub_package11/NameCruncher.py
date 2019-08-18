"""This module is designed to seperate the name of the file from it's extension
if you want the name, call crunch, if you want the extension,call extext"""



def ext(filename):
    name, ext = filename.split(".")
    return str("."+ext)

def name(filename):
    name, ext = filename.split(".")
    return str(name)

