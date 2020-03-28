#!/usr/bin/env python3

import os
import sys
directory=sys.argv[1]
filename=sys.argv[2]
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


create_pyscript(sys.argv[1], sys.argv[2])
