#!/usr/bin/env python3

import os
import sys
import argparse



def create_pyscript(filename, directory):
    #this function creates a new pyscript file, adds the interpreter.
    dir_base = os.getcwd()
    
    if "./" in directory:
        dirleaf = directory.split("./")[1]
        directory = "{}/{}".format(dir_base, dirleaf)
    elif "/" not in directory:
        directory = "{}/{}".format(dir_base, directory)
    else:
        pass

    if not os.path.isdir(directory):
        os.mkdir(directory)

    os.chdir(directory)
    envpy3 = "#!/usr/bin/env python3\n"
    fullname = os.path.join(directory, filename)
    if not os.path.exists(fullname):
        with open(fullname, "w") as open_file:
            open_file.write(envpy3)
    else:
        print("~~ERROR!~~, {} already exists!".format(fullname))
        sys.exit(1)

    return fullname

def edit_perms(fullname):
    # changes permissions on newly created script file using chmod +x
    os.chmod(fullname, 0o775) 
    

if __name__ == "__main__":
    dir_base = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help="Script name is required")
    parser.add_argument('-d', type=str, default=dir_base, help="script location")
    args = parser.parse_args()
    filename=args.f
    directory=args.d
    fullname = create_pyscript(filename, directory)
    edit_perms(fullname)
    sys.exit(0)
create_pyscript()
