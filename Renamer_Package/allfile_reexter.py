import renamermodule

print("Welcome to the Universal File Extension Changer! \n")

file_locate = input("Where are the target files located?: ")

file_ext = input("What new extension would you like to assign to the files?: ")

datalist = []
listt = file_ext.split()
datalist.append([listt])
print(datalist)

confirm = input("""You are about to re-designate all of the files located at:
 '"""+file_locate+"' with the extension, '"+file_ext+"""'. 
Would you like to proceed? (y/n): """)

if confirm == 'n':
    import sys
    sys.exit()

print("Please wait...")

renamermodule.file_reexter(file_ext,file_locate)

print("Success!")