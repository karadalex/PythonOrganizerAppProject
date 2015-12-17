import os


def go():
    """

    @rtype: changes current Directory to be PythonOrganizerAppProject1
    """
    cwd = os.getcwd()
    listCwd = cwd.split("\\")
    try:
        listCwd.remove("codeFilesPackage")
    except ValueError:
        pass
    cwdNew = ""
    for i in range(len(listCwd)-1):
        cwdNew += listCwd[i] + "\\"
    cwdNew += listCwd[-1]
    os.chdir(cwdNew)
