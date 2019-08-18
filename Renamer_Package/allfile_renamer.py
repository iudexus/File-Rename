#recently expanded to modify any file type by extrapolating the extansion

import renamermodule

print("Welcome to the Universal File Renamer! \n")

file_locate = input("Where are the target files located?: ")

file_name = input("What new name would you like to assign to the files?: ")

confirm = input("""You are about to rename and enumerate all of the files
located at: '"""+file_locate+"' with the name, '"+file_name+"""'. 
Would you like to proceed? (y/n): """)

if confirm == 'n':
    import sys
    sys.exit()

print("Please wait...")

renamermodule.file_rename(file_name,file_locate)

print("Success!")