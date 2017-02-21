import os
import subprocess

filePath = os.getcwd()

subprocess.call(["pip", "install", "-r", os.path.join(filePath, "requirements.txt")])