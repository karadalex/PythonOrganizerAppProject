# for mac users
import os
import sys

def runOnMac():
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    sys.path.append("/usr/local/Cellar/wxpython/3.0.2.0/lib/python2.7/site-packages/wx-3.0-osx_cocoa/")
    import wx


runOnMac()
# import PythonOrganizerAppProject1 module
import PythonOrganizerAppProject

#Run the main function of the program
PythonOrganizerAppProject.run_main()
