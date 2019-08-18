def file_rename(name,location):
    import os
    from sub_package11 import NameCruncher

    os.chdir(location)
    dirlist = os.listdir()



    num_file = 1 
    for filename in dirlist:
        ext = NameCruncher.ext(filename)
        if filename.endswith(ext):
            newname = name+str(num_file)+ext
            os.rename(filename,newname)
            num_file += 1

def file_reexter(ext,location):
    import os
    from sub_package11 import NameCruncher

    os.chdir(location)
    dirlist = os.listdir()

    for filename in dirlist:
        name = NameCruncher.name(filename)
        newname = name+ext
        os.rename(filename,newname)
