
from subprocess import Popen, PIPE
import os
import sys
import importlib.util

os.system('clear')


def run_cmd(cmd):
    sp=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
    rt=sp.wait()
    out,err=sp.communicate()
    return out


def is_root():
    if os.getuid()==0:
        return True
    else:
        return False

try:
    if is_root()==True:
        print("\n\nYou are \"ROOT\" -- Let's rock ...")
    else:
        print("\n\nYou're NOT \"ROOT\" -- Please elevate privileges ...")
        sys.exit(1)

except Exception as e:
    print(e)
    print("Please rectify the error and try again ...")

pkg_name = 'atop'

try:
    spec= importlib.util.find_spec(pkg_name)
    if spec is None:
        print(pkg_name + " is NOT installed ...")
        #sys.exit(1)
        print("Hold on ... Installing {}".format(pkg_name))
        run_cmd('apt-get install %s' % (pkg_name))

except Exception as e:
    print(e)
    print("Please rectify error ...")
    sys.exit(3)
