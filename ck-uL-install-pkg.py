
from subprocess import Popen, PIPE
import subprocess
import os
import sys
import importlib.util
import pkgutil

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
status = subprocess.getstatusoutput("dpkg-query -W -f='${Status}' " + pkg_name)

if status[0]==0:
    print(pkg_name + " installed -- nothing to do ...")
else:
    print("Installing: " + pkg_name)
    try:
       run_cmd('apt-get install %s' % (pkg_name))
       print(pkg_name + " Installed successfully ...")

    except Exception as e:
       print(e)
       print("Error installing package  ...")
       sys.exit(3)
