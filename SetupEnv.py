import os
import sys
import pip
import subprocess

from sys import platform

version = sys.version_info.major
yesList = ["YES", "Y", ""]
noList = ["NO", "N"]
osList = ["LINUX", "LINUX2", "WIN32", "DARWIN"]
envName = "Python_101"
if len(sys.argv) > 1:
    envName = sys.argv[1]
pythonBinWin = os.path.join(os.getcwd(), envName, "Scripts\\python")
pythonBinLin = os.path.join(os.getcwd(), envName, "bin/python")
reqName = "requirements.txt"
reqFlag = False
if len(sys.argv) > 2:
    reqName = sys.argv[2]
    reqFlag = True
activateThisFile = os.path.join(os.getcwd(), envName, "bin/activate_this.py")

def install(package):
    print("Installing {}...".format(package))
    pip.main(["install", package])

def setup_linux():
    print("Beginning install")
    install("virtualenv")
    print("Setting up virtual environment: " + envName)
    subprocess.call(["virtualenv", envName])
    print("Installing necessary imports in virtual environment")
    if version == 2:
        execfile(activateThisFile, dict(__file__ = activateThisFile))
    else:
        exec (activateThisFile, dict(__file__ = activateThisFile))
    if reqFlag:
        subprocess.call([pythonBinLin, "pipInstall.py", reqName])
    else:
        subprocess.call([pythonBinLin, "pipInstall.py"])
    print("Switching to new environment")
    os.system('/bin/bash --rcfile setActive.sh ' + str(os.getcwd()))
    print("Environment Setup")
    
def setup_windows():
    install("virtualenv")
    print("Setting up virtual environment: " + envName)
    subprocess.call(["virtualenv", envName])
    print("Installing necessary imports in virtual environment")
    if reqFlag:
        subprocess.call([pythonBinWin, "pipInstall.py", reqName])
    else:
        subprocess.call([pythonBinWin, "pipInstall.py"])
    print("Environment Setup")
    print("To switch to your new environment, please enter the following: '" + str(os.getcwd()) +
          "\\" + envName + "\\Scripts\\activate")

def setup_osx():
    print("Beginning install")
    install("virtualenv")
    print("Setting up virtual environment: " + envName)
    subprocess.call(["virtualenv", envName])
    print("Installing necessary imports in virtual environment")
    if version == 2:
        execfile(activateThisFile, dict(__file__ = activateThisFile))
    else:
        exec (activateThisFile, dict(__file__ = activateThisFile))
    if reqFlag:
        subprocess.call([pythonBinLin, "pipInstall.py", reqName])
    else:
        subprocess.call([pythonBinLin, "pipInstall.py"])
    print("Switching to new environment")
    os.system('/bin/bash --rcfile setActive.sh ' + str(os.getcwd()))
    print("Environment Setup")
    
def setup3():
    version = [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]
    print("Python {}.{}.{} detected".format(*version))
    prompt = True
    while(prompt):
        if platform == "linux" or platform == "linux2":
            answer = input("Linux OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_linux()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        elif platform == "win32":
            answer = input("Windows OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_windows()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        elif platform == "darwin":
            answer = input("Mac OSX detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_osx()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        else:
            print("This OS is not supported. Exiting script...")

def setup2():
    version = [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]
    print("Python {}.{}.{} detected".format(*version))
    prompt = True
    while (prompt):
        if platform == "linux" or platform == "linux2":
            answer = raw_input("Linux OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_linux()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        elif platform == "win32":
            answer = raw_input("Windows OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_windows()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid raw_input.")
        elif platform == "darwin":
            answer = raw_input("Mac OSX detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_osx()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        else:
            print("This OS is not supported. Exiting script...")

def main():
    if version == 2:
        setup2()
    else:
        setup3()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Too many arguments, see usage.")
    main()