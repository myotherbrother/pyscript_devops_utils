#!/usr/bin/env python3

import os
import sys
import stat
#directory=sys.argv[1]
#filename=sys.argv[2]
def create_pyscript(directory, filename):
    #this function creates a new pyscript file, adds the interpreter.
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
    directory = sys.argv[1]
    filename = sys.argv[2]
    fullname = create_pyscript(directory, filename)
    edit_perms(fullname)
    sys.exit(0)
create_pyscript(sys.argv[1], sys.argv[2])
