import os
import sys
import subprocess

filePath = os.getcwd()

if len(sys.argv) > 1:
    subprocess.call(["pip", "install", "-r", os.path.join(filePath, sys.argv[1])])
else:
    subprocess.call(["pip", "install", "-r", os.path.join(filePath, "requirements.txt")])